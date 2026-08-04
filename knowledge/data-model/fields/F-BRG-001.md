# F-BRG-001

**Field ID**: F-BRG-001
**Category**: Bridging
**Sub-Category**: Route Topology
**Field Name**: Bridge Route Topology Disclosure
**What to Collect / Question to Answer**: Is every route carrying vault exposure documented at route level before assessment — origin chain and canonical supply, target-chain representation (mint-and-burn, lock-and-mint, native-bridge), bridge or messaging system by name and version, per-route verifier/attestor/oracle configuration, and bridge admin/upgrade controls on both chains?
**Data Type**: Structured text (per route)
**Vault Types**: ALL (any vault whose token, collateral, or dependency chain crosses a bridge or cross-chain messaging system; N/A for single-chain vaults with no bridged collateral and no cross-chain dependency — state why)
**Collection Tier**: T2
**Pillar(s)**: P12
**Primary Source**: Issuer route-topology disclosure cross-checked against on-chain bridge admin and upgrade controls on both the origin and target chains; bridge/messaging vendor versioned documentation
**Fallback Source**: Block-explorer enumeration of bridge contracts and their admin/owner addresses on each chain; vendor deployment registry naming the messaging system and version
**Evidence Pathway**: Inspection-validatable — read the bridge contracts on origin and target chains to confirm the representation model (lock/mint vs mint-and-burn vs native), the named messaging system and version, and the admin/upgrade owners on both sides.
**Institutional Standard**: Complete route-level topology is disclosed for every route carrying vault exposure, with no undocumented route; weak origin-chain controls are assessed as part of target-chain exposure. Topology disclosure is the precondition for assessing every other bridging criterion.
**Status**: Gap with action
**If Not Found — Gap Action**: Name the issuer and request a written per-route topology table covering origin chain, canonical supply, target-chain representation, messaging system and version, per-route verifier configuration, and both-chain admin/upgrade controls. State that until this is supplied no other P12 criterion can be assessed — record as RF44 critical condition on any route with material exposure.
**Source / Precedent**: a synthetic-dollar and CLO-fund diligence 2026: bridge security risk could not be quantified because the adapter implementation and quorum configuration were undisclosed — the gap blocked a real allocator's assessment.
**Criterion ID(s)**: 12.1, RF44 (cross-ref F-CTR-019)
**Registered Sources (Fix 70)**: l2beat-chain-risk, l2beat-scaling-risk, layerzero-scan-dvn (candidate)
