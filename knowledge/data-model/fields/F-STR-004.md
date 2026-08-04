# F-STR-004

**Field ID**: F-STR-004
**Category**: Strategy Risk
**Sub-Category**: Lending — Oracle
**Field Name**: Liquidation-Oracle Price Source & Manipulation Surface
**What to Collect / Question to Answer**: For each lending market, which oracle drives BOTH borrow-capacity and the liquidation trigger, and what is its price-source type: a live market/spot price (manipulable by moving the underlying market), a TWAP, or a hardcoded / exchange-rate feed (does not move in a real depeg)? Is it a single-point dependency with no fallback? State both failure directions: (a) an upward price manipulation triggering wrongful liquidations, and (b) a hardcoded / stale feed that never triggers liquidation on a real depeg, letting a position accrue bad debt or borrow beyond intended LTV. Source: the market's oracle configuration read on-chain + oracle provider docs.
**Data Type**: Structured (oracle address + type per market; price-source class {spot / TWAP / hardcoded / NAV}; fallback present boolean; both failure directions described)
**Vault Types**: Strategy = lending
**Collection Tier**: T1
**Pillar(s)**: P3 (propose; secondary P4)
**Primary Source**: On-chain read of the market's oracle contract and its underlying source; oracle-provider documentation
**Fallback Source**: Protocol risk dashboard / audit-report oracle section (cross-ref F-ORC-008 last-update timestamp, F-ORC-010 bounds validation)
**Evidence Pathway**: Inspection-validatable — identify the oracle wired to the market's liquidation logic, classify its price-source, and confirm whether a fallback exists; then reason through both manipulation directions. A spot-priced thin market is manipulable up (wrongful liquidation); a hardcoded feed is "safe" until the pair decorrelates, then fails to liquidate at all.
**Institutional Standard**: What a well-run vault evidences: the liquidation oracle per market is named, its price-source class is stated, fallback presence is recorded, and both failure directions are described against the actual collateral — distinguishing a genuinely correlated pair (where a hardcoded feed is defensible) from a decorrelation-prone pair (where it is a latent bad-debt source).
**Status**: Gap with action
**If Not Found — Gap Action**: Read the oracle wired to the market and record its type + fallback (E). If the source class is inferable but the manipulation analysis is not evidenced, mark E(P). If the oracle cannot be enumerated on-chain and is undisclosed, classify G2 and name the market. Where a hardcoded/1:1 feed backs a decorrelation-prone pair, record that fact for the allocator; do not score it.
**Source / Precedent**: Compound DAI oracle event (26 Nov 2020): Coinbase-sourced DAI price spiked to ~$1.30, driving ~$89M of liquidations (Decrypt, comp.xyz forum). Mango Markets (Oct 2022): oracle price manipulation, ~$114M. Morpho hardcoded-oracle risk: hardcoded/NAV feeds "don't adjust, making it impossible to liquidate," letting borrowers exploit stale valuation (`docs.morpho.org/learn/resources/risks/`; MixBytes Morpho Blue analysis). Extends F-ORC-012 (VT-7-scoped NAV→liquidation link).
**Criterion ID(s)**: propose 3.1 / 3.2 / 4.3 · RF08 (leave for ratification)
