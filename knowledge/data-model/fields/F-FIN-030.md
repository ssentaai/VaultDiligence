# F-FIN-030

**Field ID**: F-FIN-030
**Category**: Financial
**Sub-Category**: Collateral
**Field Name**: Primary Collateral Asset(s)
**What to Collect / Question to Answer**: What backs this vault? List all collateral assets with their categories
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: On-chain: vault allocationStrategy() / Morpho API / protocol docs
**Fallback Source**: DefiLlama collateral list
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Classify each: native crypto / LST / wrapped / stablecoin / RWA / governance token (self-referential = flag).
**Criterion ID(s)**: 4.1