# F-CTR-027

**Field ID**: F-CTR-027
**Category**: Smart Contract
**Sub-Category**: Governance Controls
**Field Name**: Per-Governance-Action Timelock Coverage
**What to Collect / Question to Answer**: Does the timelock cover every privileged governance action class — not only proxy upgrades but also Security-Council/admin migrations, collateral onboarding, and parameter changes — and is any action class executable with no delay?
**Data Type**: Structured list — each entry: { action_class, timelock_seconds, executable_with_no_delay: bool }
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P7
**Primary Source**: On-chain: enumerate every privileged function and its access path, and for each confirm whether it routes through TimelockController (read getMinDelay and the scheduled-operation events) or can be called directly without delay
**Fallback Source**: Governance documentation enumerating each action class and its delay, cross-checked against the contract's role assignments
**Evidence Pathway**: Inspection-validatable: enumerate privileged actions from contract bytecode and confirm, per action class, whether each is gated by the timelock or reachable through a no-delay path such as a migration or Security-Council function.
**Institutional Standard**: Every privileged action class — upgrades, Security-Council/admin migrations, collateral onboarding, and parameter changes alike — is gated by an enforced delay, with no migration or council path that bypasses the timelock the upgrade path enforces.
**Status**: Gap with action
**If Not Found — Gap Action**: If any privileged action class is unmapped, classify G2 and require enumeration of every governance action and its delay; if any class is executable with no delay (particularly a migration or Security-Council path), state it as a no-timelock finding against RF03 and identify the exact function.
**Source / Precedent**: Drift, 1 Apr 2026: $285M lost when a social-engineered 2-of-5 multisig used a Security-Council migration path that carried no timelock — the proxy-upgrade timelock existed, but the migration action class was not covered.
**Criterion ID(s)**: 7.2, RF03
