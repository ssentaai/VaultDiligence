# Agent Scope Definitions Schema

Companion documentation for `spec/agent-scopes.json`. The JSON file is the
machine-readable scope definition consumed by `.claude/hooks/validate-tool-purpose.py`
(Fix 74). This markdown documents what the JSON means and how to edit it.

## Why this file exists

Agent scopes are described narratively in `.claude/agents/architecture.md`
(e.g. "All fields with a primary source in on-chain state, live market
data, or free registries"). The hook can't parse narrative descriptions
into field-ID matchers. The JSON provides a structured form the hook
reads at startup.

When agent scopes change in `architecture.md`, this JSON must be updated
to match. There is no auto-derivation; the JSON is authoritative for the
hook regardless of what architecture.md says.

## File location

`spec/agent-scopes.json`

JSON (not YAML) was chosen for portability — JSON parsing is in the
Python stdlib and works in every VaultDiligence deployment without the
PyYAML dependency.

## Schema

```
{
  "agents": {
    "<agent_id>": {
      "name": "<human-readable name>",
      "description": "<one-paragraph scope description>",
      "scope_field_families": ["F-XXX", ...],
      "scope_categories": ["Category Name", ...],
      "reads_findings_live": true|false,
      "allow_fetch_with_warning": true|false,    // optional, A3/A6 only
      "allow_recheck_cited_sources": true|false, // optional, A6 only
      "stop_condition_text": "<text for human reference, not enforced>"
    },
    ...
  },
  "hook": {
    "default_mode": "warn"|"block",
    "silent_outside_pack": true|false,
    "missing_purpose_mode": "warn"|"block",
    "unknown_field_mode": "warn"|"block"
  }
}
```

## Scope-matching rules

A field is in scope for an agent if EITHER of these is true:

1. The field's family prefix (e.g. `F-CTR` for `F-CTR-001`) is in the
   agent's `scope_field_families` list, OR
2. The field's `Category` (extracted from the field's markdown
   definition under `**Category**:`) is in the agent's
   `scope_categories` list.

Either condition is sufficient. The two paths are redundant on purpose:
families catch most cases, categories catch fields whose family-letter
encoding doesn't perfectly match the agent's domain.

## Agent scope rationale

### A1 — Evidence Agent
Field families: F-CTR, F-FIN, F-COL, F-LIQ, F-MKT, F-ORC, F-SEC, F-TECH
Categories: Contract, Oracle, Market Data, Technical

A1 fetches evidence from on-chain state, DEX/CEX/oracle prices, and
free public registries (DefiLlama, block explorers, GLEIF,
OpenCorporates). The scope reflects this — the included families are
those whose Primary Source per field-definitions is an on-chain
mechanism or free registry. F-RIS is intentionally NOT in A1 (it's
incident history, which is documents). F-OPS is NOT in A1 (operational
team data is documents).

### A2 — Document and Counterparty Agent
Field families: F-OPS, F-ENT, F-LEG, F-CUR, F-CUS, F-GOV, F-RAT,
F-PKG, F-PRJ, F-TAX, F-HED, F-RIS
Categories: Operational, Entity, Legal, Rating Pointer, Risk

A2 fetches FORMAL documentation: prospectuses, governance forums,
audit reports, regulatory filings. The scope reflects this — operator
docs, entity registries, legal documents, curator/custody disclosures.
F-RIS is here (incident history is in published reports). F-CTR is
NOT here (contract data is on-chain, A1's job).

### A3 — Adversarial Synthesis
Empty field-family scope. A3 reads from A1 and A2 outputs and
synthesizes. The hook will warn (not block) when A3 makes external
fetches, because A3's correct pattern is to append a TRIGGER to
`findings-live.md` and let A1 or A2 do the fetching.

`allow_fetch_with_warning: true` means external fetches by A3 produce
a stderr warning but do not block. This preserves the option for
operator-driven exceptions where A3 genuinely needs to verify
something live.

### A6 — Verification Agent
Empty field-family scope, with `allow_recheck_cited_sources: true`.
A6 verifies claims against their cited sources. If a verification
check requires re-fetching a source already cited in evidence, that's
legitimate — the hook checks the URL against URLs in evidence-register
and allows it without warning. Other fetches by A6 produce a warning
but don't block.

## Hook configuration

`default_mode`: 'warn' or 'block'. The hook starts in 'warn' mode for
the first few packs after Fix 74 ships. Once we have data on whether
the scope rules are well-calibrated, switch to 'block' for true
enforcement.

`silent_outside_pack`: When true (default), the hook does nothing when
the operator is using Claude Code outside an active pack. Detected by
checking for absence of `VAULTDILIGENCE_CURRENT_AGENT` env var, OR absence
of an "Active Vault" line in the working session notes.

`missing_purpose_mode`: How to handle tool calls that don't include
a `purpose` parameter at all. Initially 'warn' so the convention rolls
out without breaking active packs. Once agents reliably include
purpose, can be set to 'block'.

`unknown_field_mode`: Always 'block', regardless of override. A field
ID cited as evidence that doesn't exist in the field registry is
always wrong — this is the one absolute rule.

## How to edit

1. Update agent scope: edit the relevant agent's `scope_field_families`
   or `scope_categories` list in the JSON.
2. New field family: if you add a new family prefix (e.g. F-NEW), add
   it to whichever agent's scope it belongs in.
3. Change hook behavior: edit the `hook` section.
4. Test: run `python3 .claude/hooks/validate-tool-purpose.py --self-test`
   to verify the file parses and scope rules are coherent.

## What this file does NOT do

- Does not control which fields agents *should* fill in. That's
  controlled by the field registry's `Required?` flag and per-vault-type
  applicability.
- Does not control which sources agents can use for which fields.
  That's the source-registry's job (Fix 70).
- Does not enforce scope at write time. The hook only fires PreToolUse
  on fetches. Evidence-write validation is a separate hook.
- Does not enumerate skills. Skills are loaded by trigger match in
  `.claude/skills/_index.md`, not by agent scope.
