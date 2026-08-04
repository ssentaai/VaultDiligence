# F-HED-004

**Field ID**: F-HED-004
**Category**: Financial
**Sub-Category**: Hedge
**Field Name**: Negative Funding Duration — Historical Maximum
**What to Collect / Question to Answer**: What is the longest consecutive period of negative funding rates observed for this strategy's assets? What was the P&L impact on the junior tranche?
**Data Type**: Text
**Vault Types**: Structure=delta-neutral-synthetic OR Structure=tranched  (derived from VT-N; original "Vault Types" value: VT-2,VT-4)
**Collection Tier**: T1
**Primary Source**: Coinglass API: funding rate history — identify longest negative funding streak
**Fallback Source**: Operator documentation — request modelled junior tranche tolerance for 90/180 day negative funding
**Pillar(s)**: P5
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: No negative funding analysis = flag. Post-Merge ETH: negative funding persisted for extended periods. Operators without model = blind to this risk.
**Criterion ID(s)**: 5.4