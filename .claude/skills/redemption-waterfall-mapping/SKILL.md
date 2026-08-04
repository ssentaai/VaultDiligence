---
name: redemption-waterfall-mapping
description: Map every counterparty in the redemption stack. State individual
  T+N for each. Sum to aggregated timeline. Name bottleneck entity at each
  stress scenario. Required for VT-3, VT-3a, VT-7, VT-8. Runs once per vault.
---

# Redemption Waterfall Mapping Skill

## When to Use

Any vault where the redemption path crosses more than one counterparty.
VT-1 (Morpho): simple — map withdrawableAssets() vs queued withdrawals.
VT-3, VT-3a: complex — fund manager, tokenisation platform, custodian, bank.
VT-7: two waterfalls — collateral asset and strategy protocol.
VT-8: TradFi-primary — fund administrator, transfer agent, custodian, settlement.

## Process

Step 1: Identify every counterparty in the redemption path.
  Read the protocol Gitbook and issuer page.
  Read the fund prospectus if VT-3a or VT-8.
  List every named entity that handles the redemption request.

Step 2: For each counterparty state:
  Entity name (confirmed from formal source)
  Role in redemption
  T+N from receipt of instruction to completion of their step
  Hours of operation (24/7 onchain vs business hours only)
  Source of the T+N claim (document name, page, URL)
  Evidence state (E if sourced, G2 if unstated, G3 if no process disclosed)

Step 3: Map standard conditions timeline.
  Sum individual T+N steps.
  Identify the longest single step — this is the bottleneck entity.
  State total T+N from depositor request to cash or stablecoin receipt.

Step 4: Map stress conditions timeline.
  Condition 1: largest single counterparty unavailable (named).
  Condition 2: underlying asset market illiquidity (for RWA vaults).
  Condition 3: banking hours restriction (for fiat settlement vaults).
  For each: what is the extended T+N? What is the bottleneck?

Step 5: Map the deRWA wrapper if present.
  Is there an onchain secondary market for the token?
  What is the DEX depth at $1M, $5M, $10M?
  Source: DexScreener + 1inch simulation.
  Is this an alternative exit or is it correlated with the primary stress?

Step 6: State the Nash equilibrium condition for this waterfall.
  At what withdrawal volume does the queue length extend such that
  first-mover advantage becomes total?
  State the calculation: [queue depth] / [daily processing capacity]
    = [days to clear at X% TVL outflow].

## Output Format

REDEMPTION WATERFALL — [Vault Name]
Assessment date: [date]

Standard Conditions:

Step | Entity | Role | T+N | Hours | Source | Evidence
-----|--------|------|-----|-------|--------|--------
1    | [name] | [role] | T+[N] | [24/7 or business] | [doc, page] | [E/G2]
2    | ...
...
TOTAL: T+[N] business days from depositor request to receipt

Bottleneck entity (standard): [name] — [T+N of their step]

Stress Conditions:

Scenario 1: [counterparty] unavailable
  Extended timeline: T+[N]
  Bottleneck: [entity]
  Source: [G2 if unstated — operator must disclose]

Scenario 2: [underlying market illiquidity / banking restriction]
  Extended timeline: T+[N]
  Bottleneck: [entity]

deRWA Wrapper:
  Secondary market: [DEX name / none]
  Depth at $1M: [$ or G2]
  Depth at $5M: [$ or G2]
  Correlated with primary stress: [Y / N / unknown]

Nash Equilibrium:
  Queue clears at: [TVL%] outflow in [N] days at normal processing rate
  First-mover advantage becomes total at: [TVL%] simultaneous withdrawal
  Source: [calculation based on processing rate from prospectus or G2]

Largest single redemption processed historically:
  Amount: [$ or G2]
  Source: [operator disclosure or G2 — request from named contact]

---


## Common Rationalizations

These are the excuses agents use to skip steps in this skill.
They are documented here so they can be recognised and rejected.

| Rationalization | Reality |
|---|---|
| "The protocol says redemptions are instant" | On-chain redemption and receipt of funds are different things. Map every counterparty T+N individually. |
| "I cannot find the redemption timeline in the docs" | Absence of disclosure is a G3 finding. State it explicitly. Do not substitute an assumption. |
| "The standard timeline is T+0 so stress timeline is not needed" | T+0 standard with T+7 stress is a material difference for a $5M position. Both are required. |
| "The fund administrator is a well-known firm, terms are standard" | Standard is not confirmed. Named firm with confirmed T+N from their fund terms is E. Assumption is UNVERIFIED. |
| "I only need the total T+N, not each counterparty" | Each counterparty T+N matters independently. The bottleneck is the slowest step, not the average. |

## Verification Checklist

Exit criteria. Every item must be confirmed before the skill output
is accepted. "Seems right" is never sufficient.

- [ ] Every counterparty in the redemption path named: depositor, protocol, fund admin, custodian, settlement.
- [ ] Individual T+N for each counterparty. Not a total only.
- [ ] Standard conditions and stress conditions both present.
- [ ] Stress condition named explicitly: what specific event causes the extended timeline?
- [ ] Source for each T+N: fund documentation, operator disclosure, or G2 if undisclosed.
- [ ] Nash equilibrium threshold stated: at what redemption size does the pool become illiquid?
- [ ] Largest single redemption processed: E if confirmed, G2 if operator has not disclosed.

## When NOT to Use

- VT-1 simple lending vault with no off-chain components (use standard liquidity assessment instead).
- Redemption data already in evidence register from this session.
- The vault type is VT-A (agent treasury): T+0 only, no waterfall mapping needed.

---

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
