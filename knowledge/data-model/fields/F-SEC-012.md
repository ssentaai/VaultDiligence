# F-SEC-012

**Field ID**: F-SEC-012
**Category**: Security
**Sub-Category**: Infrastructure
**Field Name**: Off-Chain Infrastructure Pentest / Security Review
**What to Collect / Question to Answer**: Has off-chain infrastructure been explicitly in scope for any security review, pentest, or audit? Firm name, date, scope statement. Resolv precedent: 18 audits, zero covered AWS KMS.
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T3
**Primary Source**: Audit reports — scope section
**Fallback Source**: Pentest reports
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Read audit scope sections explicitly. Confirm off-chain infra in or out of scope. If out of scope: flag and request dedicated review.
**Criterion ID(s)**: 7.16
**Registered Sources (Fix 70)**: defisafety-process-reviews (candidate)
**v54 Refinement (gap audit 2026-06-12)**: Record audit recency against the last material governance or collateral change (an audit predating a material change is effectively stale), and capture the explicit out-of-scope exclusions list for each review. Source: Buzko — Drift passed two audits predating the CVT/governance changes.
**Red Flag ID(s)**: RF41