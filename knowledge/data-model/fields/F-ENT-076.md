# F-ENT-076

**Field ID**: F-ENT-076
**Category**: Entity
**Sub-Category**: Service Provider Assurance
**Field Name**: Legal Counsel — Named Provider in SP Register
**What to Collect / Question to Answer**: Is external legal counsel identified as a named, registered service provider in the service-provider register (distinct from legal opinions that counsel may have authored)?
**Data Type**: Text (firm name) + Boolean (registered)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-4, VT-8)
**Collection Tier**: T3
**Pillar(s)**: P1
**Primary Source**: Service-provider register / offering memorandum service-provider schedule naming the law firm
**Fallback Source**: Fund administrator confirmation; engagement letter with the law firm (cross-ref F-ENT-075)
**Evidence Pathway**: Third-party-evidenced: inspect the service-provider register or offering-memorandum schedule for a named law firm engaged as ongoing legal counsel, distinct from the authorship line on any one-off legal opinion.
**Institutional Standard**: Good practice is a specifically named law firm registered as ongoing legal counsel in the service-provider register, corroborated by an executed engagement; sourcing only a legal opinion's authorship without a registered standing-counsel relationship leaves no identified party to advise the structure between events.
**Status**: Gap with action
**If Not Found — Gap Action**: Identify the law firm named as ongoing legal counsel in the service-provider register. If only legal opinions (F-LEG-011/016) name a firm but no standing counsel is registered: G2 — state that ongoing legal counsel is not registered as a named provider and request confirmation. If no legal counsel is engaged: G3.
**Source / Precedent**: an operational due-diligence checklist: the tree sources legal opinions (F-LEG-011/016) but not legal counsel as a registered service provider — the checklist treats counsel as a named entry in the service-provider domain that decides the mandate.
**Criterion ID(s)**: 0.2, 1.4
