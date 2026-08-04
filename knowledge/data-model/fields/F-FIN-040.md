# F-FIN-040

**Field ID**: F-FIN-040
**Category**: Financial
**Sub-Category**: Liquidity
**Field Name**: Max Position at 1% Slippage
**What to Collect / Question to Answer**: Maximum position executable within 1% slippage from verified source — not estimate
**Data Type**: Currency
**Vault Types**: ALL
**Collection Tier**: T4
**Primary Source**: OTC desk / market maker confirmation (Wintermute, Cumberland) / on-chain DEX depth
**Fallback Source**: Liquidation Network terms if disclosed
**Pillar(s)**: P9
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**Required?**: Y
**If Not Found — Gap Action**: Hard gate if unquantifiable. Cannot accept operator estimate. Must be confirmed by named market maker.
**Criterion ID(s)**: 9.6
**Red Flag ID(s)**: RF29