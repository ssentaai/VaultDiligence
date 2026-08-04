# F-PRJ-011

**Field ID**: F-PRJ-011
**Category**: Operations
**Sub-Category**: Project Gate
**Field Name**: Business-Continuity Plan
**What to Collect / Question to Answer**: Is there a documented business-continuity and disaster-recovery plan covering loss of premises, key personnel, primary service providers, and core infrastructure, and has it been tested within a stated period?
**Data Type**: Text / Y-N (plan exists, last tested date, scenarios covered)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-8)
**Collection Tier**: T3
**Pillar(s)**: P0
**Primary Source**: Operator business-continuity / disaster-recovery policy document
**Fallback Source**: SOC-2 Type II report business-continuity section or fund administrator's BCP attestation
**Evidence Pathway**: Third-party-evidenced: obtain the dated BCP/DR document and the most recent test record, corroborated by the SOC-2 Type II business-continuity control description from the named auditor.
**Institutional Standard**: Good looks like a written, dated business-continuity and disaster-recovery plan that names the scenarios it covers (premises, personnel, service-provider, and infrastructure loss), assigns recovery responsibilities, and records a test within a defined recency window — distinct from on-chain key-compromise incident response, which is covered separately.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the BCP/DR document and its last test date from the operator COO/administrator. If only on-chain incident response exists (F-PRJ-007) with no enterprise BCP, classify as G2 and name the entity expected to hold the plan.
**Source / Precedent**: an operational due-diligence checklist (Cayman/CIMA fund administrator, LEI [LEI redacted]), Risk/Operations domain: flags business continuity and disaster-recovery policy as a required ODD document, noting 'most ODD failures are documentation, not substance.'
**Criterion ID(s)**: 0.3
