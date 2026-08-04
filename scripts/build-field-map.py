#!/usr/bin/env python3
"""
VaultDiligence Document-Field Map
Pipeline entry point for every investigation.

Inverts the investigation approach:
  OLD: Start with vault address, call one API per field.
  NEW: Load field map for this vault type, identify which sources
       satisfy which fields, make ONE PASS per source, fan out to
       all fields that source covers.

This is the operator fusion equivalent for VaultDiligence.
One Morpho API call populates TVL, withdrawable, utilisation rate,
APY, and vault metadata — not five separate calls.

Usage:
  python3 scripts/build-field-map.py --vault-type VT-1 --output field-map.json
  python3 scripts/build-field-map.py --vault-type VT-3a

From investigation code:
  from build_field_map import FieldMap
  fm = FieldMap(vault_type='VT-1')
  sources = fm.sources_for_d1()
  for source in sources:
      fields = fm.fields_for_source(source)
      # One API call per source, fan out to all fields
"""

import json
import os
import sys
import csv
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).parent.parent
FIELDS_DIR = BASE / 'knowledge' / 'data-model' / 'fields'


def load_all_fields() -> list[dict]:
    """Load all field definitions from knowledge/data-model/fields/"""
    fields = []
    if not FIELDS_DIR.exists():
        return fields
    for f in sorted(FIELDS_DIR.glob('*.md')):
        field = parse_field_md(f)
        if field:
            fields.append(field)
    return fields


def parse_field_md(path: Path) -> dict | None:
    """Parse a field definition markdown file into a dict."""
    with open(path) as f:
        content = f.read()

    field = {'field_id': path.stem}
    for line in content.split('\n'):
        if line.startswith('**Field ID**:'):
            field['field_id'] = line.split(':', 1)[1].strip()
        elif line.startswith('**Field Name**:'):
            field['name'] = line.split(':', 1)[1].strip()
        elif line.startswith('**Vault Types**:'):
            raw = line.split(':', 1)[1].strip()
            field['vault_types'] = [v.strip() for v in raw.split(',')]
        elif line.startswith('**Primary Source**:'):
            field['primary_source'] = line.split(':', 1)[1].strip()
        elif line.startswith('**Collection Tier**:'):
            field['tier'] = line.split(':', 1)[1].strip()
        elif line.startswith('**D1**:'):
            field['d1'] = line.split(':', 1)[1].strip().upper() == 'Y'
        elif line.startswith('**D2**:'):
            field['d2'] = line.split(':', 1)[1].strip().upper() == 'Y'
        elif line.startswith('**Pillar(s)**:'):
            field['pillars'] = line.split(':', 1)[1].strip()
        elif line.startswith('**If Not Found — Gap Action**:'):
            field['gap_action'] = line.split(':', 1)[1].strip()
        elif line.startswith('**Required?**:'):
            field['required'] = line.split(':', 1)[1].strip().upper() == 'Y'
        elif line.startswith('**TTL**:'):
            field['ttl_hours'] = int(line.split(':', 1)[1].strip().split()[0])

    # Default TTL if not specified (Item 2: TTL in field registry)
    if 'ttl_hours' not in field:
        field['ttl_hours'] = _default_ttl(field.get('tier', 'T1'),
                                           field.get('field_id', ''))

    return field


def _default_ttl(tier: str, field_id: str) -> int:
    """
    Default TTL by field type. These become explicit once the TTL column
    is added to each field definition file (Item 2).
    """
    fid = field_id.upper()
    if 'TVL' in fid or 'APY' in fid or 'UTIL' in fid or 'LIQ' in fid:
        return 24           # Price/liquidity: 24 hours
    if 'AUDIT' in fid or 'SEC' in fid:
        return 24 * 90      # Audit status: 90 days
    if 'TEAM' in fid or 'ENT' in fid:
        return 24 * 180     # Team identity: 180 days
    if 'LEG' in fid or 'REG' in fid:
        return 24 * 365     # Legal structure: 365 days
    if 'GOV' in fid:
        return 24 * 7       # Governance: 7 days (proposals move fast)
    return 24 * 30          # Default: 30 days


# Source normalisation: map raw primary_source strings to canonical source keys
SOURCE_ALIASES = {
    'morpho':          ['morpho', 'api.morpho.org', 'morpho api', 'morpho markets'],
    'defillama':       ['defillama', 'api.llama.fi', 'llama', 'defi llama'],
    'etherscan':       ['etherscan', 'api.etherscan.io', 'on-chain', 'contract'],
    '1inch':           ['1inch', 'api.1inch.dev', '1inch pathfinder'],
    'gleif':           ['gleif', 'api.gleif.org'],
    'ofac':            ['ofac', 'sanctions'],
    'immunefi':        ['immunefi', 'bug bounty'],
    'vaultsfyi':       ['vaults.fyi', 'api.vaults.fyi'],
    'dexscreener':     ['dexscreener', 'api.dexscreener'],
    'coingecko':       ['coingecko', 'api.coingecko'],
    'fred':            ['fred', 'api.stlouisfed.org', 'risk-free rate'],
    'snapshot':        ['snapshot', 'hub.snapshot.org'],
    'github':          ['github', 'api.github.com'],
    'solodit':         ['solodit', 'solodit.xyz'],
    'rekt':            ['rekt', 'hacks', 'api.llama.fi/hacks'],
    'scrapling':       ['scrapling', 'issuer page', 'protocol docs', 'gitbook'],
    'web_search':      ['web search', 'web_search', 'search'],
    'pdf':             ['pdf', 'audit report', 'legal opinion', 'prospectus'],
}


