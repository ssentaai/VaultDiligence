# F-FIN-006

**Field ID**: F-FIN-006
**Category**: Financial
**Sub-Category**: Vault Metrics
**Field Name**: Utilisation Rate (current)
**What to Collect / Question to Answer**: % of deposited capital currently deployed vs idle
**Data Type**: Percent
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7)
**Collection Tier**: T1
**Primary Source**: Protocol dashboard / vault.totalAssets() vs totalBorrows() / Morpho API
**Pillar(s)**: P9
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**Required?**: C
**If Not Found — Gap Action**: High utilisation (>90%) = low withdrawable liquidity. Near 100% = exit trap. Critical field.
**Criterion ID(s)**: 9.1 / 9.4