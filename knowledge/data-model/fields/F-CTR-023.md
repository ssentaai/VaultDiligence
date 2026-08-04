# F-CTR-023

**Field ID**: F-CTR-023
**Category**: Smart Contract
**Sub-Category**: Circuit Breakers
**Field Name**: Automated Invariant / Stop-Loss Halt vs Manual Pause
**What to Collect / Question to Answer**: Does the system enforce a global stop-loss threshold or invariant-based halt that triggers autonomously on-chain, separate from any human-operated emergency pause, and what condition fires it?
**Data Type**: Enum: Automated invariant halt / Automated stop-loss / Manual pause only / None; plus triggering condition and on-chain location
**Vault Types**: ALL
**Collection Tier**: T2
**Pillar(s)**: P7
**Primary Source**: Contract bytecode/ABI: locate the invariant-check or stop-loss modifier and the state variable holding the halt threshold, and confirm it reverts or pauses without a privileged call
**Fallback Source**: Protocol security documentation describing the automated halt threshold and the audit section reviewing it
**Evidence Pathway**: Inspection-validatable: read the contract for an on-chain invariant or stop-loss check that halts execution on threshold breach with no human in the loop, and confirm it is distinct from the manual pause role.
**Institutional Standard**: An autonomous on-chain invariant or stop-loss halt exists with its threshold readable from contract state and fires independently of any human pauser, so protection does not depend on a person noticing an attack in time.
**Status**: Gap with action
**If Not Found — Gap Action**: If only a manual pause exists, state that as a finding (manual pause only, no automated halt) and require the operator to document why no on-chain invariant guard is feasible; if an automated halt is claimed but not locatable in bytecode, classify G2 and require the exact contract address and function.
**Source / Precedent**: Resolv, Mar 2026: Steakhouse exited the position in 41 minutes with zero depositor loss because a human caught the anomaly — an automated invariant halt would not have depended on that reaction window; the unbacked-mint condition itself triggered no on-chain stop.
**Criterion ID(s)**: 7.10, RF02
