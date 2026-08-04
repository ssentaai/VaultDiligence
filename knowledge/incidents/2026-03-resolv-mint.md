---
schema_version: 1
id: 2026-03-resolv-mint
title: Resolv USR illegitimate mint via compromised SERVICE_ROLE
date: 2026-03-22
chains: [ethereum]
protocols_directly_affected: [resolv]
protocols_indirectly_affected: [morpho, fluid, stream-finance]
vault_types_at_risk:
  - VT-A
  - VT-3a
classification: minting
loss_estimate_usd: 25000000
loss_confidence: HIGH
sources:
  - url: https://www.coindesk.com/markets/2026/03/23/resolv-stablecoin-drops-70-after-usd80-million-exploit-after-attacker-mints-usr
    type: FORMAL
    retrieved: 2026-05-05
  - url: https://www.dlnews.com/articles/defi/resolve-labs-stablecoin-falls-80-per-cent-as-millions-tokens-minted/
    type: FORMAL
    retrieved: 2026-05-05
  - url: https://www.chainalysis.com/blog/lessons-from-the-resolv-hack/
    type: FORMAL
    retrieved: 2026-05-05
  - url: https://www.theblock.co/post/394582/resolvs-usr-stablecoin-depegs-after-attacker-mints-80-million-unbacked-tokens-extracts-roughly-25-million
    type: FORMAL
    retrieved: 2026-05-05
  - url: https://blockaid.io/blog/how-a-compromised-key-minted-80m-in-resolvs-usr-stablecoin-and-triggered-a-depeg
    type: FORMAL
    retrieved: 2026-05-05
---

## What happened

On 2026-03-22 at 02:21 UTC, an attacker who had compromised Resolv Labs' off-chain key infrastructure made deposits totalling between $100,000 and $200,000 USDC and used the protocol's SERVICE_ROLE — a privileged externally-owned account (not a multisig) — to call `completeSwap` with inflated output amounts, minting approximately 80 million USR over two transactions (50M at 02:21, 30M at 03:41). The attacker swapped the USR through wstUSR, then to other stablecoins, then to ETH, extracting roughly $25M worth of ETH. USR depegged within 17 minutes of the first mint, falling to $0.025 on Curve before settling around $0.27 by Monday morning. Resolv subsequently burned and blacklisted approximately 46M USR (~57% of the illicit supply). The protocol's collateral pool was reportedly intact; the loss was the value extracted in ETH before pause.

The compromise chain ran through GitHub credentials of a contractor account, then into Resolv's AWS Key Management Service, where the attacker altered access policies on a signing key to gain mint-completion authority.

## Why it matters for diligence

This is an off-chain key compromise that the on-chain contract design failed to bound. The smart contract verified that a valid signature existed on the mint operation but did not enforce a maximum mint limit, did not check the deposit-to-mint ratio, and did not require oracle confirmation of a reasonable output amount. A pre-allocation diligence pack on USR would have surfaced two distinct gaps: (1) the SERVICE_ROLE was a single-key EOA rather than a multisig or timelock, and (2) the contract had no on-chain ratio invariant. Either alone is not necessarily disqualifying; together they are the exact pattern that broke. The auditing record (Resolv had reportedly undergone 18 audits) did not catch this because audits assess code correctness, not the economic invariants of the off-chain-on-chain split.

## Diligence signature

- field_id: F-CTR-022 (mint authority)
  state_pre_incident: G2
  gap_action: "Confirm mint authority is bound to a multisig or timelock with at least 24h delay. Single-EOA mint authority for a stablecoin issuer is G2 with action 'request multisig migration before allocation'."
  notes: "Resolv's SERVICE_ROLE was a single externally-owned account. This was knowable from the verified contract on Etherscan but the role's implications for systemic risk were not surfaced by the curators of vaults that accepted USR as collateral."

- field_id: F-CTR-024 (mint invariants)
  state_pre_incident: G2
  gap_action: "Confirm the mint contract enforces a maximum-mint-per-block invariant AND a deposit-to-mint ratio check that cannot be bypassed by signed off-chain authorisation. If absent: G2 with action 'request on-chain bound on mint volume'."
  notes: "The attacker minted at a 500x ratio relative to the deposit. An on-chain ratio invariant capped at, say, 1.05x deposit value would have made the exploit impossible regardless of off-chain key compromise. The contract had no such check."

- field_id: F-FIN-018 (proof of reserves feed)
  state_pre_incident: G2
  gap_action: "Verify a live, attestation-backed PoR feed exists with at least daily refresh AND that the issuance ceiling is bounded by the attested reserves. Static reports are G2."
  notes: "Live PoR with an issuance ceiling would have either prevented the mint or surfaced the discrepancy in real time."

- field_id: F-SEC-014 (off-chain infrastructure audit)
  state_pre_incident: G3
  gap_action: "Confirm the off-chain key management infrastructure (HSM, KMS, signing service) has been independently audited within the last 12 months. If only the on-chain contracts have been audited: G3 with action 'request scope-extended audit'."
  notes: "Resolv had 18 contract audits but the compromise route ran through GitHub → AWS KMS → key access policy modification. The on-chain audits were not asking the questions that would have caught the off-chain attack surface."

## Cross-vault recurrence

- 2025-11-xusd-stream-finance — different mechanism (off-chain fund manager misappropriation) but same diligence-gap shape: opacity in the off-chain operational layer that the on-chain contracts could not bound.
- 2022-terra-collapse — different mechanism (algorithmic dual-token), same classification (minting → depeg).

## Lessons reference

(None yet. A cross-pack lesson on "single-EOA mint authority for stablecoin issuers" is a candidate for graduation if the pattern recurs in subsequent diligence packs.)

## Notes

The Resolv team's initial public framing called this a "compromised private key" incident, which obscured the structural issue. The Chainalysis post-mortem and onchain analyst Andrew Hong's subsequent analysis identified the missing on-chain bounds as the root cause. The "compromised key" framing is correct but incomplete: the key was the proximate cause; the absence of on-chain invariants was the systemic cause. Pre-allocation diligence should treat off-chain key custody and on-chain invariants as separate fields with separate evidence requirements.

Resolv's TVL had already declined from a peak of ~$684M (Feb 2025) to ~$95M before the exploit; this is itself a diligence signal that the protocol was under stress and may have warranted closer scrutiny in any active pack.
