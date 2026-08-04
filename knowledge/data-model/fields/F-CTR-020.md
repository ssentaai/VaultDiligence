# F-CTR-020

**Field ID**: F-CTR-020
**Category**: Contract
**Sub-Category**: Economic Security
**Field Name**: Economic Security Backing — Validator/Signer Set
**What to Collect / Question to Answer**: For every validator set or signer set in the protocol's trust model (own multisig per F-CTR-005, plus every bridge's validator set per F-CTR-018/019), quantify the economic security backing the set. Distinguishes structurally different cases that F-CTR-005 alone collapses: "5-of-9 multisig with no economic stake at risk" vs "5-of-9 validator set with $200M slashable stake" vs "AVS-backed with $1B restaked ETH and documented slashing precedent." For each set capture: (a) slashable stake amount in USD, (b) slashing conditions documented (Y/N + URL if Y), (c) slashing has actually occurred historically (Y/N — N means slashing is theoretical, not tested), (d) insurance/cover layered on top (Y/N + amount), (e) bond posted by individual signers (Y/N + amount per signer if applicable).
**Data Type**: Structured list — each entry: { set_identifier, slashable_stake_usd, slashing_conditions_url, slashing_occurred_historically: bool, insurance_amount_usd, individual_bond_usd }
**Vault Types**: ALL (every vault has at least the protocol's own signer set; vaults with cross-chain dependencies have multiple)
**Collection Tier**: T2
**Primary Source**: For AVS-backed or restaking-backed sets: read the AVS smart contract for total restaked stake and slashing parameters. For traditional multisigs: explicit confirmation that no on-chain slashing exists. For PoS validator sets: read the staking contract for total staked + slashing rules.
**Fallback Source**: Bridge protocol documentation describing validator economics + audit report's economic-security section
**Pillar(s)**: P7, P8
**D1**: Y
**D2**: Y
**D3**: Y
**D4**: Y
**D5**: Y
**Required?**: Y
**If Not Found — Gap Action**: G2 if signer set exists but economic backing is undocumented. "No economic stake at risk" is a valid finding — state it explicitly. A 5-of-9 multisig with no slashing is structurally different from a 5-of-9 validator set with credible slashing, and the report must distinguish them. Theoretical slashing (documented but never executed) ranks below tested slashing (executed at least once on a known incident); state which.
**Criterion ID(s)**: 7.2, 7.6, 8.4
**Red Flag ID(s)**: RF03, RF-CTL-006 (signer set with no economic skin)
