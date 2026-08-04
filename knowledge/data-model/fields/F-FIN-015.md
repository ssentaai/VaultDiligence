# F-FIN-015

**Field ID**: F-FIN-015
**Category**: Financial
**Sub-Category**: Fees
**Field Name**: Net Yield vs Risk-Free (bps)
**What to Collect / Question to Answer**: Basis points above current risk-free rate (SOFR or T-bill)
**Data Type**: Number
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Calculated: F-FIN-014 minus F-MKT-001
**Pillar(s)**: P6
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**Required?**: Y
**If Not Found — Gap Action**: The premium for bearing all the risks in this vault. Negative = vault currently underperforms risk-free.
**Criterion ID(s)**: 6.5 / 6.1
**Registered Sources (Fix 70)**: fred-risk-free-rate (candidate)
