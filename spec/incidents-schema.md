# Incidents Registry Schema (v44)

## Purpose

A structured catalogue of historical DeFi failures, each annotated with the diligence signature that *would have* surfaced the failure pre-allocation. Used by A3 (Adversarial Synthesis) during pack production to ask "does this vault exhibit a pattern that has previously broken?" Used during plan-mode preambles for D1 and full-dd to seed `findings-live.md` with triggers based on similar prior incidents.

This is **not a news archive**. Entries that don't carry the diligence-signature annotations are out of scope.

## What problem it solves

The v41 salience scoring has a `cross_vault_recurrence` axis weighted at zero, waiting for data. Episodic memory accumulates within a single VaultDiligence deployment; it doesn't learn from incidents VaultDiligence wasn't running for. The incidents registry is the external-event data source that lets the system reason about cross-vault patterns from before it was deployed.

Without the registry: A3 can only flag what VaultDiligence has already seen. With it: A3 can flag patterns documented in the public record, with explicit references to which fields would have surfaced them.

## Location

`knowledge/incidents/_index.md` — registry listing, one row per incident
`knowledge/incidents/<slug>.md` — one structured entry per incident

The slug format is `<year>-<short-name>`, e.g. `2025-xusd-depeg`, `2026-03-resolv-mint`, `2022-terra-collapse`.

## Entry schema

Each `<slug>.md` is a markdown file with YAML frontmatter and a structured body. Fields are:

### Frontmatter (required)

```yaml
---
id: 2026-03-resolv-mint
title: Resolv USR illegitimate mint
date: 2026-03-XX                  # YYYY-MM-DD; XX if day uncertain, document why in body
chains: [ethereum]                # list — multi-chain incidents list all
protocols_directly_affected: [resolv]
protocols_indirectly_affected: [fluid]
vault_types_at_risk:              # which VaultDiligence VT classifications could face this pattern
  - VT-A                          # stablecoin issuer
  - VT-3a                         # synthetic stablecoin
classification: minting           # one of: oracle | minting | redemption | counterparty | depeg | governance | smart-contract | rwa-recourse
loss_estimate_usd: 50000000       # null if unknown; document confidence in body
loss_confidence: HIGH             # HIGH | MEDIUM | LOW
sources:
  - url: https://...
    type: FORMAL                  # post-mortem from project, regulator filing, etc
    retrieved: 2026-04-XX
  - url: https://...
    type: INFORMAL                # news article, Twitter thread
    retrieved: 2026-04-XX
---
```

### Body (required sections)

```markdown
## What happened

Two to four sentences. Mechanical description, no interpretation.
Example: "On 2026-03-XX, an attacker deposited $100,000 into Resolv and triggered the
mint of 80,000,000 USR. The bug was in the deposit-to-mint accounting; ratio checks
were absent at the contract level."

## Why it matters for diligence

Two to four sentences explaining WHICH part of a pre-allocation diligence pack
would have surfaced the risk pattern (not necessarily this specific exploit —
patterns generalise; specific exploits don't).

## Diligence signature

A structured list. For each item: what field, what state would have caught it,
what gap action.

- field_id: F-CTR-022 (mint authority)
  state_pre_incident: G2 (could not be independently verified at FORMAL or ON-CHAIN)
  gap_action: "Confirm mint authority is bound to a verified multisig or
  timelock with at least 24h delay. If absent: G2."
  notes: "The contract had a deposit-to-mint function with no ratio invariant.
  This was knowable from the verified contract on Etherscan but not flagged
  by the curators of vaults that accepted USR as collateral."

- field_id: F-FIN-018 (proof of reserves)
  state_pre_incident: G3 (no verifiable PoR feed)
  gap_action: "Verify a live, attestation-backed PoR feed exists. If only a
  static reserve report: G3 with action 'request live PoR feed'."

- field_id: ...

## Cross-vault recurrence

Has this pattern occurred before? List prior incident slugs that share the
same `classification`. Used by the salience scorer for `cross_vault_recurrence`.

- 2022-terra-collapse — same classification (depeg/minting), different mechanism
- 2025-xusd-depeg — same classification (depeg), different counterparty

## Lessons reference

If a graduated lesson in the durable lessons record was created in
response to this incident, link to its anchor:

- LESSONS#auto-2026-04-XX-mint-authority-on-chain-verification

## Notes

Free-form. Source-confidence caveats, conflicting accounts, ongoing
investigations, anything that doesn't fit above.
```

