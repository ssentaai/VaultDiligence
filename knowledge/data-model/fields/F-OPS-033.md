# F-OPS-033

**Field ID**: F-OPS-033
**Category**: Operations
**Sub-Category**: Incident Response
**Field Name**: Pre-Agreed Incident Communication Baseline
**What to Collect / Question to Answer**: Has the issuer/operator identified a contact point and escalation path that has been tested, committed to 24/7 reachability, and committed to pre-notifying the allocator of material changes before they go live?
**Data Type**: Text (contact + escalation path) + Boolean (tested, 24/7, pre-notification committed)
**Vault Types**: ALL
**Collection Tier**: T2
**Pillar(s)**: P8
**Primary Source**: Operator incident-communication policy / service agreement clause naming contact point, escalation path, and 24/7 reachability commitment
**Fallback Source**: Operator DDQ response; evidence of a prior tested escalation drill or incident notification
**Evidence Pathway**: Third-party-evidenced: obtain the operator's incident-communication commitment naming the contact point and escalation path, evidence that the escalation path has been tested (drill record or prior incident), the 24/7-reachability commitment, and the pre-notification-of-material-changes commitment.
**Institutional Standard**: Good practice is a named issuer contact point and escalation path that has been tested, 24/7 reachability, and a standing commitment to pre-notify the allocator of material changes before they go live; incident loss is bounded by how fast the allocator hears and can act, so an untested or absent escalation path leaves that window unquantifiable.
**Status**: Gap with action
**If Not Found — Gap Action**: Ask the operator for the incident contact point, escalation path, evidence it has been tested, the 24/7-reachability commitment, and the pre-notification commitment. If named but never tested: E(P) — state the escalation path is untested. If no contact/escalation commitment exists: G3 — operator must establish and document one.
**Source / Precedent**: Aave–LlamaRisk asset risk framework, 9 June 2026, section 1.12: 'Issuer contact point and escalation path identified and tested... 24/7 reachability... Commitment to pre-notify Aave teams of material changes before they go live.' Incident loss is bounded by how fast the allocator hears and can act.
**Criterion ID(s)**: 8.3
