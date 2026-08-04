# VT-N -> Archetype Tuple — Decomposition Map

**Status:** Phase 1 (non-breaking) reference. Ratified design of record:
`an internal analysis` §5 (v2, ratified 2026-07-09).
Dimension vocabulary: `dimensions.md`.

This file is the **single source of truth** that the Phase 2 field migration will
mechanically apply: each existing `VT-N` reference decomposes into a set of dimension
predicates. It is not consumed by anything yet.

> **VT-N remains the LIVE routing key.** Through Phase 2, every field "Vault Types:" line
> and every pillar VT-gate still routes on VT-N exactly as today. This map is the key the
> Phase 2 migration applies (behind the "a tokenized CLO fund fires identically before/after" validation
> gate); VT-N is retired only in Phase 3. Nothing here changes current routing.

Dimensions in the table below, in order: **Exposure / Strategy / Management / Structure /
Seniority / Liquidity** (+ flags/composition in Note). "varies" = the VT captured only
*other* axes, so this dimension is vault-specific and resolved per vault at migration.

| Existing VT | What it captured | Exposure / Strategy / Management / Structure / Seniority / Liquidity | Note |
|---|---|---|---|
| **VT-1** DeFi Lending | structure + mgmt | crypto-native / **lending** / protocol-native / multi-asset-pool / n-a / daily | strategy now explicit |
| **VT-2** Delta-Neutral | structure | synthetic+crypto / **basis/funding-trade** / algorithmic / delta-neutral-synthetic / n-a / daily-epoch | |
| **VT-3** Tokenised RWA/Credit | exposure ONLY | (private-credit or structured-credit) / passive-carry / delegated-offchain-IM / varies / varies / varies | single-axis proof (exposure only) |
| **VT-3a** Tokenised Fund | mgmt ONLY | varies / varies / **delegated-offchain-IM** / varies / varies / varies | single-axis proof (management only) |
| **VT-4** Structured Finance/Tranche | structure ONLY | often structured-credit / passive-carry / varies / **tranched** / varies / varies | single-axis proof (structure only) |
| **VT-5** Liquid Staking | exposure + mgmt | crypto-native / **staking** / protocol-native / single-asset / n-a / daily-epoch | |
| **VT-6** Yield Aggregator | structure + mgmt | crypto-native / varies-strategy / algorithmic or delegated / multi-asset-pool / n-a / daily | |
| **VT-7** Composable/Leveraged | structure + composition | crypto-native / varies / algorithmic or delegated / leveraged/looped / n-a / varies + **composes: &lt;sub-vault&gt;** | composition = downward pointer |
| **VT-8** TradFi-Primary/Wrapped | exposure + venue | (equities or corporate/sovereign-fixed-income) / passive-carry or delegated / passive-hold or delegated / single or pool / varies / daily + **venue = tradfi-primary** | |
| **VT-A** Agent Treasury | NOT a vault property | remove — `caller_type=agent` overlay | not an archetype (moves to a caller overlay) |
| **VT-9** (orphan, F-FIN-050) | undefined | resolve to **Seniority = junior/first-loss** (NOT a structure value) | v2 fix: it was a seniority value |

## v2 changes to the decomposition (vs v1)

1. **Strategy is now an explicit predicate on every row** — v1 folded strategy into
   management, so lending / staking / basis-trade / options had no home.
2. **VT-9 resolves to a *seniority* value (junior/first-loss), not a structure value** —
   first-loss is about where you sit in the waterfall (seniority), corrected from v1.

## How Phase 2 uses this map

Each field's `Vault Types: VT-N, ...` line becomes a predicate over the dimensions by
substituting each VT-N with its row above and OR-ing. Illustrative (Phase 2, not applied
here):

- `F-ENT-075` (service-provider agreements) scoped VT-3/3a/4/8 -> `Management = delegated-offchain-IM`.
- `F-FIN-050` (first-loss capital) scoped VT-3a/VT-8/VT-9 -> `Seniority = junior/first-loss` (resolving the VT-9 orphan).
- `F-HED-001..006` (delta-neutral hedge) scoped VT-2/VT-4 -> `Structure = delta-neutral-synthetic` OR `Strategy = basis/funding-trade`.

Pillar VT-gates re-express the same way in Phase 3 (e.g. P18 -> `Management =
delegated-offchain-IM`; P5 -> `Structure = delta-neutral-synthetic` OR `Strategy =
basis/funding-trade`; P6 -> `Exposure ∈ {structured-credit, private-credit, corporate-FI,
real-estate, infrastructure}`). None of that happens in Phase 1.
