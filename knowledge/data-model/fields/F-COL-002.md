# F-COL-002

**Field ID**: F-COL-002
**Category**: Financial
**Sub-Category**: Collateral Contagion
**Field Name**: Collateral Token Issuer — Per Token
**What to Collect / Question to Answer**: For each accepted collateral token: named issuer/protocol, jurisdiction, regulatory status.
**Data Type**: Text (per token)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7)
**Collection Tier**: T3
**Primary Source**: Token issuer documentation / protocol website / regulatory register
**Fallback Source**: CoinGecko token info
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: N
**D4**: N
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Map each token to its issuer. Anonymous issuer = flag. Research issuer regulatory status per jurisdiction.
**Criterion ID(s)**: 4.1