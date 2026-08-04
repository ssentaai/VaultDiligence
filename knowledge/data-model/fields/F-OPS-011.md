# F-OPS-011

**Field ID**: F-OPS-011
**Category**: Operational
**Sub-Category**: Contributor Security
**Field Name**: Multisig Signer Identity Verification
**What to Collect / Question to Answer**: Are multisig signers identity-verified beyond wallet address? Hardware wallet requirement? Named individuals with verifiable identities? Signer rotation policy?
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T4
**Primary Source**: Operator disclosure / governance documentation
**Fallback Source**: On-chain multisig signer addresses — cross-reference with known team members
**Pillar(s)**: P8
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Request signer identity documentation. Hardware wallet requirement check. Drift precedent: signers social-engineered via fake trading firm relationship.
**Criterion ID(s)**: 8.7
**v54 Refinement (gap audit 2026-06-12)**: Add a device-exposure / air-gap dimension to signer identity: whether hardware-wallet signers are exposed to other devices, regularly cycled, and isolated from general-purpose machines. Source: Steakhouse DDQ sections 2.9/2.10; Buzko Drift precedent (cross-ref F-OPS-012, RF42).
**Red Flag ID(s)**: RF42