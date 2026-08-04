#!/usr/bin/env python3
"""
VaultDiligence External-Sources Registry Validator (Fix 70)

Validates entries in knowledge/external-sources/*.md against the contract in
spec/external-sources-schema.md. The binding check is that every field ID in an
entry's covers_field_ids resolves to a real field file in
knowledge/data-model/fields/ — the registry's reason to exist is the
source <-> field binding.

Modes:
  (default)        validate all registry entries; non-zero exit on any failure
  --rebuild-index  regenerate knowledge/external-sources/_index.md (tier-grouped)
  --check-coverage acquisition-coverage map: which of the 346 fields have a source
  --self-test      confirm the live exemplar passes and a broken synthetic fails

Stdlib only (no PyYAML), matching scripts/validate-incidents.py house style.

SCHEMA-DRIFT NOTE: the live exemplar accountable-data-feeds.md is a SUPERSET of
spec/external-sources-schema.md. The validator therefore:
  - ALLOWS unknown/extra frontmatter keys (e.g. covers_stablecoins_known)
  - ALLOWS inline "# ..." comments on scalars and list items
  - ACCEPTS two live-exemplar enum values not in the schema doc:
      auth: unknown            (schema doc lists none|api-key|rate-limited-anonymous|oauth|other)
      freshness_typical: continuous  (schema doc lists realtime..static)
    Both are flagged for operator reconciliation (add to schema doc, or fix the
    exemplar). They are accepted, not silently — see DRIFT_VALUES below.
"""

import argparse
import os
import re
import sys
from pathlib import Path

try:  # avoid the cp1252 console crash that bit validate-incidents.py
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[1])
REG_DIR = PROJECT_DIR / "knowledge" / "external-sources"
FIELDS_DIR = PROJECT_DIR / "knowledge" / "data-model" / "fields"
INDEX_PATH = REG_DIR / "_index.md"

# Files in REG_DIR that are NOT source entries
NON_ENTRY = {"_index.md", "_pending.md", "_rejected.md"}

REQUIRED_KEYS = [
    "schema_version", "id", "name", "provider", "url_base", "source_tier",
    "purpose", "auth", "freshness_typical", "freshness_max_trusted",
    "covers_chains", "covers_field_ids", "fallback_sources", "status", "added_in",
]
LIST_KEYS = {"purpose", "covers_chains", "covers_field_ids", "fallback_sources"}

TIERS = {"ON-CHAIN", "FORMAL", "EXPERT", "INFORMAL"}
# 'unknown' added to the schema-doc enum 2026-06-19 (drift closed).
AUTHS = {"none", "api-key", "rate-limited-anonymous", "oauth", "other", "unknown"}
FRESH = {"realtime", "sub-minute", "minute", "hourly", "daily", "weekly", "static"}
STATUS = {"active", "deprecated", "candidate", "blocked"}
# access_mode distinguishes 'VaultDiligence verifies' (fetch) from 'analyst obtains' (pointer-*).
# Enum-checked when present; absent defaults to 'fetch' so pre-existing entries do not break.
ACCESS_MODES = {"fetch", "pointer-gated", "pointer-paid"}
# Enum drift closed 2026-06-19 (auth:unknown promoted to schema; exemplar freshness
# typo 'continuous' -> 'realtime'). Sets kept (empty) so the warning paths stay wired
# for any future drift without code changes.
DRIFT_VALUES = {"auth": set(), "freshness_typical": set()}

DURATION_RE = re.compile(r"^\d+(s|m|h|d|w)$")
TIER_ORDER = ["ON-CHAIN", "FORMAL", "EXPERT", "INFORMAL"]

BODY_SECTIONS = [
    "What this source provides",
    "Source tier rationale",
    "When to use it",
    "When NOT to use it",
    "Authentication and rate limits",
    "Cross-references",
    "Notes",
]

NO_FALLBACK_RE = re.compile(r"no\s+fallback", re.IGNORECASE)


