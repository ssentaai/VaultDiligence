---
schema_version: 1
id: 2022-terra-collapse
title: Terra UST algorithmic stablecoin collapse
date: 2022-05-09
chains: [terra-classic, ethereum]
protocols_directly_affected: [terra, anchor-protocol]
protocols_indirectly_affected: [celsius, three-arrows-capital, voyager]
vault_types_at_risk:
  - VT-A
classification: depeg
loss_estimate_usd: 40000000000
loss_confidence: HIGH
sources:
  - url: https://www.coindesk.com/learn/the-fall-of-terra-a-timeline-of-the-meteoric-rise-and-crash-of-ust-and-luna
    type: FORMAL
    retrieved: 2026-05-05
  - url: https://en.wikipedia.org/wiki/Terra_(blockchain)
    type: FORMAL
    retrieved: 2026-05-05
---

## What happened

Beginning 2022-05-07, large UST withdrawals from Anchor Protocol and the Curve 3pool stressed the algorithmic peg between UST (Terra's algorithmic stablecoin) and LUNA (its absorbing token). The stabilisation mechanism allowed UST holders to mint $1 worth of LUNA per UST burned, intended to arbitrage the peg back. Under sustained selling pressure, the mechanism instead created hyperinflationary LUNA issuance — LUNA supply expanded from approximately 345M tokens to over 6.5 trillion within days. Both UST and LUNA approached zero. Approximately $40B+ in market value was destroyed across the Terra ecosystem, with downstream collapses at Celsius, Three Arrows Capital, and Voyager later in 2022 attributed in significant part to Terra exposure.

## Why it matters for diligence

This is the canonical example of an algorithmic dual-token stablecoin where the peg-defence mechanism becomes the destruction mechanism under stress. The diligence signature is structurally simpler than later incidents — there was no off-chain compromise, no fund-manager misappropriation, no oracle hardcode trick. The collateralisation model itself was the gap: UST was backed primarily by reflexive demand for LUNA, with a partial BTC reserve that proved insufficient. Anchor Protocol's 19.5% yield on UST deposits was the demand engine; when that demand reversed, the peg-defence mechanism imposed costs faster than reserves could absorb. VaultDiligence's typical vault scope (VT-1 through VT-8 / VT-A) does not include pure algorithmic stablecoins of this design today, so this entry serves primarily as a historical anchor for cross-vault recurrence patterns rather than as an active diligence reference.

## Diligence signature

- field_id: F-COL-018 (collateralisation mechanism class)
  state_pre_incident: E
  gap_action: "Classify the collateralisation mechanism: fully reserved (1:1 fiat-backed) | over-collateralised crypto | algorithmic dual-token | hybrid. For algorithmic dual-token mechanisms: G2 with action 'document the peg-defence mechanism's behaviour under sustained one-way pressure'."
  notes: "UST's classification was knowable and public. The mechanism's failure mode under stress was modelled and warned about by multiple analysts pre-collapse. The diligence question was not whether the design existed but whether the implications were surfaced to depositors."

- field_id: F-FIN-021 (yield source)
  state_pre_incident: E(P)
  gap_action: "For any yield-bearing position, identify the yield source. Yields paid from token-emissions or reflexive demand (rather than external revenue) are E(P) at best, with action 'document the yield's sustainability under reduced inflows'."
  notes: "Anchor's 19.5% was paid from a depleting reserve, not from sustainable revenue. This was knowable from Anchor's own published mechanics."

- field_id: F-COL-019 (reserve coverage)
  state_pre_incident: G2
  gap_action: "For any stablecoin claiming partial reserves, verify the ratio of liquid reserves to circulating supply AND the reserve's correlation with the issued asset under stress. Reserves correlated with the asset itself (e.g. BTC backing a crypto-stablecoin during a crypto-wide downturn) are G2."
  notes: "Terra's BTC reserve was correlated with the broader crypto downturn that triggered the run. Diversification on paper was concentration in stress."

## Cross-vault recurrence

- 2025-11-xusd-stream-finance — same classification (depeg) different mechanism (fund-manager loss disclosure rather than algorithmic peg-defence collapse).
- 2026-03-resolv-mint — same classification at the depeg layer, but Resolv's was an exploit-driven supply shock rather than a design-driven mechanism failure.

## Lessons reference

(None — this entry serves as historical anchor; lessons from Terra were absorbed industry-wide before VaultDiligence existed.)

## Notes

This entry is included primarily as a historical anchor for the `cross_vault_recurrence` salience axis. VaultDiligence's current vault-type scope (VT-1 through VT-8 / VT-A) does not include pure algorithmic dual-token stablecoins of UST's design — that design class effectively disappeared from institutional consideration after 2022. The diligence signature fields above are documented for completeness but are unlikely to fire on contemporary diligence packs.

The downstream Celsius / 3AC / Voyager collapses are not separate entries here because their primary failure modes (off-chain credit, undisclosed leverage, undercollateralised borrower exposure) were independent of the Terra mechanism. They are referenced in this notes section because the Terra collapse was a contributing cause; full entries would be in scope if VaultDiligence begins covering CeFi-counterpart vault types.

The factual claims in this entry are sourced from public reporting and Wikipedia, both well-documented for an event of this prominence. The schema's normal preference for FORMAL sources is satisfied by the broad public record; primary post-mortems from Terraform Labs are not included because the entity was subject to ongoing legal proceedings as of the entry date.
