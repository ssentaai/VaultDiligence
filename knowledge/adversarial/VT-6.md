

# VT-6 Adversarial Questions

**Applies when:** Structure = multi-asset-pool AND Management = algorithmic AND Exposure = crypto-native. [Phase 3 (2026-07-09): dimension-keyed; filename retained as a historical label.]

---

## Shared-Pool Contagion Question (from Kelp/Aave cascade, April 2026)

Source: buzko.legal/content-eng/defi-protocol-hacks-case-study
Added: 2026-04-29
Incident: Kelp DAO exploit → rsETH depeg → Aave bad debt $123-230M

Question: This vault deposits into a shared lending pool. What is the
Kelp/Aave cascade scenario for this vault? If a correlated collateral asset
depegs, does E-Mode or equivalent prevent normal liquidation? At what
utilisation rate does the pool become illiquid? Map the contagion path.

Why this matters: After the Kelp bridge drain, the attacker deposited stolen
rsETH as collateral in Aave V3, Compound V3, and Euler and borrowed $236M.
When rsETH lost its peg, Aave was left with bad debt of $123-230M. Users who
deposited ETH or USDC with no rsETH exposure could not withdraw — the pool
was drained by the bank run. $5.4B withdrawn from Aave within hours.
$13B+ total DeFi TVL lost in two days.

Aave E-Mode did not allow normal liquidation because it still treated the
depegged rsETH as valid collateral. This is the structural mechanism that
converted a bridge exploit into a $230M bad debt event for an unrelated pool.

Evidence to look for:
  What assets are deposited as collateral in the same pool as this vault?
  Does E-Mode apply? What collateral assets does it group together?
  What is the TVL of the correlated collateral assets in the same pool?
  At 100% utilisation: how long before liquidity recovers?
  Is there a circuit breaker for collateral asset depegs?

What closes it: Pool architecture documentation confirming isolation mode
for the subject vault's assets, or explicit simulation of a correlated
collateral depeg scenario with named structural consequences.
