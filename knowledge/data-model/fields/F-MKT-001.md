# F-MKT-001

**Field ID**: F-MKT-001
**Category**: Market Data
**Sub-Category**: Rates
**Field Name**: Risk-Free Rate (SOFR)
**What to Collect / Question to Answer**: Current SOFR rate at assessment date
**Data Type**: Percent
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: FRED API: api.stlouisfed.org/fred/series/observations?series_id=SOFR
**Fallback Source**: sofrrate.com
**Pillar(s)**: P6
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**Required?**: Y
**If Not Found — Gap Action**: Record date. Used to calculate F-FIN-015 net yield premium over risk-free.
**Criterion ID(s)**: 6.1
**Registered Sources (Fix 70)**: fred-risk-free-rate (candidate)