def normalise_source(raw: str) -> str:
    """Map a raw primary_source string to a canonical source key."""
    raw_lower = raw.lower()
    for canonical, aliases in SOURCE_ALIASES.items():
        for alias in aliases:
            if alias in raw_lower:
                return canonical
    return raw_lower.split('/')[0].split('(')[0].strip()


class FieldMap:
    """
    Document-Field Map for a specific vault type and output format.
    Pipeline entry point. Load once, query repeatedly.
    """

    def __init__(self, vault_type: str = 'VT-1'):
        self.vault_type = vault_type
        self._all_fields = load_all_fields()
        self._vault_fields = self._filter_by_vault_type(vault_type)
        self._by_source = self._build_source_index()

    def _filter_by_vault_type(self, vault_type: str) -> list[dict]:
        result = []
        for f in self._all_fields:
            vts = f.get('vault_types', [])
            if not vts or vault_type in vts or 'ALL' in vts:
                result.append(f)
        return result

    def _build_source_index(self) -> dict[str, list[dict]]:
        """Build source → [fields] index."""
        index = defaultdict(list)
        for f in self._vault_fields:
            raw_source = f.get('primary_source', 'unknown')
            canonical = normalise_source(raw_source)
            index[canonical].append(f)
        return dict(index)

    def sources_for_d1(self) -> list[str]:
        """Return ordered list of sources needed for a D1 run."""
        d1_fields = [f for f in self._vault_fields if f.get('d1')]
        sources = set()
        for f in d1_fields:
            raw = f.get('primary_source', '')
            sources.add(normalise_source(raw))
        # Priority order: on-chain first, then T1 APIs, then scrapling
        priority = ['morpho', 'etherscan', 'defillama', '1inch', 'vaultsfyi',
                    'gleif', 'ofac', 'fred', 'immunefi', 'dexscreener',
                    'coingecko', 'snapshot', 'github', 'solodit', 'rekt',
                    'scrapling', 'web_search', 'pdf']
        ordered = [s for s in priority if s in sources]
        remainder = sorted(sources - set(ordered))
        return ordered + remainder

    def fields_for_source(self, source: str,
                           d1_only: bool = False) -> list[dict]:
        """Return all fields satisfied by this source."""
        fields = self._by_source.get(source, [])
        if d1_only:
            fields = [f for f in fields if f.get('d1')]
        return fields

    def field_by_id(self, field_id: str) -> dict | None:
        for f in self._vault_fields:
            if f['field_id'] == field_id:
                return f
        return None

    def ttl_hours(self, field_id: str) -> int:
        f = self.field_by_id(field_id)
        return f['ttl_hours'] if f else 24 * 30

    def print_source_plan(self, d1_only: bool = True):
        """Print the investigation plan: one block per source."""
        label = "D1" if d1_only else "Full DD"
        print(f"\nField Map — {self.vault_type} — {label}")
        print("=" * 60)
        sources = self.sources_for_d1() if d1_only else list(self._by_source)
        for source in sources:
            fields = self.fields_for_source(source, d1_only)
            if not fields:
                continue
            print(f"\n{source.upper()} ({len(fields)} fields)")
            for f in sorted(fields, key=lambda x: x['field_id']):
                req = "REQUIRED" if f.get('required') else "optional"
                ttl = f.get('ttl_hours', 720)
                print(f"  {f['field_id']:<14} {f.get('name','')[:35]:<36} "
                      f"TTL:{ttl}h  {req}")
        print()

    def to_json(self) -> dict:
        """Serialise to JSON for the investigation runner."""
        return {
            'vault_type': self.vault_type,
            'total_fields': len(self._vault_fields),
            'sources': {
                source: [
                    {
                        'field_id': f['field_id'],
                        'name': f.get('name', ''),
                        'tier': f.get('tier', 'T1'),
                        'ttl_hours': f.get('ttl_hours', 720),
                        'required': f.get('required', False),
                        'd1': f.get('d1', False),
                        'gap_action': f.get('gap_action', '')
                    }
                    for f in fields
                ]
                for source, fields in self._by_source.items()
            }
        }


# ── CLI ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Build document-field map for an investigation'
    )
    parser.add_argument('--vault-type', default='VT-1',
                        help='Vault type (VT-1, VT-3a, VT-5, etc.)')
    parser.add_argument('--d1-only', action='store_true', default=True,
                        help='Show only D1 fields (default: true)')
    parser.add_argument('--full', action='store_true',
                        help='Show all fields including D2/D3')
    parser.add_argument('--output', help='Write JSON to this file')
    parser.add_argument('--plan', action='store_true', default=True,
                        help='Print investigation plan')

    args = parser.parse_args()

    fm = FieldMap(vault_type=args.vault_type)
    d1_only = not args.full

    if args.plan:
        fm.print_source_plan(d1_only=d1_only)

    if args.output:
        data = fm.to_json()
        with open(args.output, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Written to {args.output}")
