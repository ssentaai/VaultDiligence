# F-ORC-005

**Field ID**: F-ORC-005
**Category**: Oracle
**Sub-Category**: Quality
**Field Name**: Update Frequency / Heartbeat
**What to Collect / Question to Answer**: How often oracle updates under normal conditions (seconds/minutes/hours/daily)
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Oracle heartbeat contract: latestTimestamp() / oracle docs
**Fallback Source**: On-chain event log frequency
**Pillar(s)**: P3
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Daily (NAV oracles) vs real-time (price oracles) have different staleness risk profiles.
**Criterion ID(s)**: 3.3