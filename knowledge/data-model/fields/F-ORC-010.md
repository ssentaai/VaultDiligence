# F-ORC-010

**Field ID**: F-ORC-010
**Category**: Oracle
**Sub-Category**: Resilience
**Field Name**: Circuit Breaker / Bounds Validation
**What to Collect / Question to Answer**: Are there upper/lower price bounds that reject out-of-range oracle updates?
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Contract: getLTV() with bounds / Aave Horizon oracle config / docs
**Fallback Source**: Audit report
**Pillar(s)**: P3
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Chainlink SmartData / Chronicle bounds = strong. No bounds = manipulation surface. Note implementation.
**Criterion ID(s)**: 3.2