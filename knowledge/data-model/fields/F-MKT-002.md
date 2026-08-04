# F-MKT-002

**Field ID**: F-MKT-002
**Category**: Market Data
**Sub-Category**: Rates
**Field Name**: 3-Month T-Bill Yield
**What to Collect / Question to Answer**: Current 3-month US T-bill yield at assessment date
**Data Type**: Percent
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: FRED API: series_id=DTB3
**Fallback Source**: US Treasury: home.treasury.gov/resource-center/data-chart-center/interest-rates
**Pillar(s)**: P6
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Alternative risk-free benchmark. Use SOFR for floating-rate products, T-bill for fixed.
**Criterion ID(s)**: 6.1
**Registered Sources (Fix 70)**: fred-risk-free-rate (candidate)
