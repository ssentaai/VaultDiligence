# F-STR-011

**Field ID**: F-STR-011
**Category**: Strategy Risk
**Sub-Category**: Restaking
**Field Name**: Operator-Set Quality & Delegation Concentration
**What to Collect / Question to Answer**: To which node operators is the vault's restake delegated, and what is the concentration — the largest single operator's share of the vault's delegated stake, the operator identities, their geographic / client / infrastructure diversity, and each operator's prior slashing history? For an LRT-issuing vault, additionally record the issuer's share of the total LRT market (single-issuer systemic concentration).
**Data Type**: Structured list — `{ operator_id, share_of_delegated_stake_pct, identity, client/infra_diversity, prior_slashing_events }` + `largest_operator_share_pct` + (if LRT) `issuer_market_share_pct`.
**Vault Types**: `Strategy = restaking`
**Collection Tier**: T2
**Pillar(s)**: P8 (Team & Ops). *(propose; operator confirms)*
**Primary Source**: Restaking protocol on-chain — delegation records mapping the vault's restake to operators and their stake shares; operator registration metadata.
**Fallback Source**: Restaking-protocol / LRT-issuer operator disclosures and third-party operator dashboards, cited with date.
**Evidence Pathway**: Inspection-validatable — read delegation records on-chain to compute each operator's share of the vault's restake and identify the largest; corroborate operator identity and diversity from registration metadata.
**Institutional Standard**: Operators are named with their share of the vault's delegated stake; the largest-operator concentration is stated; client / infra / geographic diversity and any prior slashing events are recorded; for LRTs, the issuer's market share is noted so single-issuer systemic concentration is visible.
**Status**: Gap with action
**If Not Found — Gap Action**: E if delegation shares and operator identities are readable and dated. E(P) if shares are readable but identity / diversity is thin. G2 if the operator set is disclosed to the protocol but restricted from the public. G3 if operator delegation is not disclosed at all. N/A only if the vault restakes solely to its own single operator (then state that single-operator concentration explicitly).
**Source / Precedent**: Sevim & Ferreira Torres, arXiv:2604.03274 — Ether.fi ≈ 65.4% LRT market share; "a single protocol acting as the primary issuer of LRTs would concentrate the power to delegate vast amounts of staked ETH." EigenLayer operator-delegation model.
**Cross-references**: F-STD-001/F-STD-006 (party-standing of the operator/AVS as a yield-critical party)
**Criterion ID(s)**: propose at ratification.
