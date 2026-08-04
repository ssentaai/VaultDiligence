---
name: contract-reading
description: Read smart contract ABI and bytecode to enumerate privileged
  roles, upgrade mechanisms, oracle configurations, and issuance controls.
  Use for Etherscan ABI analysis on any vault contract. Runs once per contract.
---

# Contract Reading Skill

## When to Use

Any vault investigation requiring:
- Privileged role enumeration (who can mint, pause, upgrade, drain)
- Timelock configuration verification
- Oracle address and type identification
- Upgrade mechanism classification (proxy type, admin address)
- Issuance mechanism (mint/burn controls, supply cap enforcement)
- Emergency function identification

## Process

Step 1: Fetch contract ABI from Etherscan.
  URL: api.etherscan.io/api?module=contract&action=getsourcecode&address={address}
  If unverified: state evidence state G2. Do not attempt to decompile.

Step 2: Identify contract type.
  Proxy (OpenZeppelin TransparentUpgradeableProxy, UUPS, Beacon)?
  If proxy: fetch implementation address. Read implementation ABI.
  If non-upgradeable: state explicitly.

Step 3: Enumerate privileged functions.
  Functions with onlyOwner, onlyRole, onlyAdmin, onlyGovernor modifiers.
  For each: function name, caller restriction, what it can do.
  Specifically look for:
    mint() or similar issuance functions — who can call?
    pause() or emergency functions — who can call?
    upgrade() or setImplementation() — who can call?
    setOracle() or updateFeed() — who can call?
    withdrawAll() or sweep() — who can call?

Step 4: Enumerate named roles.
  AccessControl roles: DEFAULT_ADMIN_ROLE, MINTER_ROLE, PAUSER_ROLE, etc.
  For each role: who holds it? Is it an EOA, multisig, or contract?
  If multisig: what is the threshold? Fetch from Safe API if applicable.

Step 5: Identify oracle configuration.
  latestRoundData() calls — which addresses?
  Are oracle addresses hardcoded or updatable?
  If updatable: who can update? Is there a timelock?

Step 6: Check timelock.
  TimelockController.getMinDelay() — what is the minimum delay in hours?
  Who is the proposer? Who is the executor?

Step 7: Cross-reference against Resolv failure mode.
  Is there any function that allows minting tokens without proportional
  collateral being deposited in the same transaction?
  State explicitly whether such a function exists and who can call it.

## Output Format

Contract: [address]
Chain: [chain]
Verified: [Y / N]
Upgradeable: [Y / N / type]
Implementation: [address if proxy]

Privileged Functions:
  [function name] | Caller: [role/address] | Effect: [what it does]
  ...

Named Roles:
  [role name] | Holder: [address] | Type: [EOA/multisig/contract]
  ...

Oracle Configuration:
  Address: [address] | Type: [Chainlink/Pyth/custom] | Updatable: [Y/N]
  If updatable: who updates? Timelock? [hours]

Timelock:
  Min delay: [hours] | Proposer: [address] | Executor: [address]

Resolv Check:
  Uncollateralised minting function: [exists / does not exist]
  If exists: [function name] | Caller: [who]

Evidence state: [E if verified and ABI readable / G2 if unverified]
Source: api.etherscan.io/api?module=contract&action=getsourcecode&address={address}
Retrieved: [timestamp]

---


## Common Rationalizations

These are the excuses agents use to skip steps in this skill.
They are documented here so they can be recognised and rejected.

| Rationalization | Reality |
|---|---|
| "The contract is verified on Etherscan, it must be safe" | Verification means the source code matches the deployed bytecode. It says nothing about what the code does. |
| "This protocol has been audited, privileged roles are fine" | Audits check what auditors were asked to check. The Resolv privileged minting role passed 18 audits. Verify on-chain. |
| "The timelock is mentioned in the docs" | Documentation and on-chain state can diverge. Read the timelock duration from the contract directly. |
| "I know this protocol's architecture from training data" | Training data is stale. Contracts get upgraded. Read the current deployed bytecode. UNVERIFIED until verified. |
| "The proxy pattern is standard, no need to check the implementation" | The implementation address is where the logic lives. Always read the implementation, not just the proxy. |

## Verification Checklist

Exit criteria. Every item must be confirmed before the skill output
is accepted. "Seems right" is never sufficient.

- [ ] Contract verified on Etherscan: source code matches deployed bytecode. G2 if unverified.
- [ ] All privileged roles enumerated: owner, admin, guardian, pauser. Named from contract read.
- [ ] Timelock duration confirmed from contract state, not from documentation.
- [ ] Proxy pattern identified: if upgradeable, implementation address read and recorded.
- [ ] Minting functions identified: can new tokens be created? Under what conditions?
- [ ] Oracle addresses read: named oracle contracts, not assumed to be Chainlink.
- [ ] All findings from on-chain read, not from documentation or training knowledge.

## When NOT to Use

- Contract is not verified on Etherscan (use G2 gap instead).
- Field is already E in the evidence register from this session.
- The question is about legal structure, not contract architecture (use counterparty skill).

---

## Webacy Tag Vocabulary

When classifying contract vulnerabilities found during ABI read, use
the Webacy tag vocabulary (S50) for structured, consistent classification.
Source: docs.webacy.com/essentials/risk-tags

Key tags for vault investigations:

  Centralisation / privileged access:
    centralized_risk_high    — drainer-like logic present
    hidden_owner             — ownership retained after apparent renounce
    owner_change_balance     — owner can modify any wallet's balance
    pess_unprotected_initialize — initialize function not protected
    unprotected_upgrade      — contract self-destructible by owner
    can_take_back_ownership  — ownership can be reclaimed after abandonment

  Minting / supply:
    mint_high / mint_low     — arbitrary minting possible
    mintable                 — tokens can be created by minter

  Transfer / exit risk:
    is_blacklisted           — owner can blacklist any address from trading
    freezeable               — transfers can be frozen by central authority
    non-transferable         — tokens cannot be transferred between addresses

  Reentrancy:
    reentrancy_with_eth_transfer  — ETH reentrancy attack vector
    reentrancy_without_eth_transfer — token reentrancy attack vector

  Arbitrary operations:
    arbitrary_send_erc20     — approval allows attacker to drain tokens
    arbitrary_send_eth       — unprotected ETH send to arbitrary address
    selfdestruct             — contract is self-destructible

Usage rule: these tags classify what the on-chain read finds.
They are not citeable as evidence on their own.
Write: "pess_unprotected_initialize detected — verified at [etherscan URL]"
Not: "Webacy says this contract is risky"

## Self-Rewrite Protocol

After every 5 uses OR on any failure:

1. Read any recorded session learnings
   tagged with this skill name.
2. Read this skill's KNOWLEDGE.md for existing accumulated lessons.
3. Check: are there new patterns, recurring failures, or changed assumptions?
4. If yes:
   a. Append new lessons to KNOWLEDGE.md (never delete existing lessons).
   b. Update trigger phrases if a new trigger pattern has emerged.
   c. Update constraints if a safety-relevant pattern was found.
   d. Update procedures only if a step is now obsolete or incorrect.
5. If a constraint was violated during execution: escalate to
   a durable lessons record (not just this skill's local KNOWLEDGE.md).
6. Do NOT rewrite on every run. Only rewrite when evidence is clear.

Most runs produce nothing worth changing. Conservative updates only.
