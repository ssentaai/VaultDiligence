# F-FIN-002

**Field ID**: F-FIN-002
**Category**: Financial
**Sub-Category**: Vault Metrics
**Field Name**: TVL 7-Day Change (%)
**What to Collect / Question to Answer**: % change in TVL over prior 7 days
**Data Type**: Percent
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: DefiLlama TVL chart / protocol dashboard
**Fallback Source**: Nansen vault monitor
**Pillar(s)**: P9
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: >-20% in 7 days = flag for redemption pressure. >+100% in 7 days = APY dilution risk.
**Criterion ID(s)**: 9.4
**Registered Sources (Fix 70)**: coingecko-market-data, defillama-market, defillama-tvl-yield
