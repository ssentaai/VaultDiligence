# F-CUR-018

**Field ID**: F-CUR-018
**Category**: Curator
**Sub-Category**: Venue Parameter Authority
**Field Name**: Venue Parameter-Authority Split
**What to Collect / Question to Answer**: For every venue the risk control operator operates on, which risk parameters (supply caps, borrow caps, LLTV / liquidation threshold, oracle route, market configuration) are protocol- or governance-controlled versus directly curator-controlled? Classify each venue {protocol-governed, curator-governed, hybrid} and name the per-parameter owner.
**Data Type**: Structured (per venue: authority class + per-parameter owner)
**Vault Types**: ALL (curator-managed; N/A for unmanaged/immutable vaults with no active Risk Control Operator — gate off F-ROL-001 Risk Control Operator, do not assume the curator fills it, state why)
**Collection Tier**: T2
**Pillar(s)**: P14
**Primary Source**: Protocol documentation of governance-controlled parameters; on-chain read of who holds parameter-setting roles; risk control operator disclosure of curator-controlled parameters
**Fallback Source**: Risk Control Operator DDQ response mapping parameters to owners per venue
**Evidence Pathway**: Inspection-validatable: read on-chain which address/role can set each parameter at each venue; corroborate against protocol governance docs to classify protocol-governed vs curator-governed.
**Institutional Standard**: Each venue is classified by where parameter authority sits, per parameter, so it is unambiguous whether curator competence or protocol governance is the binding control on any given setting — e.g. Aave/Kamino protocol-governed vs Euler/Morpho curator-governed.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the parameter-setting roles on-chain per venue and classify each parameter's owner. If a venue with material exposure has undisclosed or unknown authority: G2 — request the risk control operator's authority map and confirm on-chain.
**Source / Precedent**: Concept surfaced by the risk-infrastructure provider methodology (pp.1, 7, venue design split); validated on first principles. Extends existing coverage — cross-reference F-CTR-007 (parameter change authority), F-CUR-008 (parameter change log), P2.8 (automated allocation policy).
**Criterion ID(s)**: 14.2 (cross-ref F-CTR-007, F-CUR-008, P2.8)
