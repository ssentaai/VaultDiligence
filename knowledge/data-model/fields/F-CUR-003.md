# F-CUR-003

**Field ID**: F-CUR-003
**Category**: Entity
**Sub-Category**: Curator
**Field Name**: Curator Other Active Vaults
**What to Collect / Question to Answer**: List of other vaults this curator currently manages — names and TVL
**Data Type**: Text
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7,VT-8)
**Collection Tier**: T3
**Primary Source**: Morpho vaultbook: vaultbook.gauntlet.xyz / protocol docs
**Fallback Source**: DefiLlama protocol page
**Pillar(s)**: P8
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Concentration risk: curator managing too many vaults relative to team size. Cross-contamination risk.
**Criterion ID(s)**: 8.1
**Registered Sources (Fix 70)**: expert-curator-forum
