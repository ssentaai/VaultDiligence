# F-FIN-035

**Field ID**: F-FIN-035
**Category**: Financial
**Sub-Category**: Collateral
**Field Name**: DEX Depth for Collateral Liquidation
**What to Collect / Question to Answer**: On-chain DEX liquidity available to execute collateral liquidations at scale
**Data Type**: Currency
**Vault Types**: Strategy=lending OR Structure=delta-neutral-synthetic OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-2,VT-7,VT-8)
**Collection Tier**: T1
**Primary Source**: DexScreener / CoinGecko DEX pools / on-chain AMM depth query
**Fallback Source**: Dune liquidity depth query
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**Required?**: C
**If Not Found — Gap Action**: Gauntlet explicitly cites this. Thin DEX depth = liquidation cascade when forced seller hits market.
**Criterion ID(s)**: 4.5