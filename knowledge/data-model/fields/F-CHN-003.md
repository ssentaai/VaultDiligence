# F-CHN-003

**Field ID**: F-CHN-003
**Category**: Chain
**Sub-Category**: Decentralisation
**Field Name**: Consensus / Sequencer Decentralisation
**What to Collect / Question to Answer**: For L2s, what is the sequencer model (single, shared, permissionless) and the documented path to permissionless sequencing; for L1s, what is the validator count, identity, geographic distribution, entry/exit/slashing mechanics and stake concentration; and for both, what is the client diversity and infrastructure concentration?
**Data Type**: Structured text (sequencer model + path; validator count/identity/distribution; client diversity; jurisdiction/cloud/RPC concentration; fee-revenue concentration)
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P13
**Primary Source**: Chain documentation on sequencer/validator architecture; on-chain validator registry or sequencer contract; published decentralisation roadmap; client-distribution telemetry (e.g. clientdiversity dashboards)
**Fallback Source**: Third-party decentralisation trackers (L2BEAT sequencer/proposer status, validator-distribution explorers)
**Evidence Pathway**: Inspection-validatable: read the sequencer or validator-set contract on-chain for operator identity, count, and stake distribution; Third-party-evidenced: cite L2BEAT or equivalent for sequencer model and forced-inclusion status, and client-diversity telemetry for single-client dependency.
**Institutional Standard**: No single-sequencer dependence without documented escape mechanics; validator concentration below honest-majority thresholds in any single entity or jurisdiction; multi-client consensus rather than single-client dependency.
**Status**: Gap with action
**If Not Found — Gap Action**: Name the undisclosed dimension (sequencer model and permissionless path, validator identity/distribution, slashing mechanics, client diversity, or infrastructure concentration) and request it from the chain foundation; flag a single sequencer with no forced-inclusion path, validator concentration above honest-majority threshold in one entity or jurisdiction, or single-client dependency as critical conditions (cross-ref SC11).
**Source / Precedent**: Arbitrum sequencer outages (Dec 2021 and Jun 2022) halted transaction inclusion chain-wide; every position on the chain was frozen for the duration of the single-sequencer outage regardless of asset quality.
**Criterion ID(s)**: 13.3, RF45, SC11
**Registered Sources (Fix 70)**: l2beat-chain-risk, l2beat-scaling-risk
