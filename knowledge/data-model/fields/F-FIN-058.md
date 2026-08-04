# F-FIN-058

**Field ID**: F-FIN-058
**Category**: Financial
**Sub-Category**: Composability
**Field Name**: DeFi Integrations — Live Protocol Count
**What to Collect / Question to Answer**: How many live DeFi protocols accept this vault token? (Lending markets, DEXs, yield aggregators). Multiple integrations = multiple exit paths.
**Data Type**: Number
**Vault Types**: Strategy=lending OR Strategy in {staking,restaking} OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-5,VT-6,VT-8)
**Collection Tier**: T1
**Primary Source**: DefiLlama protocol page — integrations section. Etherscan — check if vault token appears in other protocol contracts.
**Fallback Source**: Protocol documentation — integration page
**Pillar(s)**: P9
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Zero DeFi integrations and single redemption path = flag. Composability creates exit optionality and liquidity depth.
**Criterion ID(s)**: 9.5