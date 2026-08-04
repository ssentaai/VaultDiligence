# F-CTR-024

**Field ID**: F-CTR-024
**Category**: Smart Contract
**Sub-Category**: Battle-Testedness
**Field Name**: Codebase Battle-Testedness — Value-Secured & Value-Since-Last-Release
**What to Collect / Question to Answer**: What dollar value has the utilised codebase already secured over what duration, and how much value has the current release in particular held since the last major code change reset that clock?
**Data Type**: Structured: { lifetime_value_secured_usd, lifetime_duration_days, last_major_release_date, value_secured_since_release_usd, days_since_release }
**Vault Types**: ALL
**Collection Tier**: T2
**Pillar(s)**: P7
**Primary Source**: On-chain: TVL history at the contract addresses for the lifetime of the codebase and from the block of the last major release forward, read from the vault contract balances and protocol analytics
**Fallback Source**: Operator-stated TVL-secured history cross-checked against a third-party analytics dashboard (DeFiLlama or equivalent) for the same addresses
**Evidence Pathway**: Inspection-validatable: derive value-secured and duration from on-chain TVL history at the deployed addresses, and separately measure value held only since the last major release block so a recent release cannot borrow the prior version's track record.
**Institutional Standard**: The codebase has secured material value over an extended live period and, critically, the current release has itself held material value since its deployment — a fresh release is treated as resetting the empirical clock regardless of the prior version's history.
**Status**: Gap with action
**If Not Found — Gap Action**: If value-secured or last-release date is unstated, classify G2 and require the operator to state the last major release date and the value held since; where a release is recent, state explicitly that empirical battle-testedness is reset and the prior version's track record does not transfer.
**Source / Precedent**: Resolv, Mar 2026: the prior codebase's track record did not protect against the deployed-but-unaudited change that minted $80M of unbacked supply ($34M net loss) — value secured by an earlier release did not carry over to the changed code.
**Criterion ID(s)**: 7.4, RF02
