# VT-7 Adversarial Questions

**Applies when:** Structure in {leveraged, looped}. [Phase 3 (2026-07-09): dimension-keyed; filename retained as a historical label.]

Created: 2026-04-29



---

## DVN Configuration Question (from Kelp DAO $292M exploit, April 2026)

Source: buzko.legal/content-eng/defi-protocol-hacks-case-study
Added: 2026-04-29

Question: This protocol uses cross-chain bridge infrastructure. What is the DVN
configuration? If LayerZero: is it 1-of-1 (the Kelp default as of April 2026)?
If 1-of-1: what is the structural consequence of a single verifier compromise
given the Kelp DAO $292M precedent from April 18 2026?

Why this matters: Kelp DAO used a 1-of-1 LayerZero DVN configuration.
Attackers compromised two RPC nodes and forced failover to compromised
infrastructure. The single verifier approved a fraudulent cross-chain message.
$292M drained. LayerZero's own default configuration was 1-of-1 — used by
40% of protocols on the platform as of the exploit date.

Evidence to look for:
  Read bridge configuration on-chain. Confirm DVN count and threshold.
  Do not accept documentation claims. Verify from contract state.
  1-of-1: CRITICAL triggered condition. Kelp precedent cited.
  2-of-3 or higher: E (verified from contract state).

What closes it: On-chain confirmed multi-DVN configuration (minimum 2-of-3).
