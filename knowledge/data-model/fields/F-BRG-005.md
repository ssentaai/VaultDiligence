# F-BRG-005

**Field ID**: F-BRG-005
**Category**: Bridging
**Sub-Category**: Authority Timelocks
**Field Name**: Bridge Authority Timelocks
**What to Collect / Question to Answer**: Is each of the five bridge authority classes — ownership transfer, verifier-set change, library upgrade, rate-limit change, and mint/burn authority grant — gated by a timelock on every route, with a delay long enough to permit mitigating action before execution (instantaneous or sub-hour delays being below baseline)?
**Data Type**: Duration (per authority class, per route)
**Vault Types**: ALL (bridge-crossing vaults; N/A single-chain, state why)
**Collection Tier**: T2
**Pillar(s)**: P12
**Primary Source**: On-chain read of the timelock delay configured on each of the five bridge authority classes on every route
**Fallback Source**: Issuer/vendor governance documentation enumerating the bridge authorities and their timelock parameters (confirm against contract state)
**Evidence Pathway**: Inspection-validatable — read the timelock contracts gating ownership transfer, verifier-set change, library upgrade, rate-limit change, and mint/burn authority grants on each route and confirm the configured delay.
**Institutional Standard**: Timelocks gate all five bridge authority classes on every route, each with an observation-window delay sufficient for mitigating action before execution. Absence of a timelock on any bridge authority is a critical condition.
**Status**: Gap with action
**If Not Found — Gap Action**: Enumerate the five bridge authority classes per route and read the configured timelock delay for each. For any authority with no timelock or a sub-hour delay, record RF44 critical condition and request the issuer place an observation-window delay on it.
**Source / Precedent**: Drift, Apr 2026: the governance migration path carried zero timelock weeks before the $285M exploit — authority-without-observation-window is the same control failure class at bridge level.
**Criterion ID(s)**: 12.5, RF44 (cross-ref F-CTR-016)
**Registered Sources (Fix 70)**: l2beat-scaling-risk
