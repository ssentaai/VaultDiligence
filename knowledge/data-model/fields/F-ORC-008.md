# F-ORC-008

**Field ID**: F-ORC-008
**Category**: Oracle
**Sub-Category**: Quality
**Field Name**: Oracle Last Update Timestamp
**What to Collect / Question to Answer**: When did the oracle last update at time of assessment?
**Data Type**: DateTime
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: On-chain: latestRoundData() on Chainlink / latestAnswer() / oracle dashboard
**Pillar(s)**: P3
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Calculate staleness at time of assessment. >24hrs for price oracle = flag.
**Criterion ID(s)**: 3.3