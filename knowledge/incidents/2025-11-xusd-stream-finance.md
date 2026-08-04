---
schema_version: 1
id: 2025-11-xusd-stream-finance
title: xUSD depeg from Stream Finance fund-manager loss disclosure
date: 2025-11-04
chains: [ethereum, arbitrum]
protocols_directly_affected: [stream-finance]
protocols_indirectly_affected: [morpho, euler, silo, gearbox, compound, elixir, beefy, lista-dao]
vault_types_at_risk:
  - VT-3a
  - VT-7
classification: depeg
loss_estimate_usd: 285000000
loss_confidence: MEDIUM
sources:
  - url: https://blockeden.xyz/blog/2025/11/08/m-defi-contagion/
    type: FORMAL
    retrieved: 2026-05-05
  - url: https://www.htx.com/news/Project%20Updates-4NfKiUET/
    type: FORMAL
    retrieved: 2026-05-05
  - url: https://coinmarketcap.com/academy/article/stream-finance-stablecoin-xusd-crashes-77percent-after-dollar93m-loss
    type: FORMAL
    retrieved: 2026-05-05
  - url: https://www.ccn.com/education/crypto/why-xusd-depegged-stream-finance-stablecoin-crisis-explained/
    type: FORMAL
    retrieved: 2026-05-05
  - url: https://web.ourcryptotalk.com/news/stream-finance-collapse-explained
    type: FORMAL
    retrieved: 2026-05-05
---

## What happened

On 2025-11-04, Stream Finance disclosed that an external fund manager (later identified in a Stream Trading Corp lawsuit as Ryan DeMattia) had caused a loss of approximately $93M after his personal leveraged trading positions were liquidated during the 2025-10-10 ETH price crash, with funds reportedly misappropriated from Stream protocol assets to cover those losses. Stream paused all deposits and withdrawals on disclosure. xUSD, Stream's yield-bearing stablecoin, depegged within hours: from $1 to roughly $0.50, then to $0.27 within 24 hours, eventually trading at $0.07–$0.14 by 2025-11-08.

