# F-COL-006

**Field ID**: F-COL-006
**Category**: Financial
**Sub-Category**: Collateral Contagion
**Field Name**: Vault Exposure Per Collateral Token (% TVL)
**What to Collect / Question to Answer**: Percentage of TVL exposed to each collateral token. Concentration >30% in single collateral = flag.
**Data Type**: Percent (per token)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7)
**Collection Tier**: T1
**Primary Source**: Calculated from F-COL-005 / TVL
**Fallback Source**: Protocol dashboard
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: N
**D4**: N
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Compute from F-COL-005 divided by total TVL. Flag any single token >30%.
**Criterion ID(s)**: 4.5
**Red Flag ID(s)**: RF12