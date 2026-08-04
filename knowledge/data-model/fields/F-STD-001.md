# F-STD-001

**Field ID**: F-STD-001
**Category**: Party Standing
**Sub-Category**: Yield-Critical Designation
**Field Name**: Yield-Critical Party Flag
**What to Collect / Question to Answer**: Which named parties in this vault's stack are fundamental to generating or protecting the yield? Identify each by F-ROL ID (e.g. Investment Manager F-ROL-003, Sub-Advisor F-ROL-004, Custodian F-ROL-007, and any credit-critical counterparty), state the reason each is yield-critical, and record the as-of-date of the determination. This is a DISTINCT judgment from F-FIN-083: F-FIN-083 flags a counterparty by exposure size and functioning-dependency; F-STD-001 flags a party by its role in generating or protecting the yield. A party may be one, the other, or both. Cross-reference F-FIN-083 for the exposure view but derive this flag independently — do not re-label F-FIN-083.
**Data Type**: Structured (list of F-ROL IDs -> reason yield-critical -> as-of-date)
**Vault Types**: ALL (where the vault has one or more delegated yield parties; N/A for a vault with no delegated yield party — e.g. a fully immutable protocol vault — which is itself a finding, state why)
**Collection Tier**: T2
**Pillar(s)**: P18
**Primary Source**: Fund offering memorandum / strategy documentation identifying the party that generates or protects the yield; the F-ROL role registry for this vault
**Fallback Source**: Operator disclosure; on-chain strategy mapping; the exposure view in F-FIN-083 (cross-reference only, not a substitute)
**Evidence Pathway**: Third-party-evidenced: obtain the fund/strategy documentation naming the yield-generating and yield-protecting parties and map each to its F-ROL ID; record the reason and date. Derived independently of F-FIN-083's exposure register.
**Institutional Standard**: The set of yield-critical parties is stated by F-ROL ID with the reason each is fundamental to the yield and an as-of-date, derived as its own judgment rather than re-labelled from the exposure-materiality register (F-FIN-083). This flag gates F-STD-002 through F-STD-007: only flagged parties receive a standing assessment.
**Status**: Gap with action
**If Not Found — Gap Action**: Yield-critical parties identified and mapped to F-ROL IDs with dated reasons: E. Identified but unverified this session: E(P). The party exists but which party generates or protects the yield is undisclosed: G3 — a finding (the dominant yield party cannot be assessed). No delegated yield party in this vault type: N/A with a stated reason.
**Source / Precedent**: an internal analysis (2026-07-08): the framework flagged counterparties by exposure (F-FIN-083) but never by yield-generation; the yield-critical flag is the gate for the P18 standing dimension.
**Criterion ID(s)**: 18.1 (P18 Party Standing)