def strip_inline_comment(s):
    """Remove a trailing ' # comment' (space-hash) but never a URL fragment '#x'."""
    return re.sub(r"\s+#.*$", "", s).strip()


def parse_frontmatter(text):
    """Minimal YAML-ish parser: scalars + string lists, inline comments stripped.
    Returns (fm: dict, body: str) or (None, error_str)."""
    if not text.startswith("---"):
        return None, "file does not start with '---' frontmatter delimiter"
    end = text.find("\n---", 3)
    if end < 0:
        return None, "frontmatter not closed with '---' delimiter"
    fm_text = text[3:end].strip()
    body = text[end + 4:]

    fm = {}
    current_list = None
    for raw in fm_text.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            continue
        # full-line comment
        if line.lstrip().startswith("#"):
            continue
        # list item
        if line.lstrip().startswith("- "):
            if current_list is not None:
                current_list.append(strip_inline_comment(line.lstrip()[2:]))
            continue
        # top-level key: value
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, value = line.partition(":")
            key = key.strip()
            value = strip_inline_comment(value)
            if value == "":
                fm[key] = []
                current_list = fm[key]
            elif value.startswith("[") and value.endswith("]"):
                inner = value[1:-1].strip()
                fm[key] = [x.strip() for x in inner.split(",")] if inner else []
                current_list = None
            else:
                fm[key] = value
                current_list = None
            continue
        # anything else (indented continuation) is ignored — tolerant by design
    return (fm, body), None


def validate_text(text, slug):
    """Return (errors: list[str], warnings: list[str], fm: dict)."""
    errors, warnings = [], []
    parsed, err = parse_frontmatter(text)
    if err:
        return [f"frontmatter: {err}"], [], {}
    fm, body = parsed

    # required keys present
    for k in REQUIRED_KEYS:
        if k not in fm:
            errors.append(f"missing required key: {k}")
    # list-typed keys must actually be lists
    for k in LIST_KEYS:
        if k in fm and not isinstance(fm[k], list):
            errors.append(f"{k} must be a list (got scalar {fm[k]!r})")

    # enums
    if fm.get("source_tier") not in TIERS:
        errors.append(f"source_tier={fm.get('source_tier')!r} not in {sorted(TIERS)}")
    if fm.get("auth") not in AUTHS:
        errors.append(f"auth={fm.get('auth')!r} not in {sorted(AUTHS)}")
    elif fm.get("auth") in DRIFT_VALUES["auth"]:
        warnings.append(f"auth={fm.get('auth')!r} is a live-exemplar value not in the schema-doc enum (drift; accepted)")
    if fm.get("freshness_typical") not in FRESH:
        errors.append(f"freshness_typical={fm.get('freshness_typical')!r} not in {sorted(FRESH)}")
    elif fm.get("freshness_typical") in DRIFT_VALUES["freshness_typical"]:
        warnings.append(f"freshness_typical={fm.get('freshness_typical')!r} is a live-exemplar value not in the schema-doc enum (drift; accepted)")
    if fm.get("status") not in STATUS:
        errors.append(f"status={fm.get('status')!r} not in {sorted(STATUS)}")
    # access_mode: enum-checked when present; absent defaults to 'fetch'
    if "access_mode" in fm and fm.get("access_mode") not in ACCESS_MODES:
        errors.append(f"access_mode={fm.get('access_mode')!r} not in {sorted(ACCESS_MODES)}")
    if not (isinstance(fm.get("freshness_max_trusted"), str)
            and DURATION_RE.match(fm.get("freshness_max_trusted", ""))):
        errors.append(f"freshness_max_trusted={fm.get('freshness_max_trusted')!r} must match a duration like 4h, 30m, 1d, 7d")

    # covers_field_ids — non-empty AND every ID resolves to a real field (the binding check)
    cfi = fm.get("covers_field_ids")
    if not isinstance(cfi, list) or len(cfi) == 0:
        errors.append("covers_field_ids must be a non-empty list")
    else:
        for fid in cfi:
            if not re.match(r"^F-[A-Z]+-\d+[a-z]?$", fid):
                errors.append(f"covers_field_ids entry {fid!r} is not a field-ID shape")
            elif not (FIELDS_DIR / f"{fid}.md").is_file():
                errors.append(f"covers_field_ids cites {fid} which does not exist in knowledge/data-model/fields/")

    # fallback_sources non-empty OR explicit no-fallback statement in body
    fbs = fm.get("fallback_sources")
    has_fb = isinstance(fbs, list) and len(fbs) > 0
    if not has_fb and not NO_FALLBACK_RE.search(body):
        errors.append("fallback_sources is empty and body has no explicit 'no fallback' statement")

    # body sections — all present, in order
    positions = []
    for sec in BODY_SECTIONS:
        m = re.search(r"^##\s+" + re.escape(sec) + r"\s*$", body, re.MULTILINE)
        if not m:
            errors.append(f"missing required body section: '## {sec}'")
        else:
            positions.append((sec, m.start()))
    if len(positions) == len(BODY_SECTIONS):
        ordered = [p[1] for p in positions]
        if ordered != sorted(ordered):
            errors.append("body sections present but out of canonical order")

    # id should match filename slug (advisory)
    if fm.get("id") and slug and fm["id"] != slug:
        warnings.append(f"id={fm['id']!r} does not match filename slug {slug!r}")

    return errors, warnings, fm


