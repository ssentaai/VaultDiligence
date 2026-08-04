# F-ORC-013

**Field ID**: F-ORC-013
**Category**: Oracle
**Sub-Category**: RWA-Specific
**Field Name**: Internal Issuer-Side Oracle Surface
**What to Collect / Question to Answer**: What are the issuer-internal oracle surfaces — the mint/burn gate, the redemption-pricing mechanism, the internal exchange-rate feed, and the proof-of-reserves figure — and can any of them be manipulated within a single transaction or be made to move in a way the consumed external feed would not detect?
**Data Type**: Text (per surface: source, update authority, monotonicity, single-tx manipulability)
**Vault Types**: Strategy=lending OR (Structure=multi-asset-pool AND Management=algorithmic AND Exposure=crypto-native) OR Structure in {leveraged,looped}  (derived from VT-N; original "Vault Types" value: VT-1, VT-6, VT-7)
**Collection Tier**: T3
**Pillar(s)**: P3
**Primary Source**: Issuer contract code for mint/burn and exchange-rate functions; redemption-pricing and PoR methodology docs
**Fallback Source**: Third-party oracle/risk teardown (LlamaRisk, Chaos Labs) of the issuer-side mechanism
**Evidence Pathway**: Inspection-validatable: read the mint, burn, and exchange-rate functions in the issuer contract bytecode to confirm the gates cannot be moved by in-block donations or flash-loan-induced deviation and that the internal exchange-rate is monotonically non-decreasing under normal operation, then inspect how redemption pricing and PoR are sourced.
**Institutional Standard**: Good looks like a decomposed inventory of every issuer-internal oracle surface where the mint and burn gates cannot be unilaterally moved within a single transaction (in-block donations and flash-loan-induced deviations are excluded), the internal exchange-rate feed is monotonically non-decreasing under normal operation, and redemption pricing and proof-of-reserves draw from an independently verifiable source rather than a hardcoded internal value.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the issuer mint/burn/exchange-rate functions and document each internal surface's source and update authority. Where the exchange-rate or redemption price is set by an internal or hardcoded value with no independent check, state the gap and the single-transaction manipulability exposure; this field is un-deferred given its allocator share (consumed-feed checks pass while the asset is counterfeit).
**Source / Precedent**: Aave-LlamaRisk protocol risk framework, 9 Jun 2026, §1.18: mint and burn gates 'cannot be unilaterally manipulated within a single transaction; in-block donations, flash-loan-induced deviations... are explicit critical conditions... internal exchange-rate oracles are monotonically non-decreasing under normal operation.' Grounded by Resolv's hardcoded internal oracle enabling an effectively infinite mint.
**Criterion ID(s)**: 3.6, RF28
