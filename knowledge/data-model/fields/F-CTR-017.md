# F-CTR-017

**Field ID**: F-CTR-017
**Category**: Contract
**Sub-Category**: Upgradability
**Field Name**: Core Protocol Immutability — Verified Flag
**What to Collect / Question to Answer**: Is the core protocol code immutable (cannot be upgraded by any authority)? Distinct from F-CTR-003 (permissioned/permissionless) and F-CTR-004 (upgrade timelock). A protocol with a permissionless interface can still be upgradeable; immutability means no upgrade path exists at all. Per Egalite (May 2026): "If the core protocol cannot be upgraded, there is no upgrade path to exploit, no admin function to compromise, and no possibility of an atomic hack where funds are drained in a single transaction." Verify by inspecting the contract for any proxy pattern, upgrade authority, or initializer that could be re-invoked. Uniswap V2 is the canonical immutable reference.
**Data Type**: Enum: `immutable` | `upgradeable_with_timelock` | `upgradeable_without_timelock` | `unknown` + verification_method (text)
**Vault Types**: ALL
**Collection Tier**: T1
**Primary Source**: On-chain verification — inspect contract code for proxy patterns (Transparent, UUPS, Beacon), upgrade functions, initializer reuse paths
**Fallback Source**: Audit report's upgrade-architecture section + cross-check against on-chain
**Pillar(s)**: P7
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: G2. This is verifiable on-chain — a G2 here means the contract was not inspected, not that the answer is unknowable. State the verification gap explicitly. `unknown` is a placeholder for inspection-pending; never the final state for a published pack.
**Criterion ID(s)**: 7.1, 7.2
**v54 Refinement (gap audit 2026-06-12)**: Extend the immutability flag to enumerate replaceable or mutable components behind an 'immutable' claim — upgradeable hooks, replaceable libraries, or governance-swappable modules that make a nominally immutable contract mutable in practice. Source: gap audit 2026-06-12.
**Red Flag ID(s)**: RF-CTL-003 (upgradeable with no timelock = atomic-attack surface)
