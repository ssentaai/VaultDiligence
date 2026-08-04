# F-PRJ-004

**Field ID**: F-PRJ-004
**Category**: Security
**Sub-Category**: Project Gate
**Field Name**: Off-Chain Key Storage Method
**What to Collect / Question to Answer**: Where are privileged signing keys physically stored? AWS KMS / GCP KMS / Azure Key Vault / HSM / MPC (Fireblocks/Anchorage/Copper) / Hardware wallet (Ledger/Trezor). State specifically.
**Data Type**: Text
**Vault Types**: ALL
**Collection Tier**: T4
**Primary Source**: Operator CTO disclosure / infrastructure security documentation
**Fallback Source**: Audit scope documentation (check if off-chain infra was in scope)
**Pillar(s)**: P0/P7
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: Request infrastructure security documentation from operator CTO. If undisclosed: flag as P0 hard gate fail — RF41.
**Criterion ID(s)**: 0.3 / 7.16
**Red Flag ID(s)**: RF41