# F-ORC-007

**Field ID**: F-ORC-007
**Category**: Oracle
**Sub-Category**: Quality
**Field Name**: Staleness Check On-Chain
**What to Collect / Question to Answer**: Does the contract revert or use circuit breaker if oracle price is stale?
**Data Type**: Boolean
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Smart contract: require(updatedAt > block.timestamp - maxStaleness) / Etherscan read
**Fallback Source**: Audit report oracle section
**Pillar(s)**: P3
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: No staleness check = flag. Oracle can return stale price silently.
**Criterion ID(s)**: 3.3