# F-FIN-075

**Field ID**: F-FIN-075
**Category**: Financial
**Sub-Category**: Yield Concentration
**Field Name**: Single Underlying Concentration — % of Total Yield
**What to Collect / Question to Answer**: What % of vault yield comes from a single named issuer or instrument? State issuer name and concentration %. 100% = complete single-name dependency.
**Data Type**: Percent / Text
**Vault Types**: ALL
**Collection Tier**: T3
**Primary Source**: Vault documentation / governance forum RFC / operator disclosure
**Fallback Source**: On-chain vault composition
**Pillar(s)**: P6
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Read vault specification in RFC or protocol docs. a preferred-equity-backed vault: 100% backed by a listed preferred instrument at launch. State explicitly. If operator does not disclose: flag as gap — request from operator.
**Criterion ID(s)**: 6.8
**Red Flag ID(s)**: RF43