# F-STD-004

**Field ID**: F-STD-004
**Category**: Party Standing
**Sub-Category**: Regulatory Standing
**Field Name**: Party Regulatory Standing — Current
**What to Collect / Question to Answer**: For each yield-critical party, what is its current regulatory registration/authorization and good standing (SEC / FCA / equivalent)? Record the regulator, the registration, the good-standing status, and the as-of-date. Cross-reference F-ENT-021 (investment-manager regulatory status), F-ENT-041 (custodian regulatory status), and F-CUS-004 (prime-broker regulatory standing) — those capture registration as static onboarding snapshots; this field adds the current, dated standing for the yield-critical party specifically.
**Data Type**: Structured (party -> regulator -> registration -> good-standing -> as-of-date)
**Vault Types**: ALL (assessed only for parties flagged yield-critical in F-STD-001; N/A for parties not so flagged)
**Collection Tier**: T2
**Pillar(s)**: P18
**Primary Source**: Regulator public register (SEC IAPD / EDGAR, FCA Financial Services Register, or equivalent) queried at assessment time
**Fallback Source**: Party disclosure of its licenses; the onboarding snapshots in F-ENT-021 / F-ENT-041 / F-CUS-004 (cross-reference)
**Evidence Pathway**: Third-party-evidenced / Inspection-validatable: query the regulator's public register for the party's current registration and good standing and record it with the date.
**Institutional Standard**: Current registration and good standing for the yield-critical party is recorded and dated from the regulator's public register, not carried forward from an onboarding-time snapshot.
**Status**: Gap with action
**If Not Found — Gap Action**: Current standing confirmed and dated from the regulator register: E. Registration known but current standing not re-confirmed this session: E(P). Register access restricted: G2. Party runs a regulated activity with no discoverable registration: G3 — a finding. Party not flagged yield-critical: N/A.
**Source / Precedent**: an internal analysis (2026-07-08): F-ENT-021 / F-ENT-041 and F-CUS-004 capture registration once, without a current/dated or change dimension for the delegated yield party.
**Criterion ID(s)**: 18.4 (P18 Party Standing)
