# F-FIN-052

**Field ID**: F-FIN-052
**Category**: Financial
**Sub-Category**: Collateral
**Field Name**: Vault Token as External Collateral — Protocol List
**What to Collect / Question to Answer**: In which external protocols is the vault token accepted as collateral? What is the total borrowed against it?
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Morpho API: check if vault token is a listed collateral asset. Aave / Compound subgraph: same check.
**Fallback Source**: DefiLlama protocol page — check integrations section for vault token
**Pillar(s)**: P4
**D3**: Y
**D4**: Y
**Required?**: C
**If Not Found — Gap Action**: Identify all protocols using vault token as collateral. Aggregate borrowed amount. If >20% of vault TVL is borrowed externally = flag. RF23/RF24.
**Criterion ID(s)**: 4.8
**Red Flag ID(s)**: RF23