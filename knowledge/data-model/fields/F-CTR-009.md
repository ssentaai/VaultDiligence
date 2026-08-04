# F-CTR-009

**Field ID**: F-CTR-009
**Category**: Contract
**Sub-Category**: Architecture
**Field Name**: Stack Depth
**What to Collect / Question to Answer**: Count of distinct protocol layers in dependency chain
**Data Type**: Number
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Calculated from F-CTR-008
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**Required?**: Y
**If Not Found — Gap Action**: Stack ≥3 layers with no circuit breaker = flag RF25. Source: count from dependency map.
**Criterion ID(s)**: 7.6
**Red Flag ID(s)**: RF25