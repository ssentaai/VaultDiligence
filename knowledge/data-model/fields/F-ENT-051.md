# F-ENT-051

**Field ID**: F-ENT-051
**Category**: Entity
**Sub-Category**: Fund Administrator
**Field Name**: Independent NAV Calculation Agent
**What to Collect / Question to Answer**: Is there a third-party independent NAV calculation agent separate from both operator and oracle?
**Data Type**: Text
**Vault Types**: Exposure in {private-credit,structured-credit} OR Structure=tranched OR Structure in {leveraged,looped} OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3,VT-4,VT-7,VT-8)
**Collection Tier**: T3
**Primary Source**: Fund prospectus / Kaiko / administrator disclosure
**Pillar(s)**: P3
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: C
**If Not Found — Gap Action**: Kaiko offers registered benchmark provider NAV calculation services. Absence = flag for institutional DD.
**Criterion ID(s)**: 3.1
**v54 Refinement (gap audit 2026-06-12)**: Confirm a reconciliation step is actually present: that an independent party reconciles reserves or holdings against reported balances (not merely that a NAV agent is named), with tooling and oversight stated. Source: an ODD source-ODD; Steakhouse section 4.5. Cross-ref F-FIN-079, F-OPS-036.
