# F-COL-008

**Field ID**: F-COL-008
**Category**: Financial
**Sub-Category**: Collateral Contagion
**Field Name**: Cross-Protocol Contagion Map
**What to Collect / Question to Answer**: Which other protocols accept the same collateral tokens? If collateral depegs, which protocols are simultaneously affected? Resolv precedent: simultaneous exposure across 15 Morpho vaults.
**Data Type**: Text
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1,VT-6,VT-7)
**Collection Tier**: T1
**Primary Source**: Morpho markets API / DefiLlama collateral data / protocol documentation
**Fallback Source**: Curator disclosure
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: N
**D4**: N
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Query which protocols accept each collateral token. Map simultaneous exposure. Concentrated cross-protocol exposure to single collateral = elevated systemic risk.
**Criterion ID(s)**: 4.5 / 7.6
**v54 Refinement (gap audit 2026-06-12)**: Add a shared-pool contagion sub-dimension: whether the token sits in a shared lending pool or E-Mode grouping where its depeg can freeze unrelated depositors via utilisation (Kelp/Aave: E-Mode treated depegged rsETH as valid, freezing ETH/USDC depositors with no rsETH exposure). Cross-ref F-LIQ-048, VT-6.
**Red Flag ID(s)**: RF35