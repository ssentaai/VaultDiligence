# F-GOV-022

**Field ID**: F-GOV-022
**Category**: Governance
**Sub-Category**: Board Oversight
**Field Name**: Board Composition & Committee Structure
**What to Collect / Question to Answer**: What is the board's composition (number of directors, independent versus manager-affiliated), what committees exist (audit, risk, valuation), and are board minutes maintained?
**Data Type**: Text (composition + committees) + Number (director count, independent count)
**Vault Types**: Exposure in {private-credit,structured-credit} OR Management=delegated-offchain-IM OR Structure=tranched OR (Exposure in {equities,corporate-fixed-income,sovereign-fixed-income} AND venue=tradfi-primary)  (derived from VT-N; original "Vault Types" value: VT-3, VT-3a, VT-4, VT-8)
**Collection Tier**: T3
**Pillar(s)**: P1
**Primary Source**: Board charter / constitutional documents listing directors and committees; offering memorandum governance section
**Fallback Source**: Fund administrator confirmation of board roster; company registry director filings; board minutes
**Evidence Pathway**: Third-party-evidenced: inspect the board charter and constitutional documents for the director roster (with independence status per director), the committee structure, and confirmation that board minutes are kept; cross-check director identities against the company registry.
**Institutional Standard**: Good practice is a documented board with a meaningful proportion of independent directors, defined committees (audit, risk, valuation) with charters, and maintained board minutes; a board of manager-affiliated directors only, with no committee structure or minutes, provides no independent governance layer. This is traditional-fund governance and must not be conflated with on-chain timelock governance (F-GOV-005/006/007).
**Status**: Gap with action
**If Not Found — Gap Action**: Obtain the board roster, independence status per director, committee structure, and confirmation that minutes are kept. If composition is partially sourced (F-LEG-017 names independent directors) but committee structure and minutes are not: G2 — name the missing items and the document required (board charter / minutes). If no board or committee structure exists: G3.
**Source / Precedent**: an operational due-diligence checklist: traditional-fund board composition, committee structure, and minutes are a service-providers/governance ODD domain item; the tree sources the independent-director question (F-LEG-017) and conflict-of-interest framework (F-GOV-020) but has no field for board composition, committee structure, or minutes.
**Criterion ID(s)**: 1.4
