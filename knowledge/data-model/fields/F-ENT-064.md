# F-ENT-064

**Field ID**: F-ENT-064
**Category**: Entity
**Sub-Category**: Service Provider Assurance
**Field Name**: Audit Management Letters
**What to Collect / Question to Answer**: Has the financial auditor issued a management letter identifying control-deficiency findings beyond the audit opinion, and what deficiencies (and remediation status) does it record?
**Data Type**: Document + Text (enumerated findings)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-4, VT-8)
**Collection Tier**: T3
**Pillar(s)**: P1
**Primary Source**: Auditor management letter / letter to management accompanying the most recent audited financial statements
**Fallback Source**: Fund administrator (an ODD source or equivalent); audit committee minutes recording deficiency findings
**Evidence Pathway**: Third-party-evidenced: obtain the named financial auditor's management letter accompanying the audited statements (the control-deficiency annex, not just the clean opinion) and inspect each enumerated finding and its remediation status.
**Institutional Standard**: Good practice is a management letter on file from the named auditor with each control-deficiency finding enumerated, severity-classified, and tracked to a dated remediation; an unqualified opinion with no accompanying management letter, or a refusal to disclose it, leaves the control-environment findings unobservable to the allocator.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the management letter accompanying the most recent audited financial statements. If the auditor issued one but it is withheld: G2 — name the auditor and the period, state the letter exists and is required to read control-deficiency findings. If no management letter was ever issued: G3 — operator must obtain and publish the control-deficiency findings.
**Source / Precedent**: an operational due-diligence checklist: audit management letters carry control-deficiency findings, not just the opinion; the checklist's thesis is that 'most ODD failures are documentation, not substance' — the opinion can be clean while the management letter records material control gaps.
**Criterion ID(s)**: 8.4, 1.4
