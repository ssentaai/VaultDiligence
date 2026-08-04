# F-FIN-054

**Field ID**: F-FIN-054
**Category**: Financial
**Sub-Category**: Duration
**Field Name**: Asset Duration — Average Maturity
**What to Collect / Question to Answer**: What is the average maturity / duration of the vault's underlying assets? For RWA: weighted average life of the portfolio.
**Data Type**: Number (days)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-8)
**Collection Tier**: T3
**Primary Source**: Centrifuge pool API: api.centrifuge.io/pools/{id} — average asset maturity. Fund prospectus for private credit vaults.
**Fallback Source**: Operator reporting — request weighted average life of portfolio
**Pillar(s)**: P6
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Duration not disclosed = gap. Duration >180 days with overnight liabilities = flag (SVB failure mode).
**Criterion ID(s)**: 6.3