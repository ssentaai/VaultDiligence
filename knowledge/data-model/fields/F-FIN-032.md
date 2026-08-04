# F-FIN-032

**Field ID**: F-FIN-032
**Category**: Financial
**Sub-Category**: Collateral
**Field Name**: Current Collateralisation Ratio
**What to Collect / Question to Answer**: Current CR at time of assessment
**Data Type**: Percent
**Vault Types**: Strategy=lending OR Structure=delta-neutral-synthetic OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-2,VT-7,VT-8)
**Collection Tier**: T1
**Primary Source**: On-chain: getUserAccountData() / vault health factor / protocol dashboard
**Fallback Source**: Chaos Labs dashboard
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**Required?**: C
**If Not Found — Gap Action**: Declining CR = approaching liquidation. Distance from liquidation threshold = key signal.
**Criterion ID(s)**: 4.2