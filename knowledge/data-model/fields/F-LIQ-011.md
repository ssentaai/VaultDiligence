# F-LIQ-011

**Field ID**: F-LIQ-011
**Category**: Liquidity
**Sub-Category**: deRWA Wrapper — DEX Venues + Depth
**Field Name**: deRWA Wrapper — DEX Venue Depth ($1M/$5M/$10M)
**What to Collect / Question to Answer**: DEX venues where wrapper is traded. Estimated depth at $1M/$5M/$10M (1inch API). TVL in DEX liquidity pool.
**Data Type**: USD
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-8)
**Collection Tier**: T1 (Tier 1)
**Primary Source**: DeFiLlama pool data
**Fallback Source**:
**Pillar(s)**: P9
**D4**: Y
**D5**: Required
**Required?**:
**If Not Found — Gap Action**: NOT ACCESSIBLE — run 1inch API simulation before deployment
**Criterion ID(s)**: 9.6, RF29
**Registered Sources (Fix 70)**: defillama-market, kaiko-reference-rates
