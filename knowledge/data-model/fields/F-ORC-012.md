# F-ORC-012

**Field ID**: F-ORC-012
**Category**: Oracle
**Sub-Category**: RWA-Specific
**Field Name**: NAV Oracle to Liquidation Link
**What to Collect / Question to Answer**: For VT-7: does NAV oracle directly feed liquidation threshold? What is the chain?
**Data Type**: Text
**Vault Types**: Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-7)
**Collection Tier**: T3
**Primary Source**: Aave/lending protocol oracle config / governance docs
**Fallback Source**: LlamaRisk report
**Pillar(s)**: P3,P4
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Stale NAV oracle in leveraged stack = delayed liquidation trigger. Describe the full chain.
**Criterion ID(s)**: 3.5 / 4.7