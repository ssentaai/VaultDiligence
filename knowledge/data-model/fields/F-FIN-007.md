# F-FIN-007

**Field ID**: F-FIN-007
**Category**: Financial
**Sub-Category**: Vault Metrics
**Field Name**: NAV Per Share
**What to Collect / Question to Answer**: Current net asset value per vault share / token
**Data Type**: Currency
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Vault.convertToAssets(1e18) on-chain / CoinGecko / RWA.xyz
**Fallback Source**: Protocol dashboard
**Pillar(s)**: P3,P9
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Cross-check oracle-reported NAV against on-chain calculation. Divergence = flag.
**Criterion ID(s)**: 3.1 / 9.2
**Registered Sources (Fix 70)**: coingecko-market-data, coinmarketcap-market-data, kaiko-reference-rates, messari-market-data
