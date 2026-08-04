# F-FIN-033

**Field ID**: F-FIN-033
**Category**: Financial
**Sub-Category**: Collateral
**Field Name**: Liquidation Threshold
**What to Collect / Question to Answer**: CR at which liquidation is triggered (on-chain confirmed)
**Data Type**: Percent
**Vault Types**: Strategy=lending OR Structure=delta-neutral-synthetic OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-2,VT-7,VT-8)
**Collection Tier**: T1
**Primary Source**: On-chain: getReserveConfigurationData(assetAddress).liquidationThreshold
**Fallback Source**: Protocol docs
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**Required?**: C
**If Not Found — Gap Action**: Must be on-chain verified. Operator-stated threshold is not sufficient. Use contract call.
**Criterion ID(s)**: 4.2 / 4.3