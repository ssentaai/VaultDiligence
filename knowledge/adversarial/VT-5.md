# VT-5 Adversarial Questions

**Applies when:** Strategy in {staking, restaking}. [Phase 3 (2026-07-09): dimension-keyed; filename retained as a historical label.]

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


---

## a synthetic-dollar vault Oracle Single-Venue Failure (October 2025)

Source: Coin Metrics State of the Network Issue 359, April 15 2026
Added: 2026-04-29

Question: For any vault using the staked synthetic-dollar token as collateral or yield source — what
oracle source does the vault use for the staked synthetic-dollar token pricing? Does it reference
Binance specifically or a multi-source aggregated feed?

Why this matters: In October 2025, a synthetic-dollar vault fell to $0.65 on Binance due to
an internal oracle referencing a thin single-venue orderbook, despite
a synthetic-dollar issuer's collateral remaining intact. The oracle price did not reflect
actual collateral value. Liquidations triggered at incorrect prices.

Evidence to look for:
  Read oracle contract address from vault ABI.
  Confirm whether it references Binance-specific price data or
  a multi-source aggregated reference rate.
  Single-venue oracle on a thin orderbook = CRITICAL triggered condition.
  Multi-source oracle (Chainlink, CM reference rate, Pyth) = E.

What closes it: On-chain confirmed oracle contract reading a multi-source
aggregated feed. Not documentation — the actual oracle contract address.
