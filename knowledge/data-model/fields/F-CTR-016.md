# F-CTR-016

**Field ID**: F-CTR-016
**Category**: Contract
**Sub-Category**: Emergency Authority
**Field Name**: Guardian Scope and Revocation Authority
**What to Collect / Question to Answer**: Beyond the simple emergency-pause flag (F-CTR-006), enumerate guardian/sentinel mechanisms with explicit scope. For each: (a) what actions the guardian can take (pause, revoke, freeze, recover, mint, burn), (b) whether the guardian's actions are time-bounded or permanent, (c) whether the guardian's actions can themselves be reverted by governance, (d) whether the guardian role is upgradeable. Per Egalite (May 2026): "guardian and sentinel mechanisms provide emergency intervention capabilities... without introducing new centralized control or allowing the response itself to be turned against users."
**Data Type**: Structured list — each entry: { authority_name, scope_actions, time_bounded: bool, reversible_by_governance: bool, role_upgradeable: bool }
**Vault Types**: ALL
**Collection Tier**: T2
**Primary Source**: On-chain enumeration of privileged roles (F-SEC-006) + smart contract code review of guardian functions
**Fallback Source**: Audit report describing emergency authority + operator disclosure
**Pillar(s)**: P7, P8
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: G2 if guardian mechanism exists but scope is undocumented. A guardian whose scope is not enumerated is functionally unbounded — state this as the finding.
**Criterion ID(s)**: 7.6, 8.4
**v54 Refinement (gap audit 2026-06-12)**: Capture the timelock as a graded, per-authority, per-chain security-config model (Aave/LlamaRisk section 1.6): sub-hour or instantaneous delay on any authority is below baseline, and per-governance-action coverage must include migration paths, not only proxy upgrades. Cross-ref F-CTR-027. Also record measured pause latency where an incident exists (cross-ref F-CTR-006).
**Red Flag ID(s)**: RF-CTL-002 (unbounded guardian authority)
