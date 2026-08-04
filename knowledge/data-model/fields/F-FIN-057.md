# F-FIN-057

**Field ID**: F-FIN-057
**Category**: Financial
**Sub-Category**: Composability
**Field Name**: ERC-4626 Compliance — Interface Confirmation
**What to Collect / Question to Answer**: Does the vault implement ERC-4626 standard interface? deposit(), withdraw(), convertToAssets(), convertToShares() all present?
**Data Type**: Y/N
**Vault Types**: Strategy=lending OR Strategy in {staking,restaking} OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-5,VT-6,VT-8)
**Collection Tier**: T1
**Primary Source**: Etherscan contract ABI — check for ERC-4626 function signatures. Vault contract read.
**Fallback Source**: Protocol documentation — stated ERC-4626 compliance
**Pillar(s)**: P9
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Non-ERC-4626 vault = reduced composability, harder for aggregators to integrate, fewer exit paths.
**Criterion ID(s)**: 9.5