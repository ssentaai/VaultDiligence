---
schema_version: 1
id: 2026-04-kelp-dvn
title: Kelp DAO 1-of-1 DVN bridge compromise and Aave contagion
date: 2026-04-18
chains: [ethereum]
protocols_directly_affected: [kelp]
protocols_indirectly_affected: [aave, layerzero]
vault_types_at_risk:
  - VT-5
  - VT-1
classification: counterparty
loss_estimate_usd: 292000000
loss_confidence: HIGH
sources:
  - url: a legal analysis
    type: FORMAL
    retrieved: 2026-06-18
---

## What happened

On 2026-04-18 an attack attributed to Lazarus drained approximately $292M from Kelp DAO by forcing a failover to a 1-of-1 LayerZero DVN (decentralised verifier network) — a single message-verifier configuration that LayerZero shipped as the default for a large share of integrators. With one verifier controlling message validity on the route, the attacker minted/moved roughly 116,500 rsETH (about 18 percent of supply). A pauser froze the affected path 46 minutes after the drain began, blocking an estimated further $200M.

The loss did not stay contained. rsETH was widely used as collateral on Aave, and the depeg propagated: Aave's shared-pool and E-Mode treated the depegged rsETH as still valid, host-pool utilisation reached full as roughly $5.4B was withdrawn within hours, and depositors with no rsETH exposure at all — ordinary ETH and USDC suppliers in the same pool — were frozen by the utilisation spike. Estimated bad debt ran $123M-$230M, and DeFi TVL fell on the order of $13B over two days.

## Why it matters for diligence

The proximate failure was a single cross-chain verifier — the exact configuration the bridging baseline treats as below minimum (at least three independent verifiers required). The default-vs-chosen distinction matters: a known-weak vendor default is a finding even when the operator did not deliberately select it. The second-order failure was contagion through a shared lending pool whose isolation/E-Mode grouping let a depegged asset freeze unrelated depositors — a host-pool utilisation and shared-pool-contagion question, not a property of the vault that originated the loss. Incident-response speed was itself a quantifiable control: the 46-minute detection-to-pause window set the loss boundary.

## Diligence signature

- field_id: F-BRG-002 (verifier-set threshold)
  state_pre_incident: G2
  gap_action: "Read the configured verifier set on each route on-chain. A one-of-N or two-of-N configuration is a critical condition (RF44); record whether it is vendor-default or operator-chosen."
  notes: "LayerZero's 1-of-1 DVN default was the single point of failure. A baseline of at least three independent verifiers would have made the forced failover insufficient."

- field_id: F-BRG-010 (bridge incident-response & monitoring coverage)
  state_pre_incident: G2
  gap_action: "Confirm 24/7 redphone reachability and a measured detection-to-pause latency across vendor, attestors, and issuer. Absent or slow incident response is a critical condition."
  notes: "The 46-minute pause blocked ~$200M; faster detection would have lowered the loss boundary further."

- field_id: F-COL-008 (shared-pool contagion / collateral correlation)
  state_pre_incident: G2
  gap_action: "Map whether the vault token is used as collateral in shared lending pools where its depeg can freeze unrelated depositors via utilisation or E-Mode grouping. Name the host pool and the isolation mode."
  notes: "Aave's shared pool / E-Mode treated depegged rsETH as valid, freezing ETH/USDC depositors with no rsETH exposure."

- field_id: F-LIQ-048 (host-pool utilisation & illiquidity threshold)
  state_pre_incident: G2
  gap_action: "Determine the host-pool utilisation and the illiquidity threshold at which exits stop clearing. Full utilisation under stress is a critical condition for any depositor in the pool."
  notes: "Utilisation reached full as ~$5.4B exited within hours; exit capacity vanished for everyone in the pool."

## Cross-vault recurrence

- 2026-04-drift-multisig — same actor class (DPRK), same week, off-chain/human-and-infrastructure compromise rather than a contract bug.
- 2026-03-resolv-mint — different mechanism, same shared-pool contagion shape into Morpho/Fluid.

## Lessons reference

(None yet. A cross-pack lesson on "single cross-chain verifier (1-of-1 DVN) as a total-loss configuration" is a candidate for graduation.)

## Notes

The facts above are drawn from the in-tree Buzko Krasnov legal analysis (Filipp Petkevitch, 2026-04-27), a published law-firm legal analysis taken as FORMAL under source-authority.md ("legal opinions"). Corroborating primary news / post-mortem URLs are not yet attached and should be added at the next D1 — flagged G2 in docs/state-of-framework-v54.md. The contagion figures ($123M-$230M bad debt, ~$5.4B withdrawn, ~$13B TVL decline) are single-source ranges, not on-chain-reconciled. Classification mapped to the closed incident vocabulary as `counterparty` (the 1-of-1 DVN is a single trusted-verifier counterparty failure); the vocabulary has no `bridge-exploit` term — a candidate vocab extension that P12 Bridging now motivates.
