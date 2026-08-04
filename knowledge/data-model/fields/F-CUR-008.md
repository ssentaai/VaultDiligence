# F-CUR-008

**Field ID**: F-CUR-008
**Category**: Entity
**Sub-Category**: Curator
**Field Name**: Parameter Change Log
**What to Collect / Question to Answer**: Record of recent curator parameter changes: what changed, when, why
**Data Type**: Text
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7,VT-8)
**Collection Tier**: T1
**Primary Source**: On-chain event logs / governance forum / Chaos Labs Risk Oracle log
**Fallback Source**: Protocol dashboard
**Pillar(s)**: P7,P8
**D3**: Y
**D4**: Y
**Required?**: C
**If Not Found — Gap Action**: Frequent unexplained changes = governance risk. Changes without timelock = flag. Source from event logs.
**Criterion ID(s)**: 7.2 / 8.6
**Registered Sources (Fix 70)**: snapshot-governance-votes, tally-onchain-governance (candidate)
