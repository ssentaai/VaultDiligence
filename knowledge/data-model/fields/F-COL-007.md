# F-COL-007

**Field ID**: F-COL-007
**Category**: Financial
**Sub-Category**: Collateral Contagion
**Field Name**: Blast Radius Estimate — Per Collateral Depeg
**What to Collect / Question to Answer**: If this collateral token depegged to zero: estimated protocol loss, cascade liquidation risk, and cross-protocol contagion. Resolv USR: 15 Morpho vaults exposed, Fluid $10M+ bad debt.
**Data Type**: Text (per token)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7)
**Collection Tier**: T3
**Primary Source**: Assessor stress calculation / curator disclosure
**Fallback Source**: Historical contagion case studies (Resolv/Stream/Usual precedents)
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: N
**D4**: N
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Model: if collateral X depegs to 0, what is vault loss? What protocols are downstream? Request curator stress test.
**Criterion ID(s)**: 4.5 / SC1
**Red Flag ID(s)**: RF35