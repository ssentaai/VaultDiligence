# F-STD-002

**Field ID**: F-STD-002
**Category**: Party Standing
**Sub-Category**: Credit Standing
**Field Name**: Party Credit Rating
**What to Collect / Question to Answer**: For each yield-critical party (or its ratable parent per F-STD-003), what is its current independent corporate credit rating? Record the rating, the issuing agency (S&P / Moody's / Fitch / KBRA) named, and the rating's as-of-date. This is DISTINCT from F-RAT, which points to a rating of the token/fund, not the party. A crypto-native or private party with no corporate credit rating has that absence recorded as the finding — do not infer a rating or substitute the token rating.
**Data Type**: Structured (party -> agency -> rating -> as-of-date)
**Vault Types**: ALL (assessed only for parties flagged yield-critical in F-STD-001; N/A for parties not so flagged)
**Collection Tier**: T2
**Pillar(s)**: P18
**Primary Source**: Rating agency public rating page or rating-action release (S&P / Moody's / Fitch / KBRA) for the party or its rated parent
**Fallback Source**: Party investor-relations disclosure citing its current rating; the registered rating sources on F-RAT-006 (applied to the party, not the token)
**Evidence Pathway**: Third-party-evidenced: obtain the rating agency's current published rating for the party (or its parent per F-STD-003) and record the agency, rating, and date.
**Institutional Standard**: The party's current corporate credit rating is recorded from the rating agency with the agency named and the rating dated, or its absence is stated explicitly; the token rating (F-RAT) is never substituted for the party's own rating.
**Status**: Gap with action
**If Not Found — Gap Action**: Current rating recorded and dated from the agency: E. Rating known but not re-confirmed this session: E(P). Rating exists but is behind a paywall/subscription: G2. Party has no corporate credit rating where one would be expected for a party of its role: G3 — a finding (record the absence, do not infer soundness). Party not flagged yield-critical: N/A.
**Source / Precedent**: an internal analysis (2026-07-08): F-RAT-001..007 rate the token/fund, never the party; F-RAT-006 notes the tokenized CLO fund is unrated while the party (the CLO fund manager) carried a corporate rating.
**Criterion ID(s)**: 18.2 (P18 Party Standing)
