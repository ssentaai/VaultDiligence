# F-FIN-084

**Field ID**: F-FIN-084
**Category**: Financial
**Sub-Category**: Holder Concentration
**Field Name**: Holder Concentration Index — HHI / Gini / Top-N with Threshold and Trend
**What to Collect / Question to Answer**: What is the holder-concentration profile measured as a Herfindahl-Hirschman Index, Gini coefficient, and top-N holder shares, how does each compare to a stated reference threshold, and what is the trajectory of concentration over the observation window?
**Data Type**: Numeric set (HHI, Gini, top-1/top-N shares) + reference threshold + trend direction
**Vault Types**: ALL
**Collection Tier**: T2
**Pillar(s)**: P9
**Primary Source**: On-chain top-holder analysis across all deployment chains (block explorer holder lists / Dune)
**Fallback Source**: Wallet-labelling service (Nansen) to attribute holders, plus operator investor-relations disclosure for off-chain holders
**Evidence Pathway**: Inspection-validatable: read the token holder distribution on-chain across every deployment chain, compute HHI, Gini, and top-N shares from the holdings, and chart the index over the observation window against the stated reference threshold.
**Institutional Standard**: Concentration is quantified as HHI, Gini, and top-N shares across all chains, each compared to an explicit reference threshold and trended over time; concentration is read against demonstrated exit capacity rather than treated as a standalone critical condition, so high concentration with proven large-redemption execution is surfaced as a monitored condition, not a verdict.
**Status**: Gap with action
**If Not Found — Gap Action**: Compute HHI, Gini, and top-N from on-chain holder data across all chains and state the reference threshold and trend; if holders are off-chain or unattributable, classify the unattributed share as G2 naming the registry or investor-relations disclosure required to attribute it.
**Source / Precedent**: a synthetic-dollar and CLO-fund diligence pack, 5-7 Jun 2026: holder HHI 49.9 against a reference of 25; top-1 holder 63.2 ($250M a seed/anchor allocator on Avalanche); combined 94.7; Gini 0.7878; HHI peaked at 60.5 in Dec 2025 — surfaced as MONITOR precisely because a $318.6M single-day redemption at five basis points proved exit capacity.
**Criterion ID(s)**: 9.7, RF28
