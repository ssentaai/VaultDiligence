# F-STR-020

**Field ID**: F-STR-020
**Category**: Financial
**Sub-Category**: Hedge
**Field Name**: Spot-Leg Collateral Quality & Redemption-Discount Risk
**What to Collect / Question to Answer**: What asset is the long/spot leg (e.g. staked ETH / LST / liquid stable / tokenized T-bill), and what is *its own* liquidity and redemption profile relative to the hedge — can it be sold or redeemed at par on the timeline needed to close the delta-neutral position, or does it carry a de-peg / secondary-market discount / staking-withdrawal-queue that would prevent realising par? State the observed maximum discount-to-NAV and the redemption/withdrawal-queue latency for the spot asset with source and date. This is the spot-*collateral* quality question — distinct from the perp/spot *basis* (`F-HED-003`).
**Data Type**: Structured (spot asset identity; max observed discount-to-NAV %; redemption/withdrawal-queue latency; on-chain/secondary depth at position size)
**Vault Types**: `Strategy = basis/funding-trade`
**Collection Tier**: T2a
**Pillar(s)**: P5 (propose; cross-refs P4) — operator confirms
**Primary Source**: On-chain / market data for the spot asset's historical discount-to-NAV and secondary depth (e.g. LST market pools, stable oracle deviations); protocol documentation of the spot asset's redemption/withdrawal mechanics and queue
**Fallback Source**: Operator disclosure of the spot-leg composition and its redemption assumptions; the composed-asset's own VaultDiligence assessment where it is a separately-tokenized backing (downward look-through, `composes:`)
**Evidence Pathway**: Third-party-evidenced / on-chain: read the spot asset's maximum historical discount-to-NAV and its redemption/withdrawal-queue latency, and the secondary-market depth available to exit the spot leg at position size.
**Institutional Standard**: The spot-leg asset's maximum observed discount-to-NAV, its redemption/withdrawal-queue latency, and the depth available to exit it at position size are recorded with source and date, so the allocator can see whether the "delta-neutral" long can actually be realised at par when the hedge is unwound. (Fact to record.)
**Status**: Gap with action
**If Not Found — Gap Action**: Spot-asset discount history + redemption latency retrieved on-chain / from primary data: E. Operator names the spot asset but its redemption-discount history is not assembled: E(P). Spot-leg composition undisclosed: G2. Where the spot leg is another tokenized asset already assessed, inherit via downward look-through and note the pointer. N/A if the spot leg is native cash with no redemption-discount surface.
**Source / Precedent**: a synthetic-dollar vault oracle incident (Oct 2025) — a synthetic-dollar vault printed $0.65 on Binance off a thin single-venue orderbook while collateral was intact, i.e. the *observed* spot value diverged from backing (published vault-mechanics research). LST redemption queues (staked-ETH withdrawal congestion) and stable de-pegs mean the long cannot always be realised at par independent of perp/spot basis; `F-HED-003` measures only the derivative basis. a synthetic-dollar issuer's backing includes staked ETH and liquid stables whose own quality varies (issuer documentation).
**Criterion ID(s)**: propose new under P5 (operator assigns); adjacent to criterion 5.3
