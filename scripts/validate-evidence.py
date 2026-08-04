#!/usr/bin/env python3
"""
VaultDiligence Evidence Object Validator
Type-level enforcement of the no-inference rule.

Every field write must pass validation before entering the evidence register.
Rejects any field missing required properties or violating the schema contract.

Usage:
  from validate_evidence import validate, write_field, read_field, inherit_or_query

  # Validate before writing
  ok, reason = validate(evidence_object)
  if not ok:
      print(f"Rejected: {reason} — classify as G2 or G3")

  # Write to session evidence register
  write_field(vault_slug, evidence_object)

  # Read existing field (returns None if not yet confirmed)
  existing = read_field(vault_slug, field_id)

  # Inherit if E already confirmed, else signal to query
  field = inherit_or_query(vault_slug, field_id)
  if field:
      print(f"Inherited: {field['value']} from {field['source_uri']}")
  else:
      print("Not yet confirmed — query required")
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).parent.parent

REQUIRED_FIELDS = [
    'field_id', 'value', 'state',
    'source_uri', 'source_type', 'retrieved_at', 'confidence', 'reasoning'
]

VALID_STATES =       ['E', 'E(P)', 'G2', 'G3', 'I', 'N/A']
VALID_SOURCE_TYPES = ['ON-CHAIN', 'FORMAL', 'EXPERT', 'INFORMAL']
VALID_CONFIDENCE =   ['HIGH', 'MEDIUM', 'LOW']

# States that require a real source URI
URI_REQUIRED_STATES = ['E', 'E(P)']

# Confidence levels that are incompatible with E state
INCOMPATIBLE_CONFIDENCE = {'E': ['LOW']}

# v42: source-tier ordering for deterministic disambiguation.
# Higher index = higher authority. ON-CHAIN beats FORMAL beats EXPERT beats INFORMAL.
SOURCE_TIER_RANK = {
    'ON-CHAIN': 4,
    'FORMAL':   3,
    'EXPERT':   2,
    'INFORMAL': 1,
}


def disambiguate(existing: dict, incoming: dict) -> tuple[str, dict, str]:
    """
    v42: Deterministic conflict resolution between two evidence objects
    for the same field_id.

    Returns (decision, winning_object, rationale) where decision is one of:
      - 'incoming_wins'  — incoming has strictly higher source authority or recency
      - 'existing_wins'  — existing has strictly higher source authority or recency
      - 'conflict'       — neither rule produces a winner, state stays I

    Rules in order:
      1. Source-tier wins. ON-CHAIN > FORMAL > EXPERT > INFORMAL.
      2. Within same tier, newer retrieved_at wins.
      3. If neither rule resolves: return 'conflict' — caller writes state=I.

    Caller is responsible for applying the decision. This function does not
    mutate the register.
    """
    e_tier = SOURCE_TIER_RANK.get(existing.get('source_type'), 0)
    i_tier = SOURCE_TIER_RANK.get(incoming.get('source_type'), 0)

    # Rule 1: source-tier
    if i_tier > e_tier:
        return ('incoming_wins', incoming,
                f"incoming source_type={incoming.get('source_type')} "
                f"outranks existing {existing.get('source_type')}")
    if e_tier > i_tier:
        return ('existing_wins', existing,
                f"existing source_type={existing.get('source_type')} "
                f"outranks incoming {incoming.get('source_type')}")

    # Rule 2: same tier — recency wins
    e_when = _parse_retrieved(existing.get('retrieved_at', ''))
    i_when = _parse_retrieved(incoming.get('retrieved_at', ''))
    if e_when and i_when:
        if i_when > e_when:
            return ('incoming_wins', incoming,
                    f"same source-tier ({existing.get('source_type')}); "
                    f"incoming retrieved_at is newer")
        if e_when > i_when:
            return ('existing_wins', existing,
                    f"same source-tier ({existing.get('source_type')}); "
                    f"existing retrieved_at is newer")

    # Rule 3: cannot disambiguate — state remains I
    return ('conflict', existing,
            f"both sources are {existing.get('source_type')} "
            f"with no recency difference; state=I")


def _parse_retrieved(s: str):
    """Parse retrieved_at to a datetime, returning None on failure."""
    try:
        return datetime.fromisoformat(s.rstrip('Z'))
    except Exception:
        return None


def validate(ev: dict) -> tuple[bool, str]:
    """
    Validate an evidence object against the schema contract.
    Returns (True, "valid") or (False, rejection_reason).
    """
    # 1. All required fields present
    for f in REQUIRED_FIELDS:
        if f not in ev or ev[f] is None:
            return False, f"Missing required field: {f}"

    # 2. Valid enum values
    if ev['state'] not in VALID_STATES:
        return False, f"Invalid state '{ev['state']}'. Must be one of {VALID_STATES}"

    if ev['source_type'] not in VALID_SOURCE_TYPES:
        return False, f"Invalid source_type '{ev['source_type']}'"

    if ev['confidence'] not in VALID_CONFIDENCE:
        return False, f"Invalid confidence '{ev['confidence']}'"

    # 3. Source URI required for E and E(P)
    if ev['state'] in URI_REQUIRED_STATES:
        uri = ev.get('source_uri', '')
        if not uri or uri in ('', 'NONE', 'none'):
            return False, f"source_uri required when state={ev['state']}"
        if uri.startswith('['):
            return False, "source_uri must be a raw URL, not a markdown link"

    # 4. E state cannot have INFORMAL source type
    if ev['state'] == 'E' and ev['source_type'] == 'INFORMAL':
        return False, "state=E is incompatible with source_type=INFORMAL. Use E(P)."

    # 5. E state cannot have LOW confidence
    if ev['state'] == 'E' and ev['confidence'] == 'LOW':
        return False, "state=E is incompatible with confidence=LOW. Use E(P)."

    # 6. E state requires a non-empty value
    if ev['state'] == 'E':
        val = str(ev.get('value', '')).strip()
        if not val or val.lower() in ('unknown', 'n/a', 'none', 'null', ''):
            return False, f"state=E requires a confirmed value. Got: '{ev.get('value')}'"

    # 7. retrieved_at must be a datetime (not just a date)
    retrieved = str(ev.get('retrieved_at', ''))
    if len(retrieved) < 19:
        return False, (
            f"retrieved_at must be ISO 8601 datetime (YYYY-MM-DDTHH:MM:SSZ), "
            f"got: '{retrieved}'"
        )

    # 8. v41: optional memory_citations must be a list of strings if present
    citations = ev.get('memory_citations')
    if citations is not None:
        if not isinstance(citations, list):
            return False, "memory_citations must be a list (use [] for none)"
        for c in citations:
            if not isinstance(c, str):
                return False, f"memory_citations entries must be strings, got: {type(c).__name__}"

    # 9. v41: optional reasoning_provenance must be a string if present
    prov = ev.get('reasoning_provenance')
    if prov is not None and not isinstance(prov, str):
        return False, "reasoning_provenance must be a string anchor like 'LESSONS#slug'"

    # 10. v42: optional agent_id must be a known label if present
    agent_id = ev.get('agent_id')
    if agent_id is not None:
        if not isinstance(agent_id, str):
            return False, "agent_id must be a string"
        # Permissive: A1, A2, A3, A6, or 'unknown'. Future agents extend this list.
        if agent_id not in ('A1', 'A2', 'A3', 'A6', 'A-VERIFICATION', 'unknown'):
            return False, (
                f"agent_id must be one of A1, A2, A3, A6, A-VERIFICATION, "
                f"unknown — got {agent_id!r}"
            )

    # 11. v42: optional write_history must be a list of entries with agent_id+action+at
    history = ev.get('write_history')
    if history is not None:
        if not isinstance(history, list):
            return False, "write_history must be a list"
        for i, entry in enumerate(history):
            if not isinstance(entry, dict):
                return False, f"write_history[{i}] must be a dict"
            for k in ('agent_id', 'action', 'at'):
                if k not in entry:
                    return False, f"write_history[{i}] missing required key '{k}'"

    return True, "valid"


def register_path(vault_slug: str) -> Path:
    return BASE / 'packs' / vault_slug / 'agent-outputs' / 'evidence-register.json'


def load_register(vault_slug: str) -> dict:
    path = register_path(vault_slug)
    if not path.exists():
        return {}
    with open(path) as f:
        return json.load(f)


def save_register(vault_slug: str, register: dict):
    path = register_path(vault_slug)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(register, f, indent=2)


def write_field(vault_slug: str, evidence_object: dict) -> tuple[bool, str]:
    """
    Validate and write a field to the session evidence register.
    Returns (True, status) or (False, rejection_reason).

    v42: when an incoming write collides with an existing E field, run the
    disambiguation rules instead of silently rejecting. The decision is
    recorded as a write_history entry on the winning evidence object so
    the audit trail survives.

    status values:
      'written'                 first write of this field
      'overwritten-by-tier'     incoming wins on source-tier rule
      'overwritten-by-recency'  incoming wins on recency rule (same tier)
      'inherited'               existing wins, incoming discarded
      'conflict'                neither wins; state forced to I, both sources kept
    """
    ok, reason = validate(evidence_object)
    if not ok:
        return False, reason

    register = load_register(vault_slug)
    field_id = evidence_object['field_id']

    # First write: just record it with a fresh write_history.
    existing = register.get(field_id)
    if existing is None:
        evidence_object = _stamp_write_history(
            evidence_object, action='created',
            agent_id=evidence_object.get('agent_id', 'unknown'),
        )
        register[field_id] = evidence_object
        save_register(vault_slug, register)
        return True, "written"

    # Existing already E and incoming weaker: keep existing (v40 behaviour).
    if existing.get('state') == 'E' and evidence_object['state'] != 'E':
        return False, (
            f"Field {field_id} already confirmed as E. "
            f"Cannot overwrite with state={evidence_object['state']}. "
            "Use inherit_or_query() to check before writing."
        )

    # Conflict resolution path — v42.
    decision, winner, rationale = disambiguate(existing, evidence_object)

    if decision == 'incoming_wins':
        # Determine which rule fired
        e_tier = SOURCE_TIER_RANK.get(existing.get('source_type'), 0)
        i_tier = SOURCE_TIER_RANK.get(evidence_object.get('source_type'), 0)
        status = 'overwritten-by-tier' if i_tier != e_tier else 'overwritten-by-recency'
        winner = _stamp_write_history(
            winner, action=status,
            agent_id=evidence_object.get('agent_id', 'unknown'),
            prior_history=existing.get('write_history', []),
            rationale=rationale,
            superseded=existing,
        )
        register[field_id] = winner
        save_register(vault_slug, register)
        return True, status

    if decision == 'existing_wins':
        # No write to register, but record the attempted-but-discarded write
        # on the existing object's history so we can audit churn.
        existing = _stamp_write_history(
            existing, action='inherited-incoming-discarded',
            agent_id=evidence_object.get('agent_id', 'unknown'),
            rationale=rationale,
            superseded=evidence_object,
        )
        register[field_id] = existing
        save_register(vault_slug, register)
        return True, "inherited"

    # Conflict — state forced to I, both sources retained.
    conflict_obj = {
        **existing,
        'state':       'I',
        'value':       f"CONFLICT: {existing.get('value')} vs {evidence_object.get('value')}",
        'source_uri':  f"CONFLICT:{existing.get('source_uri')}|{evidence_object.get('source_uri')}",
        'confidence':  'LOW',
        'reasoning':   f"Disambiguation could not resolve: {rationale}",
        'conflict': {
            'source_a': {
                'uri':          existing.get('source_uri'),
                'value':        existing.get('value'),
                'retrieved_at': existing.get('retrieved_at'),
                'source_type':  existing.get('source_type'),
                'agent_id':     existing.get('agent_id', 'unknown'),
            },
            'source_b': {
                'uri':          evidence_object.get('source_uri'),
                'value':        evidence_object.get('value'),
                'retrieved_at': evidence_object.get('retrieved_at'),
                'source_type':  evidence_object.get('source_type'),
                'agent_id':     evidence_object.get('agent_id', 'unknown'),
            },
            'resolution_action': (
                f"Re-query against the highest-authority available source "
                f"({existing.get('source_type')} tier). Resolve before pack closes."
            ),
        },
    }
    conflict_obj = _stamp_write_history(
        conflict_obj, action='conflict-recorded',
        agent_id=evidence_object.get('agent_id', 'unknown'),
        prior_history=existing.get('write_history', []),
        rationale=rationale,
    )
    register[field_id] = conflict_obj
    save_register(vault_slug, register)
    return True, "conflict"


def _stamp_write_history(
    ev: dict,
    action: str,
    agent_id: str,
    prior_history: list = None,
    rationale: str = None,
    superseded: dict = None,
) -> dict:
    """
    v42: append a write_history entry to an evidence object.

    Each entry: { agent_id, action, at, rationale?, superseded_source? }.
    The history is the audit trail: when did A1 write this, when did A6
    downgrade it, when did the disambiguation rule fire and which agents
    were involved.
    """
    entry = {
        'agent_id': agent_id,
        'action':   action,
        'at':       datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
    }
    if rationale:
        entry['rationale'] = rationale
    if superseded:
        entry['superseded_source'] = {
            'uri':          superseded.get('source_uri'),
            'value':        superseded.get('value'),
            'source_type':  superseded.get('source_type'),
            'retrieved_at': superseded.get('retrieved_at'),
            'agent_id':     superseded.get('agent_id', 'unknown'),
        }
    out = dict(ev)
    history = list(prior_history) if prior_history else list(out.get('write_history', []))
    history.append(entry)
    out['write_history'] = history
    return out


def read_field(vault_slug: str, field_id: str) -> dict | None:
    """
    Read a field from the session evidence register.
    Returns the evidence object if it exists, None otherwise.
    """
    register = load_register(vault_slug)
    return register.get(field_id)


def inherit_or_query(vault_slug: str, field_id: str) -> dict | None:
    """
    ONE SOURCE PER FIELD RULE.
    If field is already confirmed as E in the session register: return it.
    The caller inherits and does not re-query.
    If not confirmed: return None. The caller must query.

    Usage:
        existing = inherit_or_query(vault_slug, 'F-FIN-010')
        if existing:
            # inherit — do not re-query
            tvl = existing['value']
        else:
            # query the source
            tvl = call_morpho_api(vault_address)
            write_field(vault_slug, {...})
    """
    field = read_field(vault_slug, field_id)
    if field and field.get('state') == 'E':
        return field
    return None


def summary(vault_slug: str) -> dict:
    """Return a summary of the current evidence register state."""
    register = load_register(vault_slug)
    counts = {s: 0 for s in VALID_STATES}
    for ev in register.values():
        state = ev.get('state', 'UNKNOWN')
        if state in counts:
            counts[state] += 1
    return {
        'vault': vault_slug,
        'total_fields': len(register),
        'by_state': counts,
        'coverage_pct': round(counts['E'] / max(len(register), 1) * 100, 1)
    }


# ── CLI ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Validate and inspect evidence objects'
    )
    subparsers = parser.add_subparsers(dest='command')

    # validate a JSON string
    v = subparsers.add_parser('validate', help='Validate a JSON evidence object')
    v.add_argument('json', help='Evidence object as JSON string')

    # summary of a vault register
    s = subparsers.add_parser('summary', help='Show evidence register summary')
    s.add_argument('vault_slug')

    # read a field
    r = subparsers.add_parser('read', help='Read a field from the register')
    r.add_argument('vault_slug')
    r.add_argument('field_id')

    args = parser.parse_args()

    if args.command == 'validate':
        try:
            obj = json.loads(args.json)
            ok, reason = validate(obj)
            if ok:
                print(f"VALID: {obj['field_id']} state={obj['state']}")
            else:
                print(f"REJECTED: {reason}")
                sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            sys.exit(1)

    elif args.command == 'summary':
        s = summary(args.vault_slug)
        print(json.dumps(s, indent=2))

    elif args.command == 'read':
        field = read_field(args.vault_slug, args.field_id)
        if field:
            print(json.dumps(field, indent=2))
        else:
            print(f"Field {args.field_id} not yet in register for {args.vault_slug}")
            sys.exit(1)

    else:
        parser.print_help()
