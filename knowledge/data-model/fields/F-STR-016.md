# F-STR-016

**Field ID**: F-STR-016
**Category**: Strategy Risk
**Sub-Category**: Restaking
**Field Name**: LRT Peg Integrity & Redemption Backing
**What to Collect / Question to Answer**: For a vault holding or issuing an LRT: what maintains the LRT's peg to its underlying restaked ETH — is it 1:1 redeemable on demand, or only through the full unbonding queue? What is the on-chain / secondary DEX liquidity at exit size ($1M / $5M / $10M), for each chain the LRT is bridged to? At what depeg magnitude do downstream leveraged positions get liquidated? Record any historical depeg events (date, magnitude, duration, recovery).
**Data Type**: Structured — `{ redemption_mechanism, dex_depth_by_chain@{1M,5M,10M}, depeg_to_liquidation_threshold_pct, historical_depegs[] }`.
**Vault Types**: `Strategy = restaking` (narrower: where the vault holds or issues an LRT — modality ≠ native, per F-STR-015)
**Collection Tier**: T1
**Pillar(s)**: P9 (Liquidity) + P4 (Collateral). *(propose; operator confirms)*
**Primary Source**: LRT contract (redemption mechanism) + DEX pool state per chain (depth at exit size), read on-chain and dated; downstream lending markets for the liquidation threshold.
**Fallback Source**: 1inch / DefiLlama liquidity data and historical price series for the LRT, cited with date.
**Evidence Pathway**: Inspection-validatable — read the redemption mechanism from the LRT contract, measure DEX depth at $1M/$5M/$10M on each chain, and read the liquidation LTV of downstream lending positions to derive the depeg-to-liquidation threshold.
**Institutional Standard**: The LRT's redemption basis is stated (on-demand vs queue-only); DEX depth at exit size is measured per chain; the depeg magnitude at which downstream leverage liquidates is computed; historical depegs are logged — so the allocator sees whether a small peg wobble on a thin chain becomes a liquidation cascade.
**Status**: Gap with action
**If Not Found — Gap Action**: E if redemption basis, per-chain DEX depth, and liquidation threshold are readable on-chain and dated. E(P) if peg is measured but per-chain depth is incomplete. G2 if backing exists but is unpublished. G3 if no redemption backing is defined (bare receipt token). N/A if the vault restakes natively with no LRT (F-STR-015 = native).
**Source / Precedent**: Sevim & Ferreira Torres, arXiv:2604.03274 — a 3.33% depeg of bridged ezETH triggers liquidations against 64,890 ezETH with only 0.23% DEX liquidity on Linea; that liquidation could unwind ≈ 0.76% of Lido's 8.5M staked ETH. Buzko Krasnov, 27 Apr 2026 — rsETH lost its peg when the bridge reserve drained, producing $123M–$230M Aave bad debt while E-Mode still treated it as valid collateral.
**Criterion ID(s)**: propose at ratification.
