# F-STR-010

**Field ID**: F-STR-010
**Category**: Strategy Risk
**Sub-Category**: Restaking
**Field Name**: AVS-Correlation / Cascading Slashing Exposure
**What to Collect / Question to Answer**: Across the AVSs the vault opts into, how correlated is the slashable exposure — how many AVSs share the same node operators, and could one operator fault or one correlated event slash multiple AVSs against the same restaked pool simultaneously? State the worst-case correlated slash (one operator / event, multiple AVSs). Record the systemic context: the vault's restaked ETH as a share of total staked ETH and of total restaked ETH.
**Data Type**: Structured — operator↔AVS overlap map; `worst_case_correlated_slashable_pct`; `restake_share_of_total_staked_eth_pct`; `share_of_total_restaked_eth_pct`.
**Vault Types**: `Strategy = restaking`
**Collection Tier**: T2
**Pillar(s)**: P6 (Credit) + P4 (contagion). *(propose; operator confirms)*
**Primary Source**: Restaking protocol on-chain — operator registrations mapped to the AVSs each operator serves; total-staked-ETH and total-restaked-ETH aggregates from beacon-chain / restaking-protocol TVL.
**Fallback Source**: Third-party restaking dashboards (operator/AVS overlap, restake-share metrics) cited with date.
**Evidence Pathway**: Inspection-validatable — read operator→AVS registrations on-chain to build the overlap map; compute the correlated worst-case from the overlaps and the per-AVS max slashable fractions (F-STR-009).
**Institutional Standard**: The overlap between opted-in AVSs and shared operators is mapped; the worst-case correlated slash is stated; the systemic context (restaked ETH vs total staked ETH, against the 33% consensus-security threshold) is noted so the allocator sees whether the position sits in benign or cascade-prone territory.
**Status**: Gap with action
**If Not Found — Gap Action**: E if operator↔AVS overlap and restake-share are readable and dated. E(P) if the overlap is partial or the share figure is stale. G2 if operator-set is restricted. G3 if the protocol does not publish which operators serve which AVSs. N/A if the vault delegates to a single AVS with a single operator (state it explicitly — no correlation, but concentration is then F-STR-011).
**Source / Precedent**: Sevim & Ferreira Torres, arXiv:2604.03274 — restaked ETH ≈ 13% of staked ETH vs the 33% consensus-security threshold; cascading-slashing scenario across interconnected protocols. Consensys / Hacken — "an AVS bug, exploit, or governance attack can trigger slashing across many restakers simultaneously … tail risk grows as restaked ETH increases as a proportion of total staked ETH."
**Criterion ID(s)**: propose at ratification.
