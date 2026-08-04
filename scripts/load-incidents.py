#!/usr/bin/env python3
"""
VaultDiligence — query the incidents registry.

Given a vault context (vault_type, optional classification-of-interest),
return the matching incidents and, for each, the diligence-signature fields
and their pre-incident states — the fields whose gap-state preceded the
incident, i.e. what an assessment should have caught.

Usage:
  python3 scripts/load-incidents.py --vault-type VT-A
  python3 scripts/load-incidents.py --vault-type VT-3a --classification depeg
  python3 scripts/load-incidents.py --vault-type VT-A --json
"""

import argparse
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
INCIDENTS_DIR = BASE / 'knowledge' / 'incidents'

# Reuse the parser from the validator (loaded as a module to avoid duplication).
import importlib.util
_v_spec = importlib.util.spec_from_file_location(
    'validate_incidents',
    BASE / 'scripts' / 'validate-incidents.py'
)
_v_mod = importlib.util.module_from_spec(_v_spec)
_v_spec.loader.exec_module(_v_mod)


def parse_diligence_signature(body):
    """
    Extract the diligence-signature items from an incident body.
    Returns a list of dicts: [{field_id, state_pre_incident, gap_action, notes}, ...].
    """
    out = []
    sig_match = re.search(
        r'## Diligence signature\s*\n(.*?)(?=\n## |\Z)',
        body,
        re.S
    )
    if not sig_match:
        return out
    sig_body = sig_match.group(1)

    # Each item starts with "- field_id: F-XXX-NNN" and continues until the next
    # item or end of section. Use a positive lookahead.
    items = re.split(r'(?m)^\s*-\s+(?=field_id:)', sig_body)
    for item in items:
        item = item.strip()
        if not item.startswith('field_id:'):
            continue
        d = {}
        m = re.match(r'field_id:\s*([^\s]+)', item)
        if m:
            d['field_id'] = m.group(1).strip().rstrip(',()')
        for key in ('state_pre_incident', 'gap_action', 'notes'):
            km = re.search(rf'{key}:\s*"?([^"\n]+(?:\n[^A-Za-z\s][^\n]*)*)"?', item)
            if km:
                d[key] = km.group(1).strip().strip('"')
        if 'field_id' in d:
            out.append(d)
    return out


def load_all_incidents():
    """Return list of (path, frontmatter_dict, body, signature_items)."""
    if not INCIDENTS_DIR.exists():
        return []
    out = []
    for path in sorted(INCIDENTS_DIR.iterdir()):
        if not path.is_file() or path.suffix != '.md' or path.name.startswith('_'):
            continue
        try:
            text = path.read_text()
        except Exception:
            continue
        parsed, err = _v_mod.parse_frontmatter(text)
        if err:
            continue
        fm, body = parsed
        sig = parse_diligence_signature(body)
        out.append((path, fm, body, sig))
    return out


def filter_by_vault_type(incidents, vault_type):
    """Return only incidents whose vault_types_at_risk includes vault_type."""
    if vault_type is None:
        return incidents
    out = []
    for entry in incidents:
        path, fm, body, sig = entry
        vts = fm.get('vault_types_at_risk', [])
        if not isinstance(vts, list):
            continue
        if vault_type in vts:
            out.append(entry)
    return out


def filter_by_classification(incidents, classification):
    if classification is None:
        return incidents
    return [e for e in incidents if e[1].get('classification') == classification]


def render_text(matched):
    print(f"\n=== Incidents matching this context: {len(matched)} ===\n")
    for path, fm, body, sig in matched:
        print(f"  {fm.get('id', path.stem)}  ({fm.get('classification')})")
        print(f"    title: {fm.get('title', '?')}")
        print(f"    date:  {fm.get('date', '?')}")
        loss = fm.get('loss_estimate_usd')
        if loss:
            try:
                li = int(str(loss).replace('_', ''))
                if li >= 1_000_000_000:
                    print(f"    loss:  ~${li/1e9:.1f}B")
                elif li >= 1_000_000:
                    print(f"    loss:  ~${li/1e6:.0f}M")
            except Exception:
                pass
        print(f"    fields in diligence signature: "
              f"{', '.join(item['field_id'] for item in sig if item.get('field_id'))}")
        print()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--vault-type', help='Filter by vault_types_at_risk (e.g. VT-A, VT-3a).')
    p.add_argument('--classification', help='Filter by classification (e.g. depeg, minting).')
    p.add_argument('--json', action='store_true', help='Machine-readable output.')
    args = p.parse_args()

    incidents = load_all_incidents()
    if not incidents:
        print("No incidents in registry.", file=sys.stderr)
        sys.exit(0)

    matched = filter_by_classification(
        filter_by_vault_type(incidents, args.vault_type),
        args.classification,
    )

    if args.json:
        out = {
            'total_in_registry': len(incidents),
            'matched': len(matched),
            'matches': [
                {
                    'id': fm.get('id'),
                    'title': fm.get('title'),
                    'date': fm.get('date'),
                    'classification': fm.get('classification'),
                    'vault_types_at_risk': fm.get('vault_types_at_risk', []),
                    'diligence_signature': sig,
                }
                for _path, fm, _body, sig in matched
            ],
        }
        print(json.dumps(out, indent=2))
    else:
        render_text(matched)


if __name__ == '__main__':
    main()
