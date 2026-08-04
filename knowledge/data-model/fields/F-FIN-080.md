# F-FIN-080

**Field ID**: F-FIN-080
**Category**: Financial
**Sub-Category**: Reserve Attestation
**Field Name**: Reserve Attestation Cadence and Named Auditor
**What to Collect / Question to Answer**: Are the reserves regularly audited or attested by a recognised auditing firm, by whom specifically, and at what frequency, such that the staleness of the assurance can be measured against the present date?
**Data Type**: Text (named firm) + Enum cadence (real-time / daily / monthly / quarterly / annual / ad hoc)
**Vault Types**: ALL
**Collection Tier**: T2
**Pillar(s)**: P9
**Primary Source**: Most recent attestation/audit report on the reserves (PDF) naming the firm and stating the attestation date
**Fallback Source**: Protocol proof-of-reserves dashboard linking to the attestor, or operator disclosure of the engaged firm
**Evidence Pathway**: Third-party-evidenced: identify the named auditing firm and retrieve the dated attestation report; confirm the attestation date and recurrence cadence from the report text itself.
**Institutional Standard**: Reserves are attested by a named, recognised auditing firm on a cadence sized to the volatility of the backing, with the most recent dated report publicly retrievable; the attestor is identified by name rather than referenced generically.
**Status**: Gap with action
**If Not Found — Gap Action**: Name the auditing firm and request the most recent attestation report with its date and the engagement's recurrence; if only an aggregate proof-of-reserves number exists with no named attestor, classify as G2 and state that the operator must produce a named-firm attestation report.
**Source / Precedent**: Steakhouse Financial stablecoin-issuer DDQ v1.0, section 4.11: 'Are the reserves regularly audited by a recognized auditing firm (by whom?) ... in what frequency?' Frequency plus attestor identity determines the staleness of assurance.
**Criterion ID(s)**: 9.10
**Registered Sources (Fix 70)**: an issuer-disclosure source
