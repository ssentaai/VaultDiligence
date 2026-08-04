# F-LIQ-041

**Field ID**: F-LIQ-041
**Category**: Liquidity
**Sub-Category**: Secondary Market Depth
**Field Name**: Within-Venue LP Diversity
**What to Collect / Question to Answer**: For each venue where the vault token trades, how many independent liquidity providers supply the depth, and what share of that venue's depth rests on the single largest LP?
**Data Type**: Structured list (per venue: LP count, largest-LP share of depth) + named LP entities
**Vault Types**: ALL
**Collection Tier**: T2
**Pillar(s)**: P9
**Primary Source**: On-chain LP-position enumeration per pool (DEX subgraph / pool contract LP-token holders); market-maker agreements where they exist
**Fallback Source**: Protocol liquidity dashboard; operator disclosure of named market makers and their committed depth
**Evidence Pathway**: Inspection-validatable: enumerate LP-token holders and per-position depth on each pool contract and rank concentration; a single deep venue with verified independent LPs is the structural concern, not the count of venues.
**Institutional Standard**: Liquidity-provider diversity within each venue is the primary structural concern. A single deep venue with verified independent LP diversity is acceptable; a fragmented multi-venue footprint resting on thin or single-LP depth is not an improvement on it.
**Status**: Gap with action
**If Not Found — Gap Action**: Enumerate LP positions per venue from on-chain pool state and rank the largest-LP share of depth. Where depth concentrates on one provider, name that entity and confirm whether a market-maker agreement binds it. If LP composition cannot be read on-chain and is not disclosed, classify G2 and name the venue and pool requiring the disclosure.
**Source / Precedent**: Aave LlamaRisk framework, 9 Jun 2026 (§1.5): 'Liquidity-provider diversity within each venue is the primary structural concern. A single deep venue with verified LP diversity is acceptable. A fragmented multi-venue footprint with thin LP diversity offers limited improvement.'
**Criterion ID(s)**: 9.1
