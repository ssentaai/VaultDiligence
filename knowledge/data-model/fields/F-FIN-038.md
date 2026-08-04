# F-FIN-038

**Field ID**: F-FIN-038
**Category**: Financial
**Sub-Category**: Collateral
**Field Name**: Proof of Reserves
**What to Collect / Question to Answer**: Real-time on-chain PoR URL or attestation link
**Data Type**: URL
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: Protocol dashboard / Dune Analytics / Centrifuge pool page / chainlink proof-of-reserve
**Pillar(s)**: P4
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: No PoR = flag RF04. Link directly to the on-chain data, not to operator's description of it.
**Criterion ID(s)**: 4.4
**v54 Refinement (gap audit 2026-06-12)**: Extend beyond an aggregate PoR link to component-level reserve composition (each collateral component, not a single 'fully backed' figure), with attestation cadence sized to the asset's risk dynamics and the real-time backing / redemption-buffer state observable. Source: a published protocol risk framework section 1.10. Cross-ref F-FIN-079, F-FIN-080.
**Red Flag ID(s)**: RF04