# F-COL-005

**Field ID**: F-COL-005
**Category**: Financial
**Sub-Category**: Collateral Contagion
**Field Name**: Vault Exposure Per Collateral Token ($)
**What to Collect / Question to Answer**: Dollar exposure to each accepted collateral token. Source: on-chain vault composition data.
**Data Type**: Currency ($M, per token)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7)
**Collection Tier**: T1
**Primary Source**: On-chain vault composition / Morpho markets API / protocol dashboard
**Fallback Source**: DefiLlama vault breakdown
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: N
**D4**: N
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Query on-chain vault composition. If not queryable: request from curator.
**Criterion ID(s)**: 4.5