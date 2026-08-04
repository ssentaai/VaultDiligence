# F-STR-012

**Field ID**: F-STR-012
**Category**: Strategy Risk
**Sub-Category**: Restaking
**Field Name**: Restaking Unbonding Pathway & Queue Congestion
**What to Collect / Question to Answer**: What is the full *compounded* exit pathway and delay for the vault's restaked principal — AVS / operator undelegation window + restaking-protocol escrow (e.g. EigenLayer ~7-day) + beacon-chain validator exit queue — and for how long is principal *both* illiquid *and* still slashable during exit? State each leg's delay, the aggregate worst-case unbonding time, and the current queue depth / congestion.
**Data Type**: Structured — `{ leg_name, delay, slashable_during_leg: bool }` for each leg + `aggregate_worst_case_unbonding` + `current_queue_state`.
**Vault Types**: `Strategy = restaking`
**Collection Tier**: T2
**Pillar(s)**: P9 (Liquidity). *(propose; operator confirms)*
**Primary Source**: Restaking protocol contracts (escrow / withdrawal-delay parameters) + beacon-chain exit-queue state, read on-chain and dated.
**Fallback Source**: Restaking-protocol documentation stating each unbonding leg's delay; third-party exit-queue trackers cited with date.
**Evidence Pathway**: Inspection-validatable — read the escrow / undelegation delay from the restaking contracts and the current beacon-chain exit-queue length on-chain; sum the legs for the aggregate worst-case and note which legs leave principal slashable.
**Institutional Standard**: Each leg of the exit path is named with its delay, the aggregate worst-case unbonding time is stated, whether principal remains slashable during escrow is recorded, and current queue congestion is dated — so the allocator sees the true time-to-exit, not a headline "liquid" claim.
**Status**: Gap with action
**If Not Found — Gap Action**: E if each leg's delay and current queue state are readable on-chain and dated. E(P) if the mechanism is documented but current congestion is unknown. G2 if delay parameters exist but are undisclosed. G3 if no unbonding schedule is defined. N/A if the vault holds only a freely-transferable LRT with *no* redemption right exercised by the vault (then exit is F-STR-016 secondary-market, not unbonding — state which).
**Source / Precedent**: EigenLayer docs — LST/EIGEN clears a ~7-day escrow plus the base-chain exit queue, and the escrow exists so slashing can execute before withdrawal. Sevim & Ferreira Torres, arXiv:2604.03274.
**Criterion ID(s)**: propose at ratification.
