# F-CHN-001

**Field ID**: F-CHN-001
**Category**: Chain
**Sub-Category**: Evaluation Gate
**Field Name**: Chain Evaluation Gate
**What to Collect / Question to Answer**: Does a completed chain-level evaluation exist for every chain in the vault's deployment and dependency set, dated before the asset-level conclusions that depend on it, and current within the quarterly cadence and any out-of-cycle material-event refresh?
**Data Type**: Enum (present-current / present-stale / absent) + reference to each chain evaluation on record + date
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P13
**Primary Source**: VaultDiligence chain-evaluation record for each chain in scope (F-CHN-002 through F-CHN-010 completed set); deployment manifest naming every chain the vault and its dependency chains run on
**Fallback Source**: Vault documentation and contract deployment addresses confirming which chains the vault and its dependencies are deployed on
**Evidence Pathway**: Inspection-validatable: enumerate the vault's contract addresses and dependency chains on-chain, then confirm a completed chain evaluation (F-CHN-002 to F-CHN-010) exists on record for each, dated before the asset-level findings.
**Institutional Standard**: A chain evaluation is on record for every chain in scope, current within the cadence, completed before any asset-level conclusion that depends on it; re-run quarterly and out-of-cycle on a halt, reorg, governance compromise, or major ecosystem participant exit.
**Status**: Gap with action
**If Not Found — Gap Action**: Name each chain in the deployment and dependency set lacking a current chain evaluation, and state that every asset-level finding on that deployment is provisional until the chain evaluation is completed; commission the missing chain evaluation before relying on any asset-level conclusion.
**Source / Precedent**: a published protocol risk framework, 9 Jun 2026, Layer 4 §4.1: chain-risk evaluation precedes asset and bridging evaluation; a chain that does not pass this layer is not a candidate for deployment, and existing deployments are re-evaluated quarterly and out-of-cycle on halt, reorg, governance compromise, or major participant exit.
**Criterion ID(s)**: 13.1
**Registered Sources (Fix 70)**: l2beat-chain-risk, l2beat-scaling-risk
