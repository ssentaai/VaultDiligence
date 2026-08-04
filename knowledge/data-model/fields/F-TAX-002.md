# F-TAX-002

**Field ID**: F-TAX-002
**Category**: Legal
**Sub-Category**: Tax Character
**Field Name**: US Withholding Tax on Non-US Underlying Instruments
**What to Collect / Question to Answer**: For non-US underlying instruments: what US withholding tax applies to distributions received by the vault? Standard 30% for non-treaty countries. Reduced rate under applicable tax treaty?
**Data Type**: Text / Percent
**Vault Types**: ALL
**Collection Tier**: T3
**Primary Source**: Operator tax counsel opinion / IRS withholding rates publication
**Fallback Source**: Vault operator disclosure
**Pillar(s)**: P10
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Conditional
**If Not Found — Gap Action**: Apply only where underlying is a non-US instrument. Request tax counsel opinion from operator. State withholding rate and treaty position if applicable.
**Criterion ID(s)**: 10.6