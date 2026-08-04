# F-FIN-034

**Field ID**: F-FIN-034
**Category**: Financial
**Sub-Category**: Collateral
**Field Name**: Liquidation Depth at -5%
**What to Collect / Question to Answer**: Total USD value of collateral liquidatable if collateral price falls 5%
**Data Type**: Currency
**Vault Types**: Strategy=lending OR Structure=delta-neutral-synthetic OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-1,VT-2,VT-7,VT-8)
**Collection Tier**: T2a
**Primary Source**: Chaos Labs risk dashboard / Gauntlet risk simulations / Credora asset layer
**Fallback Source**: Dune Analytics liquidation analysis query
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**Required?**: C
**If Not Found — Gap Action**: This is the Credora market layer field. Thin liquidation depth = cascade risk. Key for institutional size.
**Criterion ID(s)**: 4.5