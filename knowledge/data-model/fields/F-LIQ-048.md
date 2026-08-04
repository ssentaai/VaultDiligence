# F-LIQ-048

**Field ID**: F-LIQ-048
**Category**: Liquidity
**Sub-Category**: Redemption Stress
**Field Name**: Host-Pool Utilisation & Illiquidity Threshold
**What to Collect / Question to Answer**: Where the vault token sits inside a host lending pool, at what utilisation level does the pool become illiquid for withdrawals, and how fast has comparable host-pool capacity been exhausted under stress?
**Data Type**: Structured (host pool named, current utilisation, illiquidity-threshold utilisation, time-to-exhaustion estimate)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1, VT-6, VT-7)
**Collection Tier**: T2
**Pillar(s)**: P9
**Primary Source**: On-chain host-pool state (utilisation rate, available liquidity, withdrawal-queue state read from the lending-pool contract)
**Fallback Source**: Host-protocol risk dashboard reporting utilisation and available withdrawal liquidity
**Evidence Pathway**: Inspection-validatable: read the host lending pool's utilisation and available-liquidity state on-chain and identify the utilisation level at which withdrawals can no longer clear; full utilisation freezes even depositors with no exposure to the failing asset.
**Institutional Standard**: The host pool is named, its current and illiquidity-threshold utilisation are stated, and the realistic time for available withdrawal capacity to be exhausted under stress is estimated. A host pool that reaches full utilisation freezes all depositors, including those with no exposure to the asset that triggered the run.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the host pool's utilisation and available liquidity on-chain, state the utilisation level at which withdrawals cease to clear, and estimate the time-to-exhaustion under a stressed outflow. Cross-reference SC6. If the vault is not embedded in a host pool, mark N/A and state why. If pool state is not readable and not disclosed, classify G2 and name the pool.
**Source / Precedent**: Buzko Krasnov legal analysis, 27 Apr 2026: Kelp DAO contagion into Aave on 18 Apr 2026 saw host-pool utilisation reach full with $5.4B withdrawn in hours, freezing ETH/USDC depositors with no rsETH exposure.
**Criterion ID(s)**: 9.4, RF26, SC6
**Registered Sources (Fix 70)**: aave-protocol-data, defillama-lendborrow, dune-custom-queries, morpho-blue-api, thegraph-subgraph
