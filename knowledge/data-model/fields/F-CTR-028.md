# F-CTR-028

**Field ID**: F-CTR-028
**Category**: Smart Contract
**Sub-Category**: Governance Controls
**Field Name**: Multisig Threshold & Signer Independence
**What to Collect / Question to Answer**: What is the on-chain multisig threshold and signer count, and are the signers genuinely independent — distributed across distinct organisations, jurisdictions, and security environments rather than controlled by one party?
**Data Type**: Structured: { threshold, signer_count, meets_floor: bool, distinct_orgs, distinct_jurisdictions, distinct_security_envs, signer_independence_evidence }
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P7
**Primary Source**: On-chain: read the Safe/multisig contract for threshold and owner list, then attribute each signer address to a distinct organisation, jurisdiction, and security environment via documented signer identity
**Fallback Source**: Operator-published signer register naming each signer's organisation and jurisdiction, cross-checked against the on-chain owner set
**Evidence Pathway**: Inspection-validatable: read threshold and signer count directly from the multisig contract, then confirm against documented signer identities that the signers span distinct organisations, jurisdictions, and security environments.
**Institutional Standard**: The multisig clears the RF03 floor (no fewer than three-of-five) and, reconciling the RF03 cure language, signers are distributed across at least three independent organisations, multiple jurisdictions, and separate security environments so no single party or compromise reaches threshold.
**Status**: Gap with action
**If Not Found — Gap Action**: If signer independence is undocumented, classify G2 and require a signer register mapping each on-chain owner to a distinct organisation, jurisdiction, and security environment; if the threshold is below three-of-five or signers are concentrated in one organisation, state it as an RF03 finding and name the concentration.
**Source / Precedent**: Drift, 1 Apr 2026: $285M lost when a 2-of-5 multisig was reached by social-engineering signers — a threshold below the floor and signers not independently distributed allowed a single coordinated compromise to clear it.
**Criterion ID(s)**: 7.2, RF03
