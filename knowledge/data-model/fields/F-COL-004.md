# F-COL-004

**Field ID**: F-COL-004
**Category**: Financial
**Sub-Category**: Collateral Contagion
**Field Name**: Collateral Historical Depeg Events
**What to Collect / Question to Answer**: For each accepted collateral: any historical depeg events? Date, magnitude, duration, recovery. Source: on-chain price data.
**Data Type**: Text (per token)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7)
**Collection Tier**: T1
**Primary Source**: DexScreener price history / CoinGecko historical data / Rekt.news
**Fallback Source**: Chainalysis / Messari depeg records
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: N
**D4**: N
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Query historical price data for each collateral token. Any depeg >5%: document. Never-depegged is a positive signal but not sufficient alone.
**Criterion ID(s)**: 4.2 / 9.2
**Red Flag ID(s)**: RF12