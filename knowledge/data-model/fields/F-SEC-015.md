# F-SEC-015

**Field ID**: F-SEC-015
**Category**: Security
**Sub-Category**: Infrastructure
**Field Name**: MPC-vs-Multisig Custody Transparency
**What to Collect / Question to Answer**: For each privileged authority, is custody an on-chain multisig or an MPC arrangement, and if MPC, are the shard count, signing quorum, shard-holder identities, and the open-source/independent-auditability status of the MPC cryptographic library all disclosed?
**Data Type**: Text (per authority)
**Vault Types**: ALL
**Collection Tier**: T2a
**Pillar(s)**: P7
**Primary Source**: Operator security documentation / governance disclosure naming custody type per authority
**Fallback Source**: On-chain inspection of the authority address (single EOA-like footprint indicates MPC) plus operator CTO confirmation
**Evidence Pathway**: Inspection-validatable: read the authority address on-chain to confirm whether it is a multisig contract or a single externally-owned-account footprint, then confirm against the operator's disclosed shard/quorum/holder and MPC-library statement.
**Institutional Standard**: Custody is a transparent on-chain multisig whose signer set is publicly readable; where MPC is used, the shard count, signing quorum, shard-holder identities, and whether the MPC cryptographic library is open-source and independently auditable are all disclosed, so the authority surface is verifiable rather than trusted.
**Status**: Gap with action
**If Not Found — Gap Action**: Request from the operator a per-authority custody-type statement; for any MPC authority, request shard count, signing quorum, shard-holder identities, and the MPC library name with its open-source/audit status. If MPC is used and these are withheld, classify the authority surface as undisclosed (G2) and name the operator CTO as the entity that must produce it.
**Source / Precedent**: Aave/LlamaRisk risk framework, 9 Jun 2026, §1.7: an MPC arrangement 'produces an on-chain footprint identical to a single externally-owned account,' so without shard/quorum/holder disclosure and confirmation that 'the MPC cryptographic library is open-source and independently auditable,' the allocator trusts an unverifiable authority surface.
**Criterion ID(s)**: 7.16