The depeg propagated through the lending ecosystem because xUSD had been used as collateral in recursive looping strategies across Morpho, Euler, Silo, Gearbox, and Compound markets. Liquidations failed to fire because the lending protocols' oracles had hardcoded xUSD's price at $1 to prevent cascading liquidations — a design choice that protected against price-feed volatility but made the system unable to respond when the peg actually broke. Total debt exposure across the affected protocols was estimated by DeFi research group Yields and More at $285M, with major creditors including TelosC ($123.6M), Elixir ($68M, representing 65% of deUSD's reserves), a curator, and Varlamore. Elixir's deUSD subsequently lost approximately 65% of its backing.

## Why it matters for diligence

Two distinct diligence failures stack here. First, on Stream itself: a non-trivial portion of strategy was delegated to an external fund manager whose individual trading positions were not segregated from protocol assets in a way that survived market stress. The fund-manager arrangement, the segregation discipline, and the recourse path on misappropriation were the load-bearing diligence items, and at least one was missing. Second, on the curators of the vaults that accepted xUSD as collateral: the recursive looping strategy depended on xUSD's peg holding, the oracle was hardcoded to $1 (foreclosing the standard liquidation mechanism), and the curator vaults did not surface this in their published risk parameters in a form retail depositors could evaluate. The lending protocol curators (a curator, Re7 Labs, Varlamore) accepted xUSD without diligence equivalent to what a prudent institutional allocator would have done; the reported 18% APY was the price of that gap.

## Diligence signature

- field_id: F-OPS-008 (operational structure: external delegations)
  state_pre_incident: G2
  gap_action: "Identify every external party with discretionary authority over protocol assets. For each, document: (a) segregation discipline between personal and protocol positions, (b) recourse path on misappropriation, (c) audited financial controls. Discretionary external delegation without independently audited segregation is G2 with action 'request fund-manager attestation and segregation audit'."
  notes: "Stream's fund-manager arrangement was the load-bearing risk item. Whether DeMattia was acting outside his authority or within it (with deficient controls) does not change the diligence implication: the external delegation had insufficient bounds."

- field_id: F-COL-014 (oracle methodology for collateral)
  state_pre_incident: G2
  gap_action: "For any vault accepting an asset as collateral, verify that the oracle used CAN reflect a depeg below $1 with reasonable price discovery. Hardcoded-to-$1 oracles foreclose liquidation and are G2 with action 'request market-aware oracle or explicit liquidation-suspension policy'."
  notes: "The hardcode-to-$1 oracle was a risk-management choice that protected against feed volatility but inverted into a fatal weakness when the peg broke. This is knowable from the curator's published parameters at allocation time."

- field_id: F-COL-015 (recursive collateral exposure)
  state_pre_incident: G2
  gap_action: "Identify whether the asset accepted as collateral is the issuer's own product used in a recursive loop. If so: G2 with action 'document the loop's de-leveraging path under stress'."
  notes: "xUSD looped on Morpho/Euler/Silo via curator vaults that themselves were the issuer's primary distribution channel. The loop amplified the $93M loss into $285M of debt exposure."

- field_id: F-FIN-027 (fund-manager attestation)
  state_pre_incident: G3
  gap_action: "If the protocol delegates strategy execution to an external fund manager, require quarterly attestation of asset segregation from an independent auditor. Absence is G3."
  notes: "Stream's structure was knowable; the missing attestation was knowable. The diligence question was not 'is there a fund manager' but 'is the fund manager's exposure bounded by something verifiable'."

- field_id: F-CTR-031 (curator-disclosed risk parameters)
  state_pre_incident: G2
  gap_action: "For any curated vault, verify that the curator publishes (a) the oracle methodology, (b) the LTV curve, (c) the collateral asset's recursive-loop status. Vague or absent curator-side disclosure is G2."
  notes: "Curators TelosC, a curator, Re7 Labs, and Varlamore had varying disclosure levels. Re7 admitted to ~$14.65M exposure in xUSD-isolated vault on Euler post-incident. Disclosure quality is itself a diligence signal."

## Cross-vault recurrence

- 2026-03-resolv-mint — same shape (off-chain operational opacity not bounded by on-chain controls) different mechanism (key compromise vs. fund-manager misappropriation).
- 2022-terra-collapse — same classification (depeg) different mechanism (algorithmic vs. fund-manager loss disclosure).
- (a synthetic-dollar issuer ENA depeg, 2025-10-10 — referenced in sources, separate incident, would warrant its own entry)

## Lessons reference

(None yet. A cross-pack lesson on "external fund-manager delegations require independent segregation attestation" and another on "hardcoded $1 oracles are diligence gaps not safety features" are candidates if the pattern recurs.)

## Notes

The risk-infrastructure provider paper frames this as a "Withdrawal Trap / Information Latency" failure (curators couldn't rebalance fast enough). That framing is incomplete. The deeper failure was at the diligence layer — the off-chain delegation structure on Stream and the oracle hardcode at the curator level were both knowable pre-allocation. The Information Latency was a consequence; the diligence gap was the cause. The risk-infrastructure provider framing serves their thesis (that block-level autonomy would have helped) but understates how much was structurally avoidable through pre-allocation evidence-gathering.

The October 10 ETH crash that triggered DeMattia's liquidations is referenced in multiple sources but its own diligence implications (a synthetic-dollar issuer depeg, broader market stress) are out of scope for this entry.

The Balancer hack of 2025-11-03 ($128M) preceded this incident by ~24 hours and accelerated the depeg dynamics through general market panic, but Stream's disclosure was independent of and not caused by Balancer; Stream's loss had been disclosed by DeMattia internally on 2025-11-02 per public reporting.
