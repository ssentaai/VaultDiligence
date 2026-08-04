# F-CUR-007

**Field ID**: F-CUR-007
**Category**: Entity
**Sub-Category**: Curator
**Field Name**: Vault TVL Scalability
**What to Collect / Question to Answer**: Can vault absorb large inflows (e.g. 10x TVL in one block) without APY collapse? Evidence?
**Data Type**: Text
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7,VT-8)
**Collection Tier**: T3
**Primary Source**: Curator disclosure / historical TVL data: DefiLlama / governance forum
**Fallback Source**: Vaults.fyi historical data
**Pillar(s)**: P9
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Gauntlet explicitly cites this as a differentiator. Source: vault TVL history during inflow events.
**Criterion ID(s)**: 9.1 / 9.4