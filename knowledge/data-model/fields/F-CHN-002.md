# F-CHN-002

**Field ID**: F-CHN-002
**Category**: Chain
**Sub-Category**: Architecture
**Field Name**: Network Architecture & Security Model
**What to Collect / Question to Answer**: What is the chain's consensus mechanism and finality model, its settlement layer (for L2s), its divergence from standard EVM behaviour, and are the chain's own contracts audited, bug-bounty-covered, and open-source?
**Data Type**: Structured text (consensus, finality model, settlement layer, EVM divergence, audit references, bug-bounty terms, source-code links)
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P13
**Primary Source**: Chain technical documentation and yellow/whitepaper; audit reports on consensus, settlement, and governance contracts; bug-bounty programme listing; public source-code repositories
**Fallback Source**: Third-party chain-architecture analyses (L2BEAT, rollup risk reviews) and recognised audit-firm publication pages
**Evidence Pathway**: Inspection-validatable: read the chain's consensus, settlement, and governance contract source from public repositories and verify open-source status; Third-party-evidenced: cite the named audit firm's report and the active bug-bounty programme (Immunefi or equivalent) sized to chain TVL.
**Institutional Standard**: Architecture documented (consensus, finality, settlement layer, any EVM divergence in precompiles/opcodes/gas model); chain contracts audited by reputable firms with reports available; an active bug bounty sized to chain TVL; consensus, execution, and settlement code open and publicly auditable.
**Status**: Gap with action
**If Not Found — Gap Action**: Name each missing element (consensus/finality documentation, settlement-bridge identification, EVM-divergence disclosure, contract audit, bug bounty, or open-source confirmation) and request it from the chain foundation; flag closed-source consensus or settlement code, missing chain-contract audits, or material undocumented EVM divergence as critical conditions.
**Source / Precedent**: a published protocol risk framework, 9 Jun 2026, §4.2: closed-source consensus or settlement code, missing audits on chain contracts, unrated L2 settlement security, or material undocumented divergence from standard EVM behaviour materially constrain the chain's evaluation tier.
**Criterion ID(s)**: 13.2, RF45
**Registered Sources (Fix 70)**: l2beat-chain-risk
