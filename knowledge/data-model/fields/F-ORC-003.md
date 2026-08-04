# F-ORC-003

**Field ID**: F-ORC-003
**Category**: Oracle
**Sub-Category**: Architecture
**Field Name**: Number of Independent Data Sources
**What to Collect / Question to Answer**: Count of truly independent underlying data sources feeding the oracle
**Data Type**: Number
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Oracle provider documentation / on-chain aggregation contract
**Fallback Source**: Chronicle validator set / Chainlink node list
**Pillar(s)**: P3
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: 1 source = single point of failure. 3+ independent = acceptable. <3 = flag.
**Criterion ID(s)**: 3.1
**Red Flag ID(s)**: RF08