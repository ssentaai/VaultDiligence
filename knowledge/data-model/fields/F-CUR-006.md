# F-CUR-006

**Field ID**: F-CUR-006
**Category**: Entity
**Sub-Category**: Curator
**Field Name**: Curator Supply Cap Utilisation
**What to Collect / Question to Answer**: Current allocation vs supply cap per market within vault (%)
**Data Type**: Percent
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7,VT-8)
**Collection Tier**: T1
**Primary Source**: Morpho API / protocol dashboard / on-chain query
**Fallback Source**: DefiLlama vault page
**Pillar(s)**: P4,P9
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Near-cap allocations restrict future inflows and may compress APY. Used by Gauntlet to assess scalability.
**Criterion ID(s)**: 4.5 / 9.1