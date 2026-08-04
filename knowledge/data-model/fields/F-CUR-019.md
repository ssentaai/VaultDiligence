# F-CUR-019

**Field ID**: F-CUR-019
**Category**: Curator
**Sub-Category**: Parameter Discipline
**Field Name**: Curator Control Exercised via Documented Policy
**What to Collect / Question to Answer**: Where the risk control operator holds direct parameter control (curator-governed venues per F-CUR-018), is that control exercised through a documented internal policy — approved models behind LLTV / cap settings, a parameter change log, and a review/approval step separating the party that proposes from the party that commits — rather than unconstrained discretion?
**Data Type**: Text (policy description) + Boolean (model-vetting, change log, approval separation present)
**Vault Types**: ALL (curator-managed; N/A for unmanaged/immutable vaults with no active Risk Control Operator — gate off F-ROL-001 Risk Control Operator, do not assume the curator fills it, state why)
**Collection Tier**: T2
**Pillar(s)**: P14
**Primary Source**: Risk Control Operator internal parameter-setting policy; model-vetting records; parameter change log
**Fallback Source**: Risk Control Operator DDQ response describing model design -> risk approval -> production implementation path
**Evidence Pathway**: Third-party-evidenced: obtain the risk control operator's parameter-setting policy, evidence that models are vetted before a value is set, the change log, and the proposer/committer separation.
**Institutional Standard**: Direct curator control is governed by documented policy: model-vetting before a value is set, a maintained parameter change log, and an approval step separating the analyst who proposes from the party who commits.
**Status**: Gap with action
**If Not Found — Gap Action**: Ask for the parameter-setting policy, model-vetting artifacts, and change log. If direct control exists with no documented policy or change log: G3 — the risk control operator must document its parameter-governance policy. If policy exists but no evidence it is followed: E(P).
**Source / Precedent**: Concept surfaced by the risk-infrastructure provider methodology (pp.7-8, research-design -> risk-approval -> operational-control path); validated on first principles. Cross-reference F-CUR-018, F-CUR-008.
**Criterion ID(s)**: 14.3 (cross-ref F-CUR-018, F-CUR-008)
