# F-ENT-073

**Field ID**: F-ENT-073
**Category**: Entity
**Sub-Category**: Jurisdiction
**Field Name**: Domicile Jurisdiction — FATF Status
**What to Collect / Question to Answer**: Is the vault's domicile jurisdiction on the FATF grey list or black list?
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T3
**Primary Source**: FATF published lists: fatf-gafi.org/publications/high-risk-jurisdictions
**Fallback Source**: World Bank Rule of Law score via api.worldbank.org
**Pillar(s)**: P2,P10
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Check FATF list for domicile jurisdiction. Grey list = elevated AML concern. Black list = auto-disqualifier for most regulated allocators.
**Criterion ID(s)**: 2.5
**v54 Refinement (gap audit 2026-06-12)**: Extend FATF-status capture to a five-year regulatory-enforcement lookback across every regime where the operator targets allocators, not the domicile jurisdiction alone. Source: Steakhouse DDQ section 5.7.
