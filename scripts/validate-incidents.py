#!/usr/bin/env python3
"""
VaultDiligence — validate the incidents registry (v44).

Reads knowledge/incidents/*.md and enforces the schema documented in
spec/incidents-schema.md. Also regenerates _index.md on demand.

Usage:
  python3 scripts/validate-incidents.py
      # validate every entry, print pass/fail summary
  python3 scripts/validate-incidents.py --rebuild-index
      # regenerate knowledge/incidents/_index.md from valid entries
  python3 scripts/validate-incidents.py --check-coverage
      # report field IDs referenced in incidents that don't exist in
      # knowledge/data-model/fields/
  python3 scripts/validate-incidents.py --json
      # machine-readable output

Exit codes:
  0 — all entries pass
  1 — at least one entry failed validation
  2 — registry directory missing
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
INCIDENTS_DIR = BASE / 'knowledge' / 'incidents'
FIELDS_DIR = BASE / 'knowledge' / 'data-model' / 'fields'
INDEX_PATH = INCIDENTS_DIR / '_index.md'

VALID_CLASSIFICATIONS = {
    'oracle', 'minting', 'redemption', 'counterparty',
    'depeg', 'governance', 'smart-contract', 'rwa-recourse',
}
VALID_LOSS_CONFIDENCE = {'HIGH', 'MEDIUM', 'LOW'}
VALID_SOURCE_TYPES = {'ON-CHAIN', 'FORMAL', 'EXPERT', 'INFORMAL'}

REQUIRED_FRONTMATTER = [
    'schema_version', 'id', 'title', 'date',
    'chains', 'protocols_directly_affected', 'vault_types_at_risk',
    'classification', 'loss_confidence', 'sources',
]

REQUIRED_BODY_SECTIONS = [
    'What happened',
    'Why it matters for diligence',
    'Diligence signature',
    'Cross-vault recurrence',
    'Lessons reference',
    'Notes',
]


def parse_frontmatter(text):
    """Minimal YAML-ish parser sufficient for our schema (no external deps)."""
    if not text.startswith('---'):
        return None, "file does not start with YAML frontmatter delimiter"
    end = text.find('\n---', 3)
    if end < 0:
        return None, "frontmatter not closed with --- delimiter"
    fm_text = text[3:end].strip()
    body = text[end + 4:]

    fm = {}
    current_key = None
    current_list = None
    current_dict_list = None  # list of dicts (e.g. sources)

    for raw in fm_text.split('\n'):
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith('#'):
            continue

        # List entry
        if line.lstrip().startswith('- '):
            value = line.lstrip()[2:].strip()
            # Inline dict: "url: https://...  type: FORMAL  retrieved: ..."
            if ':' in value and value.split(':', 1)[0].strip() in (
                'url', 'type', 'retrieved'
            ):
                # First field of a new dict in the list
                if current_dict_list is not None and current_key in fm:
                    new_dict = {}
                    k, v = value.split(':', 1)
                    new_dict[k.strip()] = v.strip()
                    fm[current_key].append(new_dict)
                continue
            if current_list is not None:
                current_list.append(value)
            continue

        # Continuation of a dict-in-list — looks like "  type: FORMAL"
        if line.startswith('    ') and ':' in line and current_dict_list is not None:
            k, v = line.strip().split(':', 1)
            if fm.get(current_key) and isinstance(fm[current_key], list) and fm[current_key]:
                last = fm[current_key][-1]
                if isinstance(last, dict):
                    last[k.strip()] = v.strip()
            continue

        # Top-level key
        if ':' in line and not line.startswith(' '):
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip()
            current_key = key
            if value == '':
                # Either a list-of-strings or a list-of-dicts to follow
                fm[key] = []
                current_list = fm[key]
                current_dict_list = fm[key] if key == 'sources' else None
            elif value.startswith('[') and value.endswith(']'):
                # Inline list
                inner = value[1:-1].strip()
                if inner == '':
                    fm[key] = []
                else:
                    fm[key] = [x.strip() for x in inner.split(',')]
                current_list = None
                current_dict_list = None
            else:
                fm[key] = value
                current_list = None
                current_dict_list = None

    return (fm, body), None


def validate_entry(path):
    """Returns (ok: bool, errors: list[str], warnings: list[str], frontmatter: dict)."""
    errors = []
    warnings = []

    try:
        text = path.read_text()
    except Exception as e:
        return False, [f"cannot read file: {e}"], [], {}

    parsed, err = parse_frontmatter(text)
    if err:
        return False, [f"frontmatter: {err}"], [], {}
    fm, body = parsed

    # 1. Required frontmatter keys
    for key in REQUIRED_FRONTMATTER:
        if key not in fm:
            errors.append(f"missing required frontmatter key: {key}")

    # 2. Schema version
    sv = fm.get('schema_version')
    if sv is not None and str(sv) != '1':
        warnings.append(f"schema_version={sv}; expected 1")

    # 3. ID matches filename
    expected_id = path.stem
    if fm.get('id') and fm['id'] != expected_id:
        errors.append(
            f"id={fm['id']!r} does not match filename {expected_id!r}"
        )

    # 4. Date format
    date = fm.get('date', '')
    if date and not re.match(r'^\d{4}-\d{2}-\d{2}$', str(date)):
        errors.append(f"date {date!r} is not YYYY-MM-DD")

    # 5. Classification in controlled vocabulary
    cls = fm.get('classification')
    if cls and cls not in VALID_CLASSIFICATIONS:
        errors.append(
            f"classification={cls!r} not in controlled vocabulary: "
            f"{sorted(VALID_CLASSIFICATIONS)}"
        )

    # 6. loss_confidence in vocabulary
    lc = fm.get('loss_confidence')
    if lc and lc not in VALID_LOSS_CONFIDENCE:
        errors.append(
            f"loss_confidence={lc!r} not in {sorted(VALID_LOSS_CONFIDENCE)}"
        )

    # 7. vault_types_at_risk is non-empty list
    vts = fm.get('vault_types_at_risk', [])
    if not isinstance(vts, list) or not vts:
        errors.append("vault_types_at_risk must be a non-empty list")

    # 8. Sources: at least one FORMAL
    sources = fm.get('sources', [])
    if not isinstance(sources, list) or not sources:
        errors.append("sources must be a non-empty list")
    else:
        for i, s in enumerate(sources):
            if not isinstance(s, dict):
                errors.append(f"sources[{i}] must be a dict with url/type/retrieved")
                continue
            for sk in ('url', 'type', 'retrieved'):
                if sk not in s:
                    errors.append(f"sources[{i}] missing key {sk!r}")
            stype = s.get('type')
            if stype and stype not in VALID_SOURCE_TYPES:
                errors.append(
                    f"sources[{i}].type={stype!r} not in {sorted(VALID_SOURCE_TYPES)}"
                )
        formal_count = sum(
            1 for s in sources if isinstance(s, dict) and s.get('type') == 'FORMAL'
        )
        if formal_count == 0:
            errors.append(
                "at least one source must be of type FORMAL "
                "(INFORMAL-only entries belong in _pending/)"
            )

    # 9. Required body sections
    for section in REQUIRED_BODY_SECTIONS:
        if f"## {section}" not in body:
            errors.append(f"missing required body section: '## {section}'")

    # 10. Diligence signature must have at least one item
    sig_match = re.search(
        r'## Diligence signature\s*\n(.*?)(?=\n## |\Z)',
        body,
        re.S
    )
    if sig_match:
        sig_body = sig_match.group(1)
        # Count "field_id:" markers
        field_count = len(re.findall(r'^\s*-\s*field_id:', sig_body, re.M))
        if field_count == 0:
            errors.append(
                "Diligence signature section has no '- field_id:' entries; "
                "an entry without diligence signature does not earn its place"
            )

    return len(errors) == 0, errors, warnings, fm


def field_ids_referenced(path):
    """Extract every F-XXX-NNN field_id mentioned in an entry's diligence signature."""
    try:
        text = path.read_text()
    except Exception:
        return set()
    return set(re.findall(r'\bF-[A-Z]+-\d+\b', text))


