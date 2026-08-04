# F-CHN-004

**Field ID**: F-CHN-004
**Category**: Chain
**Sub-Category**: Finality & Exit
**Field Name**: Finality, Withdrawal & Escape Mechanics
**What to Collect / Question to Answer**: What is the chain's finality model and lag (probabilistic, economic, deterministic stated separately), its reorg history relative to that finality assumption, its L2 withdrawal mechanism and standing delay, the availability of a forced-inclusion / escape hatch, the maturity of its fraud-proof or zk-proof system, and the MEV characteristics affecting liquidation execution?
**Data Type**: Structured text (finality type + lag; deepest reorg vs finality assumption; withdrawal mechanism + delay; escape-hatch present/absent; proof-system maturity; MEV/private-orderflow profile)
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P13
**Primary Source**: Chain documentation on finality and withdrawal mechanics; settlement / bridge contract exposing the forced-inclusion path; proof-system status documentation; reorg history from block explorer / chain telemetry
**Fallback Source**: Third-party finality and withdrawal analyses (L2BEAT stage and proof-maturity classifications, reorg trackers)
**Evidence Pathway**: Inspection-validatable: read the settlement/withdrawal contract on-chain to confirm the forced-inclusion or escape-hatch function exists and its standing delay, and inspect block-explorer reorg history; Third-party-evidenced: cite L2BEAT for proof-system maturity and withdrawal delay classification.
**Institutional Standard**: Bounded reorg depth; a documented withdrawal path with a stated delay; a forced-inclusion or escape hatch present for L2s; a live, permissionless proof system; probabilistic, economic, and deterministic finality stated separately rather than conflated.
**Status**: Gap with action
**If Not Found — Gap Action**: Name the undocumented mechanic (finality model and lag, reorg history, withdrawal path and delay, forced-inclusion availability, proof-system maturity, or MEV profile) and request it from the chain foundation; flag an absent escape hatch, withdrawal mechanics dependent entirely on an honest sequencer, or probabilistic finality without bounded reorg depth as critical conditions (cross-ref SC11 and SC13).
**Source / Precedent**: Polygon 2022: a reorg deeper than common finality assumptions reorganised more than a hundred blocks, retroactively rewriting positions that had assumed finality at thirty blocks.
**Criterion ID(s)**: 13.4, RF45, SC11, SC13
