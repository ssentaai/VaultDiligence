# F-PRJ-012

**Field ID**: F-PRJ-012
**Category**: Security
**Sub-Category**: Project Gate
**Field Name**: Enterprise Infosec Policy
**What to Collect / Question to Answer**: Is there a documented enterprise information-security policy governing access control, data handling, vendor security, and personnel security across the organisation, beyond on-chain key management?
**Data Type**: Text / Y-N (policy exists, scope, last reviewed date)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-8)
**Collection Tier**: T3
**Pillar(s)**: P0
**Primary Source**: Operator enterprise information-security policy document
**Fallback Source**: SOC-2 Type II report security-control narrative or ISO 27001 certification from a named assessor
**Evidence Pathway**: Third-party-evidenced: obtain the written infosec policy and corroborate its controls against the SOC-2 Type II security section or an ISO 27001 certificate issued by a named certification body.
**Institutional Standard**: Good looks like a written enterprise information-security policy with a stated scope covering organisational access control, data classification and handling, vendor/third-party security, and personnel security, reviewed within a defined period and corroborated by an independent control attestation — broader than the on-chain key-compromise incident response captured elsewhere.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the enterprise infosec policy and its last-review date; corroborate against the SOC-2 Type II security narrative. If cyber posture is framed only as on-chain key compromise with no enterprise policy, classify as G2 and name the operator's security owner.
**Source / Precedent**: an operational due-diligence checklist (David Lloyd CEO, CIMA-regulated), Compliance/Risk domain: lists cyber and information-security policies as a required ODD document set, framing the gap as documentation discipline rather than substance.
**Criterion ID(s)**: 0.3
