# F-CUR-025

**Field ID**: F-CUR-025
**Category**: Curator
**Sub-Category**: Escalation Apparatus
**Field Name**: Escalation, SLA & Incident Machinery
**What to Collect / Question to Answer**: What escalation apparatus does the risk control operator operate: a defined incident-report SLA window on a breach (for example a formal incident report within a stated number of hours), a committee with authority to reduce or unwind positions, and incident machinery (paging, war-room / coordinated response)? Confirm authority to act, not only to notify.
**Data Type**: Structured (SLA window; committee unwind authority Boolean; incident machinery named)
**Vault Types**: ALL (curator-managed; N/A for unmanaged/immutable vaults with no active Risk Control Operator — gate off F-ROL-001 Risk Control Operator, do not assume the curator fills it, state why)
**Collection Tier**: T2
**Pillar(s)**: P15
**Primary Source**: Risk Control Operator escalation policy naming severity tiers, incident-report SLA, committee authority, and incident-response tooling
**Fallback Source**: Risk Control Operator DDQ response; evidence of a prior incident handled under the SLA
**Evidence Pathway**: Third-party-evidenced: obtain the risk control operator's escalation policy and confirm the incident-report SLA window, the committee's position-reduction/unwind authority, and the incident-response machinery; corroborate with a prior incident record if one exists.
**Institutional Standard**: A graded escalation path exists with a stated incident-report window on breaches, a committee holding position-reduction/unwind authority, and named incident-response machinery; escalation ends in action, not just acknowledgement.
**Status**: Gap with action
**If Not Found — Gap Action**: Ask for the escalation policy and evidence of the committee's unwind authority. If escalation can notify but holds no authority to reduce/unwind, or has no stated incident-report window: critical condition — detection without authority to act is not a control.
**Source / Precedent**: Concept surfaced by the risk-infrastructure provider methodology (pp.15, 17, escalation map: Info/Warning/Breach/Critical with a 24h incident-report SLA and Risk-Committee unwind authority); validated on first principles. Cross-reference F-OPS-005 (incident response SLA), F-OPS-033 (pre-agreed incident communication).
**Criterion ID(s)**: 15.5 (cross-ref F-OPS-005, F-OPS-033)
