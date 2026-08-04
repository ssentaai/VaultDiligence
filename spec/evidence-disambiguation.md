# Evidence Disambiguation Rules (v42)

When two agents (or two writes from the same agent) produce different evidence objects for the same field, the disambiguation rules in `scripts/validate-evidence.py` decide what gets recorded. The rules are deterministic, the same inputs always produce the same outcome, and every decision leaves an audit trail in `write_history`.

## Rules

1. **Source-tier wins.** ON-CHAIN > FORMAL > EXPERT > INFORMAL.
2. **Within the same source-tier, recency wins.** Newer `retrieved_at` beats older.
3. **If neither rule produces a winner**, state is forced to `I`. Both sources are retained.

The rules are applied by `disambiguate(existing, incoming)` and consumed by `write_field()`. A user (or agent) calling `write_field()` does not need to know about the rules — they call write, and the resolver runs.

## Worked examples

### Example 1: source-tier resolves cleanly

A1 writes F-FIN-010 from a Substack post (source_type=INFORMAL, value="$847M TVL").
A2 writes F-FIN-010 from the operator's Gitbook (source_type=FORMAL, value="$851M TVL").

```
Rule 1 fires: FORMAL > INFORMAL.
Decision: incoming_wins.
Register entry: A2's value with state=E (or whatever state A2 wrote).
write_history records:
  [
    { agent_id: A1, action: created, ... },
    { agent_id: A2, action: overwritten-by-tier,
      rationale: "incoming source_type=FORMAL outranks existing INFORMAL",
      superseded_source: { uri: substack.com/..., value: $847M, source_type: INFORMAL } }
  ]
```

### Example 2: same tier, recency resolves

A1 writes F-CTR-008 from on-chain at 10:14 UTC (value=multisig 0xAAA).
A1 re-runs and writes F-CTR-008 from on-chain at 11:02 UTC after a governance vote (value=multisig 0xBBB).

```
Rule 1 ties: both ON-CHAIN.
Rule 2 fires: 11:02 > 10:14.
Decision: incoming_wins.
write_history records both with action=overwritten-by-recency.
```

### Example 3: neither rule resolves — state forced to I

A1 writes F-ENT-041 from on-chain governance (source_type=ON-CHAIN, value="Steakhouse Labs", retrieved_at=10:14).
A2 writes F-ENT-041 from a different on-chain registry (source_type=ON-CHAIN, value="Steakhouse Financial", retrieved_at=10:14).

Same tier, same retrieved_at. Cannot disambiguate.

```
Rule 1 ties.
Rule 2 ties.
Rule 3 fires: state forced to I.
Register entry:
  field_id: F-ENT-041
  value: "CONFLICT: Steakhouse Labs vs Steakhouse Financial"
  state: I
  source_uri: "CONFLICT:https://etherscan.io/...|https://gnosisscan.io/..."
  conflict: {
    source_a: { agent_id: A1, source_type: ON-CHAIN, ... },
    source_b: { agent_id: A2, source_type: ON-CHAIN, ... },
    resolution_action: "Re-query against the highest-authority available source (ON-CHAIN tier). Resolve before pack closes."
  }
```

A3 sees `state=I` at synthesis time and surfaces it as a gap requiring manual resolution. The pack does not close with unresolved I states.

### Example 4: existing wins, incoming discarded

A2 writes F-SEC-009 from a Gitbook (source_type=FORMAL).
A1 then attempts to write F-SEC-009 from a Substack analysis (source_type=INFORMAL).

```
Rule 1 fires: FORMAL > INFORMAL.
Decision: existing_wins.
Register entry: unchanged (A2's FORMAL evidence stays).
write_history appends:
  { agent_id: A1, action: inherited-incoming-discarded,
    rationale: "existing source_type=FORMAL outranks incoming INFORMAL",
    superseded_source: { uri: substack.com/..., source_type: INFORMAL } }
```

The discarded write is logged but not silently dropped — auditing later can see A1 attempted to overwrite with weaker evidence.

## What the rules do NOT do

- **They do not silently resolve genuine disagreements.** Two ON-CHAIN sources disagreeing about the same value is not a coding problem. It's an investigation problem and stays as state=I.

- **They do not override the no-inference rule.** A higher-tier source beats a lower-tier source on which is *recorded*, but the recorded evidence still has to pass `validate()` — no INFORMAL source can produce state=E regardless of who writes it.

- **They do not ignore confidence.** Confidence is a separate dimension; an ON-CHAIN read with confidence=LOW is still ON-CHAIN-tier, but the evidence object will have already been downgraded from E to E(P) by the existing validator before disambiguation runs.

- **They do not retroactively rewrite history.** When A6 verification downgrades a field, that's a `downgraded-state` action on `write_history`, not a re-application of disambiguation. The disambiguation rules only fire at first-write conflict time.

## Invariants

- The same `(existing, incoming)` pair always produces the same `(decision, winner, rationale)`.
- Every disambiguation decision is recorded in `write_history` on the resulting evidence object.
- Rule 3 (force I) cannot be silenced. If neither tier nor recency resolves, state is I.
- No write succeeds without a `validate()` pass first. Disambiguation runs *after* validation, never instead of it.

## Cross-references

- `scripts/validate-evidence.py` — implementation: `disambiguate()`, `write_field()`, `_stamp_write_history()`
- `spec/evidence-object-schema.md` — `write_history` and `agent_id` field definitions
- `spec/findings-live-schema.md` — A1↔A2 trigger protocol that tries to prevent disambiguation cases by routing verification before conflict
