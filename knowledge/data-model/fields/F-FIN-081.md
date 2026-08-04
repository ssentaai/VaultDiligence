# F-FIN-081

**Field ID**: F-FIN-081
**Category**: Financial
**Sub-Category**: Loss Isolation
**Field Name**: Bad-Debt Isolation and Recapitalization Mechanism
**What to Collect / Question to Answer**: In the event of a capital shortfall, what enforceable mechanisms exist to isolate the loss from unaffected positions and to restore protocol capital, and are those mechanisms contractually or contractually-and-on-chain enforceable rather than discretionary?
**Data Type**: Text (enumerated mechanisms + enforceability statement)
**Vault Types**: ALL
**Collection Tier**: T3
**Pillar(s)**: P9
**Primary Source**: Protocol documentation describing isolation/recapitalization mechanics + governing legal terms
**Fallback Source**: On-chain inspection of isolation primitives (isolated markets, per-vault accounting, insurance-fund contract) corroborated by operator disclosure
**Evidence Pathway**: Inspection-validatable: inspect the contract for isolation primitives (isolated markets, per-position accounting, insurance/backstop fund address and balance) and confirm the recapitalization path; pair with the governing document that makes the mechanism enforceable.
**Institutional Standard**: A capital shortfall is contained to the affected positions by an enforceable isolation mechanism, and a named, funded recapitalization path (insurance fund, backstop, equity injection commitment) exists with its size disclosed; losses are not silently socialised across unaffected depositors.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the enforceable isolation and recapitalization mechanism description and the size and address of any backstop fund; if loss isolation is undocumented or bad debt would socialise across unaffected positions, classify as G2 with RF35 noted and state the document (loss-allocation policy) required.
**Source / Precedent**: Steakhouse Financial stablecoin-issuer DDQ v1.0, section 4.9: 'In the event of a capital shortfall, what enforceable mechanisms exist to isolate the losses and restore the protocol capital?' Contained versus socialized bad debt is a core loss-severity determinant.
**Criterion ID(s)**: 9.4, RF35
