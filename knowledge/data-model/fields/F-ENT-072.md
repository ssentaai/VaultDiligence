# F-ENT-072

**Field ID**: F-ENT-072
**Category**: Entity
**Sub-Category**: Sanctions
**Field Name**: OFAC SDN Screening — Vault Address and Signers
**What to Collect / Question to Answer**: Is the vault contract address or any multisig signer wallet on the OFAC Specially Designated Nationals list?
**Data Type**: Y/N/Hit
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: OFAC SDN API: sanctionslistservice.ofac.treas.gov/api/search?value={address}
**Fallback Source**: TRM Labs on-chain oracle (if integrated)
**Pillar(s)**: P2,P10
**D1**: Y
**D2**: Y
**D3**: Y
**Required?**: Y
**If Not Found — Gap Action**: Run OFAC API against vault address and all multisig signers. Any hit = auto-disqualifier. Takes <1 second. Non-negotiable compliance check.
**Criterion ID(s)**: 2.5
**v54 Refinement (gap audit 2026-06-12)**: Extend single-regime OFAC screening to multi-regime sanctions coverage (OFAC, UK OFSI, EU) and a five-year lookback on entity and founder regulatory enforcement, consent orders, and material litigation. Source: Steakhouse DDQ sections 5.7/5.8.
**Red Flag ID(s)**: RF01