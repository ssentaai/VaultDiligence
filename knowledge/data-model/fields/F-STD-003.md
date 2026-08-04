# F-STD-003

**Field ID**: F-STD-003
**Category**: Party Standing
**Sub-Category**: Entity Structure
**Field Name**: Ratable-Parent Resolution
**What to Collect / Question to Answer**: For each yield-critical party, resolve its named operating entity to its ultimate ratable parent (operating subsidiary -> rated group parent), recording the entity chain and the as-of-date. The named operating entity is often thin while the parent is what is rated and what backs it, so the rating and standing (F-STD-002 / 004 / 005) must be read against the entity that actually carries them.
**Data Type**: Structured (operating entity -> intermediate entities -> ultimate parent; LEI per node; as-of-date)
**Vault Types**: ALL (assessed only for parties flagged yield-critical in F-STD-001; N/A for parties not so flagged)
**Collection Tier**: T2
**Pillar(s)**: P18
**Primary Source**: GLEIF LEI records — direct and ultimate parent relationships (gleif-lei source)
**Fallback Source**: OpenCorporates registry; UK Companies House; party corporate-structure disclosure
**Evidence Pathway**: Inspection-validatable: look up the operating entity's LEI in the GLEIF registry and follow its direct/ultimate parent relationships to the rated parent; record each node and the date. This field wires the gleif-lei source's parent-relationship capability, previously unconsumed by any field.
**Institutional Standard**: The operating-entity-to-ultimate-parent chain is resolved and dated from the entity registry, so that credit rating and financial standing are read against the entity that carries them rather than the thin operating name.
**Status**: Gap with action
**If Not Found — Gap Action**: Parent chain resolved and dated from GLEIF: E. Resolved from a fallback registry only: E(P). Parent relationship exists but is undisclosed or not in GLEIF: G2 or G3 (state which) — the party's true credit backing cannot be located. Party not flagged yield-critical: N/A.
**Source / Precedent**: an internal analysis (2026-07-08): the gleif-lei source advertises direct/ultimate parent relationships but no field consumed it; follow-to-ratable-parent was net-new. Example: the CLO fund investment manager -> the CLO fund manager parent (the rated parent).
**Criterion ID(s)**: 18.3 (P18 Party Standing)
