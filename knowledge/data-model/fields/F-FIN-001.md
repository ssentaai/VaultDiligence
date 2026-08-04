# F-FIN-001

**Field ID**: F-FIN-001
**Category**: Financial
**Sub-Category**: Vault Metrics
**Field Name**: TVL at Assessment
**What to Collect / Question to Answer**: Total Value Locked at time of assessment in USD
**Data Type**: Currency
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: DefiLlama: api.llama.fi/tvl/{protocol} / Morpho API / RWA.xyz
**Fallback Source**: CoinGecko protocol page
**Pillar(s)**: P9
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Record date and time of snapshot. TVL ≠ AUM for leveraged strategies.
**Criterion ID(s)**: 9.1
**Registered Sources (Fix 70)**: coingecko-market-data, coinmarketcap-market-data, defillama-market, defillama-tvl-yield, direct-rpc-read, messari-market-data
