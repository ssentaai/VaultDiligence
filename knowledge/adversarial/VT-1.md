# Adversarial Questions — VT-1 DeFi Lending Vaults

**Applies when:** Strategy = lending. [Phase 3 (2026-07-09): dimension-keyed; filename retained as a historical label.]

Questions that Morpho, Aave, and Compound-based vaults do not want you to ask.
Seeded from: Euler exploit (March 2023), Resolv exploit (March 2026),
Gauntlet Public Allocator incident (March 2026).
Updated after every VT-1 pack completed.

---

## Seeded Questions (from incident post-mortems)

### From Resolv March 2026

What privileged functions exist outside the main vault contract that are
not in scope for any published audit? Specifically: is there any function
that allows minting the deposit token without proportional collateral being
deposited atomically in the same transaction?

Does the out-of-scope section of every audit explicitly cover or exclude
the token issuance mechanism? State the exact clause.

Who holds the minting role? Is it an EOA, a multisig, or a contract?
What is the threshold? Has this address been used for any transaction
other than normal protocol operation?

### From Gauntlet Public Allocator March 2026

Does this vault use an automated allocation mechanism (Public Allocator
or equivalent)? If yes: what is the circuit breaker condition? At what
utilisation rate does automated reallocation halt?

If the vault reallocates automatically into a market that becomes stressed
simultaneously with a large redemption request: what is the withdrawal
path and is there a cap on how much can be reallocated into any single
market per block?

### From Euler March 2023

Does the protocol implement checks-effects-interactions pattern across
all external calls? Is there any function where an external call occurs
before the state is updated?

For each collateral asset accepted: what is the DEX depth at $10M? At
what collateral value does a liquidation become unprofitable for bots,
and what happens to bad debt when it does?

### General VT-1 Questions

What is the correlation between the collateral assets across all markets
in this vault under a simultaneous risk-off event? Has this been
stress-tested?

Who are the named individuals who can execute protocol upgrades? What is
their accountability structure if an upgrade introduces a vulnerability?

At current utilisation rate: what is the time to clear a queue of 30%
TVL withdrawals if no new deposits arrive? State the calculation.

---

## Questions Added from Completed Packs

[None yet. Add after every VT-1 pack completion.]

Format:
Pack: [vault name] | Date: [YYYY-MM-DD]
Question: [what we should have asked]
Why missed: [why it was not in the initial adversarial brief]
Evidence that would close it: [what source or document]


---

## Questions Added from Buzko Krasnov / Drift Exploit (April 2026)

Source: buzko.legal/content-eng/defi-protocol-hacks-case-study
Added: 2026-04-29
Incident: Drift Protocol $285M exploit, April 1 2026 (UNC4736 / North Korea)

Question: Who are the named multisig signers for this protocol?
What security standards govern their signing devices?
Is there a documented key management policy? What prevents a
Radiant Capital / Drift-style six-month social engineering compromise?

Why this matters: The Drift attack succeeded not through a code vulnerability
but through a six-month trust-building operation targeting human multisig signers.
Two passing audits (Trail of Bits 2022, ClawSecure Feb 2026) did not catch it.
The governance architecture — 2-of-5 multisig with no timelock — was the
exploitable surface, not the contracts themselves.

Evidence to look for:
  Named multisig signers confirmed on-chain (Etherscan gnosis-safe read).
  Signing threshold: 3-of-5 or higher = defensible. 2-of-5 or lower = material.
  Timelock on Security Council migration and governance changes: confirm duration.
  No timelock = CRITICAL triggered condition. Drift precedent is the evidence.
  Published key management policy or security standards for signers.

What closes it: On-chain confirmation of timelock duration on all governance
actions affecting user assets. Named signers with confirmed separation across
organisations and jurisdictions. Documented security standards for multisig
signers (hardware wallets, air-gapped signing environments).


---

## Multi-Vault Contagion Pattern (from Resolv USR collapse, March 2026)

Source: Coin Metrics State of the Network Issue 359, April 15 2026
Added: 2026-04-29

Question: For any collateral asset accepted by this vault — what is the
TOTAL vault exposure to that collateral across all protocols that accept it?
Not just this vault's exposure. The total ecosystem exposure.

Why this matters: When Resolv Labs' USR was exploited (March 2026), bad debt
propagated across Morpho, Euler, and Fluid vaults simultaneously because all
three accepted USR as collateral. The contagion was proportional to total
ecosystem exposure, not individual vault exposure. A small vault with modest
USR exposure was affected because other vaults' liquidations moved the market.

Evidence to look for:
  Identify the top 3 collateral assets by weight in this vault.
  For each: query DefiLlama and Morpho API for total TVL using that
  collateral across all accepting protocols.
  If total ecosystem exposure to a collateral asset exceeds 10x this
  vault's exposure: note as a contagion risk — a failure elsewhere
  in the ecosystem will affect this vault's collateral value.

What closes it: Explicit curator documentation of their collateral
whitelist rationale including ecosystem-level exposure analysis.