### What every entry MUST do

1. Cite at least one FORMAL source. INFORMAL-only entries are not registry-quality; they belong in a separate `knowledge/incidents/_pending/` triage folder.
2. Have at least one item in the Diligence Signature section. An incident with no field-level diligence implication doesn't earn its place.
3. Specify `vault_types_at_risk`. If the answer is "all vault types" this is also acceptable but should be justified in the body.
4. Specify `classification` exactly once from the controlled vocabulary. If a new classification is needed, add it to this schema doc first.

### What every entry MUST NOT do

1. Speculate about parties' intent. "The attacker was motivated by X" — not registry content.
2. Assign blame. "The curator should have known" — not registry content. VaultDiligence does not score third parties.
3. Predict future incidents. The diligence signature describes what evidence states *would have* applied, not what will happen next.
4. Reproduce copyrighted post-mortem text. Cite, don't quote at length.

## Schema versioning

Entries written under v44's schema are tagged `schema_version: 1` in frontmatter. If the schema evolves, increment the version and document migration rules. Old entries are not silently re-interpreted.

## Index format

`knowledge/incidents/_index.md` is one row per incident, ordered by date descending:

```markdown
# Incidents Registry

| Date | Slug | Title | Classification | VT at risk | Loss USD |
|------|------|-------|----------------|------------|----------|
| 2026-03-XX | 2026-03-resolv-mint | Resolv USR illegitimate mint | minting | VT-A, VT-3a | $50M |
| 2025-XX-XX | 2025-xusd-depeg | xUSD depeg / Stream Finance | depeg | VT-3a, VT-7 | (unknown) |
| 2022-05-09 | 2022-terra-collapse | Terra UST collapse | depeg | VT-A, VT-3a | $40B+ |
```

The index is regenerated by `scripts/validate-incidents.py --rebuild-index`, not edited by hand.

## How it gets used

- **A3 synthesis** loads incidents matching the current vault's `vault_type` via `scripts/load-incidents.py`, then for each entry checks whether the diligence signature's referenced fields are present in the current pack and at what state. Incidents whose signature fields are at G2 or G3 in the current pack are surfaced as `findings-live.md` triggers (severity: medium) — "this vault has a gap in field F-CTR-022, which is the same gap that surfaced in 2026-03-resolv-mint."
- **Plan mode** before D1/full-dd loads the same matched incidents and presents them to the operator: "this vault type has these prior failure patterns, are any of them load-bearing for this run."
- **`cross_vault_recurrence`** axis in salience scoring counts how many distinct incidents share the same classification as the current episodic entry's pattern.
- **Validation:** `scripts/validate-incidents.py` enforces the schema. `--rebuild-index` regenerates `_index.md`. `--check-coverage` reports field IDs referenced in incidents that don't exist in the registry (broken references).

## Versioning and growth

The registry grows when a new public incident occurs that has a clean diligence signature. Population is manual, not agentic — every entry is human-written from FORMAL post-mortems, then validated. The dream cycle does not write to this directory.

## Cross-references

- `.claude/agents/architecture.md` — A3 synthesis scope, which consumes this registry
- `.claude/commands/d1.md`, `.claude/commands/full-dd.md` — plan-mode preambles that consult this registry
- `scripts/validate-incidents.py`, `scripts/load-incidents.py` — the tooling
