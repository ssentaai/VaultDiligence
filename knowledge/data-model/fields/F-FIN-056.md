# F-FIN-056

**Field ID**: F-FIN-056
**Category**: Financial
**Sub-Category**: Duration
**Field Name**: Duration Mismatch — Calculated Gap and Management
**What to Collect / Question to Answer**: Asset duration minus liability duration in days. Is there an immunisation strategy? Interest rate sensitivity analysis?
**Data Type**: Number (days)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-8)
**Collection Tier**: T3
**Primary Source**: Calculated from F-FIN-054 minus F-FIN-055. FRED API for current rate sensitivity: api.stlouisfed.org — DGS3MO for 3M T-bill rate.
**Fallback Source**: Operator interest rate sensitivity documentation
**Pillar(s)**: P6
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: >180 day mismatch with no documented immunisation = flag. SVB: long-duration bond portfolio backing short-duration deposits with no rate hedging.
**Criterion ID(s)**: 6.3