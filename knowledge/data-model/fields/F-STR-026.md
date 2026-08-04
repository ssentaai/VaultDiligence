# F-STR-026

**Field ID**: F-STR-026
**Category**: Strategy Risk
**Sub-Category**: LP/AMM — Range Management
**Field Name**: Concentrated-Liquidity Range Policy, In-Range Time & Rebalance Churn
**What to Collect / Question to Answer**: For a concentrated-liquidity position: what is the range-setting policy (fixed width, volatility-scaled, oracle-following), what share of the live window did price actually sit inside the range (in-range time), how often is the position rebalanced, and what IL and gas cost has rebalancing realised? Who decides and executes the rebalance (automated contract vs curator/manual)?
**Data Type**: Structured (range policy, in-range time %, rebalance frequency, realised rebalance IL + gas, execution actor)
**Vault Types**: Strategy = LP/AMM-provision (narrower predicate: concentrated-liquidity / CLMM positions; N/A for full-range v2-style pools — state which)
**Collection Tier**: T2 (on-chain position/tick history) + T3 (policy disclosure)
**Pillar(s)**: P6 (Strategy Integrity) primary; P8 (Operational) for the execution/automation angle — propose; operator confirms
**Primary Source**: On-chain position tick bounds and mint/burn history vs realised price (in-range time, rebalance count); operator/curator strategy documentation for the range policy
**Fallback Source**: DEX position-manager dashboard; governance-forum strategy write-up
**Evidence Pathway**: Inspection-validatable — tick bounds, price path, and rebalance transactions are on-chain; in-range time and rebalance churn are measured directly, and the stated policy is checked against the observed behaviour.
**Institutional Standard**: A well-run CLMM vault documents its range policy, and its observed in-range time and rebalance cadence are consistent with that policy; out-of-range dormancy (zero fees, full one-sided conversion) and rebalance churn (realised IL + gas) are both recorded. An undocumented or discretionary range policy with no observable rebalance discipline is the gap.
**Status**: Gap with action
**If Not Found — Gap Action**: If tick history and policy are both available, record in-range time, cadence, realised rebalance IL/gas and the execution actor, and classify E. If behaviour is observable but no policy is documented, classify E(P) and state the policy gap. If neither is available, classify G3 and require the operator to publish the range policy. Mark N/A with reason for full-range positions.
**Source / Precedent**: Uniswap v3 Core whitepaper (Adams et al., 2021) — concentrated liquidity earns fees only in-range and amplifies IL as ranges narrow; "Backtesting Framework for Concentrated Liquidity Market Makers on Uniswap V3", arXiv:2410.09983 (supporting, on range/rebalance trade-offs). Distinct from F-HED-005 (delta-hedge rebalancing on a perp).
**Criterion ID(s)**: propose at ratification