def known_field_ids():
    """Return the set of valid field_ids registered in knowledge/data-model/fields/."""
    out = set()
    if not FIELDS_DIR.exists():
        return out
    for f in FIELDS_DIR.iterdir():
        if f.is_file() and f.suffix == '.md':
            try:
                t = f.read_text()
                m = re.search(
                    r'^(?:id|field_id):\s*(["\']?)(F-[A-Z]+-\d+)\1',
                    t, re.M
                )
                if m:
                    out.add(m.group(2))
                elif re.match(r'^F-[A-Z]+-\d+$', f.stem):
                    out.add(f.stem)
            except Exception:
                pass
    return out


def check_coverage(entries, known):
    """Report field IDs cited in incidents but not in registry."""
    cited = {}
    for path in entries:
        for fid in field_ids_referenced(path):
            cited.setdefault(fid, []).append(path.name)
    missing = {fid: files for fid, files in cited.items() if fid not in known}
    return cited, missing


def rebuild_index(entries, results):
    """Regenerate _index.md sorted by date descending."""
    rows = []
    for path, ok, _errs, _warns, fm in results:
        if not ok:
            continue
        date = fm.get('date', '?')
        slug = fm.get('id', path.stem)
        title = fm.get('title', '?')
        cls = fm.get('classification', '?')
        vts = fm.get('vault_types_at_risk', [])
        if isinstance(vts, list):
            vts_str = ', '.join(vts)
        else:
            vts_str = str(vts)
        loss = fm.get('loss_estimate_usd')
        if loss is None or loss == 'null' or loss == '':
            loss_str = '(unknown)'
        else:
            try:
                loss_int = int(str(loss).replace('_', ''))
                if loss_int >= 1_000_000_000:
                    loss_str = f"${loss_int / 1_000_000_000:.1f}B"
                elif loss_int >= 1_000_000:
                    loss_str = f"${loss_int / 1_000_000:.0f}M"
                else:
                    loss_str = f"${loss_int:,}"
            except Exception:
                loss_str = str(loss)
        rows.append((date, slug, title, cls, vts_str, loss_str))

    rows.sort(key=lambda r: r[0], reverse=True)

    lines = [
        "# Incidents Registry",
        "",
        "Generated by `scripts/validate-incidents.py --rebuild-index`. Do not edit by hand.",
        "",
        "| Date | Slug | Title | Classification | VT at risk | Loss USD |",
        "|------|------|-------|----------------|------------|----------|",
    ]
    for date, slug, title, cls, vts, loss in rows:
        lines.append(f"| {date} | `{slug}` | {title} | {cls} | {vts} | {loss} |")
    lines.append("")

    INDEX_PATH.write_text('\n'.join(lines))
    return len(rows)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--rebuild-index', action='store_true',
                   help='Regenerate _index.md from valid entries.')
    p.add_argument('--check-coverage', action='store_true',
                   help='Report field IDs cited in incidents but not in registry.')
    p.add_argument('--json', action='store_true', help='Machine-readable output.')
    args = p.parse_args()

    if not INCIDENTS_DIR.exists():
        print(f"FATAL: {INCIDENTS_DIR} does not exist", file=sys.stderr)
        sys.exit(2)

    entries = sorted(
        f for f in INCIDENTS_DIR.iterdir()
        if f.is_file() and f.suffix == '.md' and not f.name.startswith('_')
    )

    results = []
    for path in entries:
        ok, errs, warns, fm = validate_entry(path)
        results.append((path, ok, errs, warns, fm))

    n_ok = sum(1 for _, ok, *_ in results if ok)
    n_fail = len(results) - n_ok

    if args.json:
        payload = {
            'total': len(results),
            'passed': n_ok,
            'failed': n_fail,
            'entries': [
                {
                    'file': str(path.relative_to(BASE)),
                    'ok': ok,
                    'errors': errs,
                    'warnings': warns,
                }
                for path, ok, errs, warns, _fm in results
            ],
        }
        if args.check_coverage:
            cited, missing = check_coverage(entries, known_field_ids())
            payload['coverage'] = {
                'cited_count': len(cited),
                'missing': {fid: files for fid, files in missing.items()},
            }
        print(json.dumps(payload, indent=2))
    else:
        print(f"\n=== Incidents registry validation ===\n")
        print(f"  total:  {len(results)}")
        print(f"  passed: {n_ok}")
        print(f"  failed: {n_fail}\n")

        for path, ok, errs, warns, _fm in results:
            mark = '✓' if ok else '✗'
            print(f"  {mark} {path.name}")
            for e in errs:
                print(f"      ERROR: {e}")
            for w in warns:
                print(f"      WARN:  {w}")
        print()

        if args.check_coverage:
            cited, missing = check_coverage(entries, known_field_ids())
            print(f"=== Coverage check ===\n")
            print(f"  field IDs cited in incidents: {len(cited)}")
            print(f"  field IDs cited but missing from registry: {len(missing)}\n")
            if missing:
                for fid, files in sorted(missing.items()):
                    print(f"  MISSING: {fid}  (cited in: {', '.join(files)})")
                print()

    if args.rebuild_index:
        n_indexed = rebuild_index(entries, results)
        if not args.json:
            print(f"  Rebuilt {INDEX_PATH} with {n_indexed} entries.\n")

    if n_fail > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
