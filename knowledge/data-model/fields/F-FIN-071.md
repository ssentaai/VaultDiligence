# F-FIN-071

**Field ID**: F-FIN-071
**Category**: Financial
**Sub-Category**: Yield
**Field Name**: Net Realised Yield — All-In Single Number
**What to Collect / Question to Answer**: Single net yield figure: Gross APY minus all costs. Costs: management fee + performance fee + protocol fee + custody fee + execution/hedging cost + gas (annualised) + slippage estimate. State as: Gross X% minus Y bps = Net Z%. Must appear in Executive Summary. Use conservative estimate where any component unavailable.
**Data Type**: Percent
**Vault Types**: ALL
**Collection Tier**: T1/T3
**Primary Source**: Operator fee schedule + on-chain gas data (Etherscan average) + DEX depth data (DefiLlama/DexScreener)
**Fallback Source**: Comparable vault fee benchmarks (vaults.fyi / Keyrock onchain asset management report)
**Pillar(s)**: P6
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Compute from operator fee schedule + on-chain gas average. If any component undisclosed: use conservative estimate and state assumption explicitly. Gap action: request complete fee schedule from operator CFO.
**Criterion ID(s)**: 6.6
**v54 Refinement (gap audit 2026-06-12)**: Distinguish the headline / advertised yield from the pass-through yield actually reaching depositors after every intermediary layer takes its cut; name each layer and its take. Source: gap audit 2026-06-12. Cross-ref F-FIN-086.
