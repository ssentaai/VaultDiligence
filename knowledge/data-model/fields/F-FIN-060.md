# F-FIN-060

**Field ID**: F-FIN-060
**Category**: Financial
**Sub-Category**: Leverage Stack
**Field Name**: Looping Exposure Estimate — Recursive Borrowing Against Vault Token
**What to Collect / Question to Answer**: Is there evidence of recursive borrowing using this vault's issued tokens? What is the estimated leverage multiplier: total borrowed against vault token across all external protocols relative to vault's own TVL? This surfaces the unknown leverage stack Blume (Two Prime) identifies as the core DeFi lending reckoning risk.
**Data Type**: Percent / Number
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Cross-reference F-FIN-052 (total borrowed against vault token externally) with F-FIN-001 (vault TVL). Leverage multiplier = external borrowed / vault TVL. Morpho API + Aave subgraph for external borrowing against vault token.
**Fallback Source**: DefiLlama protocol page — integrations showing vault token as collateral and estimated borrowed
**Pillar(s)**: P4,P6,P9
**D3**: Y
**D4**: Y
**Required?**: Y
**If Not Found — Gap Action**: Leverage multiplier >20% of TVL = flag. >50% = blocking. No visibility on looping = flag RF27. Blume: 'unknown amounts of leverage are built into DeFi markets' — partially traceable on-chain via vault token collateral positions.
**Criterion ID(s)**: 6.3 / 9.4 / 4.8
**Red Flag ID(s)**: RF27