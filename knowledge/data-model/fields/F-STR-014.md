# F-STR-014

**Field ID**: F-STR-014
**Category**: Strategy Risk
**Sub-Category**: Restaking
**Field Name**: AVS-Specific Failure & Slashing-Dispute Mechanics
**What to Collect / Question to Answer**: For each AVS the vault opts into, what is its audit history, time-live, and total value secured and what governs *unjust*-slashing risk — is there a slashing veto committee, a dispute / challenge window, or insurance, and who controls the slashing trigger? Could an AVS bug or governance capture slash correctly-behaving operators (and therefore the vault's principal)?
**Data Type**: Structured per-AVS — `{ avs_id, audits, time_live, total_value_secured, slashing_trigger_controller, veto_or_dispute_mechanism, dispute_window, insurance }`.
**Vault Types**: `Strategy = restaking`
**Collection Tier**: T2
**Pillar(s)**: P7 (Smart Contract) + P6. *(propose; operator confirms)*
**Primary Source**: Each AVS's audit reports, deployment date, and slashing-governance documentation; on-chain slashing-trigger authority and veto-committee configuration.
**Fallback Source**: Restaking-protocol disclosure of the AVS's risk profile; third-party AVS risk assessments, cited with date.
**Evidence Pathway**: Third-party-evidenced — obtain each AVS's named audits and slashing-governance docs; Inspection-validatable — read the slashing-trigger authority and veto / dispute configuration on-chain.
**Institutional Standard**: Each opted-in AVS is named with its audits, time-live, and value secured; the slashing-trigger controller is identified; a veto committee, dispute window, or insurance against unjust slashing is documented — so the allocator sees whether an AVS bug or governance capture can reach the vault's principal.
**Status**: Gap with action
**If Not Found — Gap Action**: E if each AVS's audits, age, and slashing-governance are documented and the trigger authority is readable on-chain. E(P) if some AVSs are documented and others are not. G2 if an AVS exists but its slashing governance is undisclosed. G3 if an AVS has slashing enabled with no dispute / veto mechanism and none is documented (a finding). N/A if no opted-in AVS has slashing enabled (state it).
**Source / Precedent**: EigenLayer docs — slashing conditions are set by the AVS and approved by the slashing veto committee before the AVS may operate. Sevim & Ferreira Torres, arXiv:2604.03274. Industry commentary — each added AVS increases attack surface and slashing vulnerability.
**Criterion ID(s)**: propose at ratification.
