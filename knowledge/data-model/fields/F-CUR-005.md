# F-CUR-005

**Field ID**: F-CUR-005
**Category**: Entity
**Sub-Category**: Curator
**Field Name**: Curator Fee Structure
**What to Collect / Question to Answer**: Performance fee %, management fee %, and split arrangements with distribution partners
**Data Type**: Text
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7,VT-8)
**Collection Tier**: T3
**Primary Source**: Vault contract: feeRecipient / feeBps / operator docs
**Fallback Source**: Governance forum
**Pillar(s)**: P6,P8
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Higher fee share = curator incentivised to chase yield at depositor expense. Flag if >20% performance fee.
**Criterion ID(s)**: 6.5