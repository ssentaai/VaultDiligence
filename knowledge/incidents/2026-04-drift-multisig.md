---
schema_version: 1
id: 2026-04-drift-multisig
title: Drift social-engineered multisig compromise and fictitious-collateral mint
date: 2026-04-01
chains: [ethereum]
protocols_directly_affected: [drift]
protocols_indirectly_affected: []
vault_types_at_risk:
  - VT-1
  - VT-7
classification: governance
loss_estimate_usd: 285000000
loss_confidence: HIGH
sources:
  - url: a legal analysis
    type: FORMAL
    retrieved: 2026-06-18
---

## What happened

On 2026-04-01 an attack attributed to North Korean state actors (UNC4736 / Lazarus) drained approximately $285M from Drift. The compromise was not a smart-contract bug. Over a roughly six-month operation beginning in Fall 2025, operatives posing as a quantitative trading firm built trust with contributors (including via real deposits and technical engagement), then delivered two compromise vectors: a malicious VS Code repository whose `tasks.json` executed on open, and a weaponised wallet application distributed through Apple TestFlight. Multisig signers were social-engineered into pre-signing transactions whose execution was delayed via durable nonces. Weeks before the attack, Security Council governance had been migrated to a 2-of-5 multisig with zero timelock on the migration path itself. A fictitious collateral token (CarbonVote / CVT) was admitted without an audit re-scope. The protocol had passed audits from Trail of Bits (2022) and ClawSecure (February 2026) — neither assessed human access controls or the governance-migration path.

## Why it matters for diligence

Two structural gaps, each individually survivable, combined into a total loss: (1) the governance/Security-Council migration path carried no timelock, so a compromised signer set could be acted on before anyone could intervene — distinct from an upgrade timelock, which existing fields measured; and (2) a new collateral token was onboarded with no audit-gated admission control. The audit record gave false comfort because audits assess code correctness, not contributor vetting, signer device hygiene, the timelock coverage of migration actions, or collateral-onboarding integrity. A pre-allocation pack would have had to ask about per-governance-action timelock coverage, multisig threshold and signer independence, contributor vetting and dev-tool restrictions, and new-collateral admission gating — none of which a code audit surfaces.

## Diligence signature

- field_id: F-CTR-027 (per-governance-action timelock coverage)
  state_pre_incident: G2
  gap_action: "Confirm a timelock gates every governance action class including Security-Council / migration paths, not just proxy upgrades. Absence on the migration path is a critical condition."
  notes: "Drift's gap was the migration path, not the upgrade path. A field measuring only upgrade timelock would have passed this vault."

- field_id: F-CTR-028 (multisig threshold & signer independence)
  state_pre_incident: G2
  gap_action: "Confirm multisig at or above the floor (at least three-of-five), with signers independent across organisations, jurisdictions, and security environments. A 2-of-5 with socially-reachable signers is a critical condition."
  notes: "Security Council was migrated to 2-of-5 weeks before the attack; signers were reachable by social engineering."

- field_id: F-COL-011 (collateral onboarding controls)
  state_pre_incident: G3
  gap_action: "Confirm new collateral admission is gated by audit re-scope, timelock, and an integrity check on the token's backing. Admission of an unaudited or fictitious token is a critical condition."
  notes: "CarbonVote / CVT was admitted without re-scope; its backing was fictitious."

- field_id: F-OPS-012 (contributor vetting & social-engineering exposure)
  state_pre_incident: G2
  gap_action: "Confirm a documented contributor-vetting policy, hardware-wallet signing, dev-tool installation restrictions, and security-awareness training. Absence is a critical condition (cf. RF42)."
  notes: "Compromise ran through a malicious VS Code repository and a TestFlight wallet app — exactly the vectors RF42 names."

## Cross-vault recurrence

- 2026-03-resolv-mint — different vector (AWS KMS key compromise) but the same diligence-gap shape: an off-chain / human-layer compromise that on-chain audits did not bound.
- Radiant (October 2024) — prior social-engineering of governance signers by the same actor class; the foreseeability anchor for this failure mode.

## Lessons reference

(None yet. A cross-pack lesson on "timelock coverage must include governance-migration actions, not just upgrades" is a candidate for graduation if the pattern recurs.)

## Notes

The facts above are drawn from the in-tree Buzko Krasnov legal analysis (Filipp Petkevitch, 2026-04-27), a published law-firm legal analysis taken as FORMAL under source-authority.md ("legal opinions"). Corroborating primary news / post-mortem URLs are not yet attached and should be added at the next D1 — flagged G2 in docs/state-of-framework-v54.md. Classification mapped to the closed incident vocabulary as `governance` (the Security-Council multisig / migration-path compromise); the vocabulary has no `key-compromise` term — a candidate vocab extension.