def validate_entry(path):
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"cannot read file: {e}"], [], {}
    return validate_text(text, path.stem)


def entry_paths():
    if not REG_DIR.is_dir():
        return []
    return sorted(p for p in REG_DIR.glob("*.md") if p.name not in NON_ENTRY)


# ---------- modes ----------

def mode_validate():
    paths = entry_paths()
    print(f"=== validate-sources: {len(paths)} entr{'y' if len(paths)==1 else 'ies'} ===")
    any_fail = False
    for p in paths:
        errors, warnings, _ = validate_entry(p)
        if errors:
            any_fail = True
            print(f"FAIL  {p.name}")
            for e in errors:
                print(f"        - {e}")
        else:
            print(f"OK    {p.name}")
        for w in warnings:
            print(f"        ~ warning: {w}")
    return 1 if any_fail else 0


def mode_rebuild_index():
    rc = mode_validate()
    if rc != 0:
        print("\nIndex NOT rebuilt — fix validation failures first.")
        return rc
    by_tier = {t: [] for t in TIER_ORDER}
    for p in entry_paths():
        _, _, fm = validate_entry(p)
        by_tier.setdefault(fm.get("source_tier", "INFORMAL"), []).append(fm)
    lines = [
        "# External Sources Registry — Index",
        "",
        "Generated by `scripts/validate-sources.py --rebuild-index`. Do not edit by hand.",
        "Schema: `spec/external-sources-schema.md`. Add entries via `.claude/skills/source-add/SKILL.md`.",
        "",
    ]
    for tier in TIER_ORDER:
        lines.append(f"## {tier}")
        lines.append("")
        rows = sorted(by_tier.get(tier, []), key=lambda f: f.get("id", ""))
        if not rows:
            lines.append("(none yet)")
        else:
            for f in rows:
                lines.append(f"- {f.get('id','?')} — {f.get('name','?')} — {f.get('status','?')}")
        lines.append("")
    INDEX_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"\nRebuilt {INDEX_PATH} ({sum(len(v) for v in by_tier.values())} entries).")
    return 0


