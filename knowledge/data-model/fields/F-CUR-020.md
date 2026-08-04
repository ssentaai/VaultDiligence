# F-CUR-020

**Field ID**: F-CUR-020
**Category**: Curator
**Sub-Category**: Execution & Custody
**Field Name**: Execution/Oversight Separation & Key Custody
**What to Collect / Question to Answer**: Is execution separated from risk oversight, and what governs the execution surface? Capture: executor type (application / on-chain bot / keeper / manual), signer architecture, permission scopes per action, timelock, kill-switch authority, and change-management on any execution agent or bot. Where bots execute outside the risk/monitoring layer, state the boundary and its controls explicitly.
**Data Type**: Structured (executor type, signer scheme, permission scopes, timelock, kill-switch, change-mgmt evidence)
**Vault Types**: ALL (curator-managed; N/A for unmanaged/immutable vaults with no active Risk Control Operator — gate off F-ROL-001 Risk Control Operator, do not assume the curator fills it, state why)
**Collection Tier**: T2
**Pillar(s)**: P14
**Primary Source**: On-chain read of signer/role architecture and timelocks on execution contracts; risk control operator disclosure of bot permission scopes and change-management
**Fallback Source**: Risk Control Operator operational-security documentation; bot deployment and key-custody description
**Evidence Pathway**: Inspection-validatable: read the signer architecture, permission scopes, and timelocks on execution contracts on-chain; Third-party-evidenced: obtain the risk control operator's bot change-management and kill-switch documentation for logic that executes off the risk-app.
**Institutional Standard**: Execution is documented as separate from oversight, with institutional key custody, scoped permissions, timelocks, a kill switch, and change-management on execution logic; where bots execute outside the risk/monitoring layer, that boundary and its controls are explicit.
**Status**: Gap with action
**If Not Found — Gap Action**: Read execution-contract signers/timelocks on-chain and request the bot permission-scope and change-management docs. If bots execute outside the risk app with undisclosed signer/kill-switch/change-management: I (investigate) — highest-priority open item; classify G2 until the controls are evidenced.
**Source / Precedent**: Concept surfaced by the risk-infrastructure provider methodology (pp.8, 11, 19 and Source Note 4 — bots execute outside the Risk Application); validated on first principles. Cross-reference F-CTR-004 (timelock), F-CTR-015 (custody chain), F-CTR-016 (guardian scope), F-CTR-027 (per-action timelock), F-CTR-028 (multisig threshold), F-OPS-011 (signer identity).
**Criterion ID(s)**: 14.4 (cross-ref F-CTR-004, F-CTR-015, F-CTR-016, F-CTR-027, F-CTR-028, F-OPS-011; RF03, RF42)
