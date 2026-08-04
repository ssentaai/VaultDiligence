# F-STR-013

**Field ID**: F-STR-013
**Category**: Strategy Risk
**Sub-Category**: Restaking
**Field Name**: Restaking-Depth & Leverage-on-Leverage
**What to Collect / Question to Answer**: How many times is the same underlying ETH reused as economic security or collateral? Record (a) restaking depth — the number of AVSs one unit of the vault's restake simultaneously secures; and (b) downstream leverage — whether the vault's LRT is further re-deposited or looped as collateral in lending markets (leverage-on-leverage). State the effective multiple of obligations per unit of principal and where each downstream position sits.
**Data Type**: Structured — `avs_per_unit_count` + downstream looping/leverage map `{ venue, position, leverage }` + `effective_obligation_multiple`.
**Vault Types**: `Strategy = restaking`
**Collection Tier**: T2
**Pillar(s)**: P4 / P6. *(propose; operator confirms)*
**Primary Source**: Restaking protocol on-chain — count of AVSs a unit of restake secures (from F-STR-009 opted-in set) + on-chain trace of the LRT into lending markets / looping vaults.
**Fallback Source**: Protocol / curator disclosure of the strategy's looping and downstream-collateral use; DefiLlama / lending-market data for LRT deposits, cited with date.
**Evidence Pathway**: Inspection-validatable — read the opted-in AVS count and follow the LRT on-chain into any lending / looping venue to establish the obligation multiple per unit of principal.
**Institutional Standard**: The number of AVSs one unit of restake secures is stated, any downstream re-looping of the LRT as collateral is mapped, and the effective obligation multiple per unit of principal is recorded so the allocator sees whether a single breach cascades across stacked positions.
**Status**: Gap with action
**If Not Found — Gap Action**: E if the AVS-per-unit count and downstream positions are readable on-chain and dated. E(P) if restaking depth is known but downstream looping is only partly traceable. G2 if the strategy's looping is disclosed to the protocol but not published. G3 if the strategy does not disclose whether it loops. N/A if the vault does no restaking and no looping (not a restaking vault).
**Source / Precedent**: Sevim & Ferreira Torres, arXiv:2604.03274 — ezETH looped and bridged (30.18% bridged); interconnection across DeFi. Hacken / Stanford — "if restaked assets flow repeatedly through lending loops or derivative stacks, any breach can cascade across protocols." EigenLayer over-collateralisation / stacked-AVS discussion.
**Criterion ID(s)**: propose at ratification.
