# F-FIN-010

**Field ID**: F-FIN-010
**Category**: Financial
**Sub-Category**: Vault Metrics
**Field Name**: Native (Organic) Yield
**What to Collect / Question to Answer**: Yield from underlying strategy revenue only, excluding token incentives
**Data Type**: Percent
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Gross APY minus token incentive APY / vaults.fyi / protocol revenue data
**Fallback Source**: Token Terminal protocol revenue
**Pillar(s)**: P6
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**Required?**: Y
**If Not Found — Gap Action**: Token Terminal shows protocol fees. If fees << incentives: yield is subsidised and will compress.
**Criterion ID(s)**: 6.1
**Registered Sources (Fix 70)**: defillama-market, defillama-tvl-yield
