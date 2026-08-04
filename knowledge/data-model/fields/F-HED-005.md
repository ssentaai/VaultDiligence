# F-HED-005

**Field ID**: F-HED-005
**Category**: Financial
**Sub-Category**: Hedge
**Field Name**: Delta Rebalancing — Automation Confirmation
**What to Collect / Question to Answer**: Is delta rebalancing automated or manual? What is the tolerance band before rebalancing triggers? What is execution latency?
**Data Type**: Text
**Vault Types**: Structure=delta-neutral-synthetic OR Structure=tranched  (derived from VT-N; original "Vault Types" value: VT-2,VT-4)
**Collection Tier**: T1
**Primary Source**: On-chain event logs via Etherscan — read rebalancing event frequency from vault contract
**Fallback Source**: Audit report — rebalancing logic and delta tolerance should be in audit scope
**Pillar(s)**: P5
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Manual-only rebalancing = flag. Delta tolerance >10% = flag. High-volatility periods require automated sub-1-hour rebalancing.
**Criterion ID(s)**: 5.5