def mode_check_coverage():
    all_fields = sorted(p.stem for p in FIELDS_DIR.glob("F-*.md"))
    total = len(all_fields)
    covered = {}  # field_id -> set of tiers covering it
    tier_count = {t: 0 for t in TIER_ORDER}
    paths = entry_paths()
    for p in paths:
        errors, _, fm = validate_entry(p)
        tier = fm.get("source_tier", "?")
        if tier in tier_count:
            tier_count[tier] += 1
        for fid in (fm.get("covers_field_ids") or []):
            if (FIELDS_DIR / f"{fid}.md").is_file():
                covered.setdefault(fid, set()).add(tier)

    covered_ids = sorted(covered)
    uncovered = [f for f in all_fields if f not in covered]

    print("=== ACQUISITION COVERAGE MAP ===")
    print(f"Registered sources : {len(paths)}  (ON-CHAIN {tier_count['ON-CHAIN']}, "
          f"FORMAL {tier_count['FORMAL']}, EXPERT {tier_count['EXPERT']}, INFORMAL {tier_count['INFORMAL']})")
    print(f"Total fields       : {total}")
    print(f"Covered (>=1 src)  : {len(covered_ids)}")
    print(f"Uncovered          : {len(uncovered)}")
    print("")
    print("Distinct fields covered, by covering-source tier:")
    for t in TIER_ORDER:
        n = sum(1 for f, tiers in covered.items() if t in tiers)
        print(f"  {t:<9}: {n}")
    print("")
    if covered_ids:
        print(f"Covered field IDs ({len(covered_ids)}):")
        print("  " + ", ".join(covered_ids))
        print("")
    print(f"UNCOVERED field IDs ({len(uncovered)}) — the acquisition target:")
    # wrap ~8 per line for readability
    for i in range(0, len(uncovered), 8):
        print("  " + ", ".join(uncovered[i:i + 8]))
    return 0


SYNTHETIC_BAD = """---
schema_version: 1
id: broken-synthetic
name: Broken Synthetic Source
provider: Test
url_base: https://example.test
source_tier: SEMI-FORMAL
auth: magic
access_mode: teleport
freshness_typical: occasionally
freshness_max_trusted: soon
covers_chains:
  - ALL
covers_field_ids:
  - F-DOES-NOT-EXIST-999
fallback_sources: []
status: maybe
added_in: v54
---

## What this source provides

Nothing real.

## Notes

Missing most body sections on purpose.
"""


def mode_self_test():
    ok = True
    # 1. live exemplar must pass
    exemplar = REG_DIR / "accountable-data-feeds.md"
    if not exemplar.is_file():
        print("[FAIL] exemplar accountable-data-feeds.md not found")
        return 1
    errs, warns, _ = validate_entry(exemplar)
    if errs:
        print("[FAIL] live exemplar accountable-data-feeds.md should pass but reported:")
        for e in errs:
            print(f"         - {e}")
        ok = False
    else:
        print("[PASS] live exemplar accountable-data-feeds.md validates clean"
              + (f" ({len(warns)} drift warning(s))" if warns else ""))
        for w in warns:
            print(f"         ~ {w}")
    # 2. synthetic broken entry must fail
    berrs, _, _ = validate_text(SYNTHETIC_BAD, "broken-synthetic")
    if berrs:
        print(f"[PASS] synthetic broken entry correctly rejected ({len(berrs)} errors), e.g.:")
        for e in berrs[:5]:
            print(f"         - {e}")
    else:
        print("[FAIL] synthetic broken entry should have failed but passed")
        ok = False
    print("\nSELF-TEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="VaultDiligence external-sources registry validator (Fix 70)")
    ap.add_argument("--rebuild-index", action="store_true", help="regenerate _index.md (tier-grouped)")
    ap.add_argument("--check-coverage", action="store_true", help="acquisition-coverage map vs the field registry")
    ap.add_argument("--self-test", action="store_true", help="confirm exemplar passes and a broken synthetic fails")
    args = ap.parse_args()

    if args.self_test:
        return mode_self_test()
    if args.check_coverage:
        return mode_check_coverage()
    if args.rebuild_index:
        return mode_rebuild_index()
    return mode_validate()


if __name__ == "__main__":
    sys.exit(main())
