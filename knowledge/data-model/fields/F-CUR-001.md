# F-CUR-001

**Field ID**: F-CUR-001
**Category**: Entity
**Sub-Category**: Curator
**Field Name**: Curator Name
**What to Collect / Question to Answer**: Named individual or entity responsible for vault parameter decisions
**Data Type**: Text
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7,VT-8)
**Collection Tier**: T3
**Primary Source**: Vault contract: owner() / operator docs / Morpho vaultbook
**Fallback Source**: Protocol governance forum
**Pillar(s)**: P8
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: C
**If Not Found — Gap Action**: Essential for delegated risk management vaults. Anonymous curator = flag.
**Criterion ID(s)**: 8.1