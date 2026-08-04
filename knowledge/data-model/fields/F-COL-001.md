# F-COL-001

**Field ID**: F-COL-001
**Category**: Financial
**Sub-Category**: Collateral Contagion
**Field Name**: Collateral Token List — Complete
**What to Collect / Question to Answer**: Complete list of all collateral tokens accepted by this vault. Source: on-chain collateral whitelist or curator documentation.
**Data Type**: Text (list)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7)
**Collection Tier**: T1
**Primary Source**: On-chain collateral whitelist (Etherscan) / curator documentation / Morpho markets API
**Fallback Source**: Protocol documentation
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: N
**D4**: N
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Query on-chain collateral whitelist. If not verifiable: request from curator. Every accepted token must be listed.
**Criterion ID(s)**: 4.1 / 4.5
**Red Flag ID(s)**: RF12