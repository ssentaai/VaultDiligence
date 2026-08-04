---
name: defi-teardown
description: Produce DeFi-native teardown from a completed D3 pack. Same data,
  different rendering. Leads with on-chain metrics. Language for DeFi analysts
  who will verify on-chain in parallel. Maximum four paragraphs.
---

# DeFi-Native Teardown

## Prerequisite

D3 Full Diligence Pack must be complete.
Load packs/{vault-slug}/D3-full-diligence-pack.md

## Output Structure

Maximum four paragraphs. No sections. No headers.
Written for a DeFi analyst who will verify on-chain in parallel.

---

### Paragraph 1: The Numbers That Matter

Lead with: TVL, utilisation rate, withdrawable liquidity today,
net APY (share price basis only — no emissions),
LLTV per market (for VT-1), oracle last update age,
max position at 1% slippage (1inch confirmed).

No prose framing. State the numbers. Source in brackets.

### Paragraph 2: The Structure

Curator, their track record (bad debt history, named),
automated allocation (Public Allocator yes/no, circuit breaker yes/no),
governance (multisig threshold, timelock hours),
audit firm(s) and date, bug bounty ($M on Immunefi),
privileged roles enumerated (minting, pausing, upgrading — named or undocumented).

### Paragraph 3: The Risk That Matters for This Vault Type

VT-1: loop exposure multiplier, oracle type (hardcoded vs updatable),
  collateral DEX depth at $10M, Nash equilibrium utilisation threshold.

VT-3a: redemption waterfall (T+N per counterparty, total),
  deRWA wrapper (yes/no, DEX depth),
  legal structure (BVI SPC / Cayman, legal opinion yes/no).

VT-2: funding rate sustainability (days negative tolerated),
  basis spread historical max, exchange concentration.

VT-7: full protocol stack (every layer named),
  cross-protocol contagion path,
  coordinated circuit breaker (yes/no/undocumented).

### Paragraph 4: Open Gaps

State the gaps that a DeFi analyst cannot verify on-chain.
What requires a document from the operator.
What requires a human interview.
What is G3 (does not exist and needs to be created).

No judgment. Just: here is what we could not confirm and why.

---

## Output file

packs/{vault-slug}/DeFi-teardown.md

## Tone

DeFi-native. Specific. No softening. No hedging.
If something is not confirmed: say it is not confirmed.
If a condition is structurally dangerous: state the mechanism clearly.
The analyst is going to verify on-chain. Give them exactly what to look for.
