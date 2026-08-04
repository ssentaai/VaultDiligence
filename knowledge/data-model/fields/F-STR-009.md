# F-STR-009

**Field ID**: F-STR-009
**Category**: Strategy Risk
**Sub-Category**: Restaking
**Field Name**: Slashing-Condition Exposure of Restaked Principal
**What to Collect / Question to Answer**: Enumerate every AVS (or restaking service) the vault's restaked principal is delegated to. For each: the slashing conditions (URL), the fault types that trigger a slash, the maximum slashable fraction of the delegated stake, and whether slashing is enabled and has ever executed. State the aggregate maximum *simultaneous* slashable exposure across all opted-in AVSs, and whether any single ETH unit backs conditions on more than one AVS at once.
**Data Type**: Structured list — each entry `{ avs_identifier, slashing_conditions_url, fault_types, max_slashable_fraction_pct, slashing_enabled: bool, slashing_executed_historically: bool }` + aggregate `max_simultaneous_slashable_pct`.
**Vault Types**: `Strategy = restaking`
**Collection Tier**: T2
**Pillar(s)**: P6 (Credit — principal impairment); cross-ref P7. *(propose; operator confirms)*
**Primary Source**: Restaking protocol on-chain — operator-set / AVS registry for the opted-in AVS list, plus each AVS's slashing-contract parameters (EigenLayer AllocationManager / AVS slashing contracts or equivalent). Each AVS's published slashing conditions.
**Fallback Source**: Restaking-protocol / LRT-issuer disclosure of its opted-in AVS set and slashing terms.
**Evidence Pathway**: Inspection-validatable — read the operator-set / AVS registry on-chain to enumerate opted-in AVSs, then read each AVS's slashing parameters for the max slashable fraction and trigger conditions.
**Institutional Standard**: Every opted-in AVS is named with its slashing-conditions URL, fault types, and maximum slashable fraction; the aggregate simultaneous slashable exposure is stated; whether slashing is enabled and whether it has ever executed on any opted-in AVS is recorded.
**Status**: Gap with action
**If Not Found — Gap Action**: E if the on-chain AVS set and each slashing parameter are readable and dated. E(P) if the opted-in set is known but some AVS slashing parameters are undocumented. G2 if the opted-in set exists but is restricted / undisclosed. G3 if the protocol does not disclose which AVSs it delegates to at all (a finding — the allocator cannot price principal-loss exposure). N/A if the vault performs no restaking delegation (native staking only).
**Source / Precedent**: EigenLayer docs — slashing conditions set by the AVS and approved by the slashing veto committee; "a single staked deposit is exposed to the aggregated slashing rules … of every AVS your capital is delegated to." Hacken / Stanford Blockchain Review — five opted-in AVSs = five slashing frameworks against the same ETH pool. Sevim & Ferreira Torres, arXiv:2604.03274.
**Criterion ID(s)**: propose at ratification (candidate RF: new "restaking slashing-exposure undisclosed" condition).
