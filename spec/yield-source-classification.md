# Yield Source Classification — Threshold Specification

**Status:** v51, applies to F-FIN-077.
**Origin:** 2026-05-06 review of W19 2026 Morpho USDC vault snapshot. The article identified that vaults with similar headline APR can have completely different risk profiles depending on yield source decomposition.
**Companion field:** F-FIN-077 (Yield Source Classification — Single-Value Rollup).

## Why this exists

F-FIN-016 (yield source breakdown) reports percentages — % organic, % token incentives, % other. F-FIN-075 (single underlying concentration) reports the largest single-name share of yield. Both are useful inputs but neither produces a single-value summary an institutional reader can scan.

F-FIN-077 is that summary. This spec defines the rules that map (F-FIN-016, F-FIN-075) → F-FIN-077.

## Classification rules

The rules are evaluated in order. The first rule that matches sets F-FIN-077.

### Rule 1 — `concentrated`

If F-FIN-075 reports >70% of yield from a single named issuer or instrument, F-FIN-077 = `concentrated`.

Rationale: regardless of whether that single source is organic or incentive-driven, the structural risk is the single-name dependency. Steakhouse Gauntlet Prime USDC at 94-97% cbBTC/USDC is the canonical example — a single collateral asset's failure propagates directly to depositor outcomes.

### Rule 2 — `incentive_driven`

If F-FIN-016's "% token incentives" component is >40%, F-FIN-077 = `incentive_driven`.

Rationale: when more than 40% of headline yield is incentive-driven, the yield is structurally subject to emission-schedule decay or termination. The Morpho article's UltraYield example (>60% concentration in a single bridge asset alongside emissions) is the canonical pattern.

### Rule 3 — `sustainable`

If F-FIN-016's "% organic (real revenue)" is >75% AND F-FIN-075 is <50%, F-FIN-077 = `sustainable`.

Rationale: yield is predominantly from real economic activity (RWA, lending demand, fees) AND no single source dominates. Smokehouse USDC (~5.5% organic from RWAs and diversified lending) is the canonical example.

### Rule 4 — `mixed`

If none of rules 1-3 match, F-FIN-077 = `mixed`.

Rationale: the vault has a partial mix of yield sources without one source dominating to the threshold of `sustainable`, `concentrated`, or `incentive_driven`. The classification surfaces that the structural risk is plural rather than mono-source. The verdict block (spec/verdict-block-spec.md) should explicitly enumerate the components.

## Edge cases

### Multi-source incentive yield

A vault with 30% yield from Token A emissions + 25% from Token B emissions = 55% total incentive-driven, hits Rule 2 even though no single emission source is dominant. Classification = `incentive_driven`. Correct: aggregate incentive dependence is what matters for structural decay.

### Concentrated organic yield

A vault with 100% yield from a single RWA issuer's tokenized treasuries. F-FIN-075 = 100% > 70% → Rule 1 fires. Classification = `concentrated`, not `sustainable`. Correct: even fully organic yield concentrated in one issuer carries the issuer's solvency risk.

### Concentrated and incentive-driven simultaneously

A vault with 80% yield from a single source where that source is itself driven by token emissions. Rule 1 fires first → classification = `concentrated`. The verdict block must call out the compounding (concentrated AND incentive-driven). The single classification field can only carry one value; the rationale and verdict carry the secondary signal.

### Threshold edge

A vault with exactly 70% single-name concentration is NOT `concentrated` (rule says >70%). Round-up does not apply. The threshold is a hard inequality.

This is deliberate. Edge cases (69%, 71%) cluster around the threshold; the verdict block should explicitly state the % rather than rely on the binary classification when the value is within ±2 percentage points of the threshold.

## What this classification is NOT

- **Not a risk score.** A `sustainable` classification does not mean low risk. RWA-backed yield can carry counterparty risk, regulatory risk, off-chain custody risk. The classification surfaces yield-source structure, not aggregate risk.
- **Not a recommendation.** No buy/avoid signal attaches to any classification. An institutional allocator might prefer `concentrated` exposure (high conviction in the single source) over `sustainable` (less exposure to anything specific).
- **Not predictive.** A `sustainable` classification today says nothing about whether the vault will remain sustainable. A vault can shift between classifications across diligence cycles. Pack lifecycle (Fix 73) handles versioning.
- **Not a substitute for the underlying fields.** F-FIN-016 and F-FIN-075 must still be populated and reported. F-FIN-077 is the rollup, not a replacement.

## Updating the rules

These thresholds are first-cut. After three real D1s with v51 in production, review the threshold values against operator judgment. If a vault that operators would call `concentrated` in conversation gets classified as `mixed` by these rules (or vice versa), the thresholds need adjustment.

A future fix (call it Fix 84-tune) re-examines threshold values with empirical data. Until that data exists, the thresholds above are the working version.

## Cross-references

- `knowledge/data-model/fields/F-FIN-016.md` — yield source breakdown (input)
- `knowledge/data-model/fields/F-FIN-075.md` — single underlying concentration (input)
- `knowledge/data-model/fields/F-FIN-076.md` — secondary yield floor (related, not input)
- `knowledge/data-model/fields/F-FIN-077.md` — the field this spec defines
- `spec/verdict-block-spec.md` (Fix 86) — where this classification surfaces in reports
- W19 2026 Morpho USDC vault snapshot — original taxonomy source
