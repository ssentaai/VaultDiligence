# F-STR-023

**Field ID**: F-STR-023
**Category**: Strategy Risk
**Sub-Category**: LP/AMM — Impermanent Loss
**Field Name**: Impermanent / Divergence Loss vs HODL Benchmark
**What to Collect / Question to Answer**: Over the vault's live period, what is the realised divergence loss of the LP position measured against a HODL benchmark (holding the same two tokens in the deposit ratio unchanged) — stated as a figure with the observation window, the price-divergence range that produced it, and the data source? For a concentrated-liquidity position, state IL under the actual range width, not the full-range v2 approximation.
**Data Type**: Percentage (LP value / HODL value − 1) + observation window + source
**Vault Types**: Strategy = LP/AMM-provision
**Collection Tier**: T2 (on-chain position history + reference price series)
**Pillar(s)**: P6 (Credit & Yield Sustainability / Family B: Strategy Integrity) — propose; operator confirms whether a dedicated LP sub-pillar is preferred
**Primary Source**: On-chain LP-position history (pool contract mint/burn/collect events, position NAV) reconstructed against a reference price series; DEX analytics (e.g. a pool-level IL/PnL dashboard) where independently reproducible
**Fallback Source**: Operator disclosure of realised IL with stated methodology and window
**Evidence Pathway**: Inspection-validatable — reconstruct the LP position value and the HODL-equivalent value across the same window from on-chain state and a reference price feed, and take the difference. The result is a measured historical figure, not a projection.
**Institutional Standard**: A well-run vault records realised IL against a stated HODL benchmark over its live window, alongside the fee income earned in the same window (see F-STR-025), so the two can be read together. Recording IL in isolation, or only as an unrealised "impermanent" figure, is the gap.
**Status**: Gap with action
**If Not Found — Gap Action**: If on-chain position history and a reference price series are both available, compute realised IL and classify E. If only headline share-price return is disclosed with no HODL decomposition, classify E(P) and state the decomposition is missing. If position history is not reconstructable and the operator discloses nothing, classify G3 (the operator must publish an IL series). N/A only if the vault provides single-sided liquidity with no divergence exposure — state why.
**Source / Precedent**: Constant-function AMM impermanent-loss literature; "Impermanent Loss in Uniswap v3", arXiv:2111.09192 (2021); Uniswap v3 Core whitepaper (Adams, Zinsmeister, Salem, Keefer, Robinson, 2021) on the amplified IL of concentrated ranges.
**Criterion ID(s)**: propose at ratification (adjacent to 6.4 performance / drawdown)
