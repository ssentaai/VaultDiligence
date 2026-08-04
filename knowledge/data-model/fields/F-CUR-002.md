# F-CUR-002

**Field ID**: F-CUR-002
**Category**: Entity
**Sub-Category**: Curator
**Field Name**: Curator Track Record — Bad Debt History
**What to Collect / Question to Answer**: Has this curator's vault(s) ever incurred bad debt? Amount and cause.
**Data Type**: Text
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7,VT-8)
**Collection Tier**: T3
**Primary Source**: Rekt.news / governance forum / public incident reports / DeFiLlama
**Fallback Source**: Dune Analytics vault-specific dashboard
**Pillar(s)**: P8
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**Required?**: C
**If Not Found — Gap Action**: Zero bad debt through stress = positive evidence. Any bad debt = flag with amount and cause.
**Criterion ID(s)**: 8.1 / 6.4
**Registered Sources (Fix 70)**: expert-curator-forum, expert-governance-forum
