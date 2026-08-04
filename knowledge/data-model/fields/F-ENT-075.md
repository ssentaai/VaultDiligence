# F-ENT-075

**Field ID**: F-ENT-075
**Category**: Entity
**Sub-Category**: Service Provider Assurance
**Field Name**: Executed Service-Provider Agreements on File
**What to Collect / Question to Answer**: Are executed (signed, countersigned) service-provider agreements on file with the administrator, custodian, auditor, and legal counsel, evidencing each engagement beyond merely naming the provider?
**Data Type**: Document set (executed agreement per provider) + Boolean per provider
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-4, VT-8)
**Collection Tier**: T3
**Pillar(s)**: P1
**Primary Source**: Executed engagement letters / service agreements for administrator, custodian, auditor, legal counsel
**Fallback Source**: Fund administrator (an ODD source or equivalent) confirmation that executed agreements are held; offering memorandum service-provider schedule
**Evidence Pathway**: Third-party-evidenced: obtain or have the administrator confirm the executed engagement letter for each named service provider (administrator, custodian, auditor, legal counsel), inspecting that each is signed and current rather than only named in marketing.
**Institutional Standard**: Good practice is a complete set of executed, current engagement agreements on file for every material service provider, confirmable by the administrator; naming a provider in documentation without an executed agreement leaves the relationship unevidenced and potentially terminable or never formed.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the executed agreement for each named service provider (administrator, custodian, auditor, legal counsel). For any provider named but with no executed agreement produced: G2 — name the provider and the missing agreement. If no executed agreements exist for a claimed relationship: G3 — operator must execute and file them.
**Source / Precedent**: an operational due-diligence checklist: the tree names service providers but does not require evidence of an executed agreement — a documentation gap exactly matching the checklist thesis that 'most ODD failures are documentation, not substance.'
**Criterion ID(s)**: 0.2, 1.4
