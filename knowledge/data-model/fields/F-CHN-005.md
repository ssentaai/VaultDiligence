# F-CHN-005

**Field ID**: F-CHN-005
**Category**: Chain
**Sub-Category**: Chain Governance
**Field Name**: Chain Governance & Upgrade Control
**What to Collect / Question to Answer**: Who holds upgrade authority over the chain's contracts (including L2 settlement contracts), what is the multisig composition/quorum/signer identity for upgrade and pause authorities, what timelock delays gate critical upgrades, what are the pause/emergency-action authorities and their invocation conditions, and where on-chain governance is the upgrade path, what is the governance-token distribution?
**Data Type**: Structured text (upgrade authority address + type; multisig composition/quorum/signers; timelock delays; pause/emergency authorities + conditions; governance-token concentration; hard-fork change-management process)
**Vault Types**: ALL
**Collection Tier**: T1
**Pillar(s)**: P13
**Primary Source**: On-chain upgrade-authority, multisig, and timelock contracts for the chain's contracts; published chain-governance documentation; governance-token distribution from on-chain holdings
**Fallback Source**: Third-party upgrade-authority trackers (L2BEAT permissions / upgradeability section, governance dashboards)
**Evidence Pathway**: Inspection-validatable: read the chain-contract proxy admin, multisig, and timelock contracts on-chain to enumerate signer set, quorum, and timelock delay; Third-party-evidenced: cite L2BEAT permissions section for the upgrade-authority and timelock classification.
**Institutional Standard**: Disclosed upgrade authorities under honest-majority control with observation-window timelocks on production-critical upgrades; pause and emergency authorities identified with their invocation conditions; governance-token concentration scrutinised where on-chain governance is the upgrade path.
**Status**: Gap with action
**If Not Found — Gap Action**: Name the undisclosed authority (upgrade-key composition, quorum, signer identity, timelock delay, pause authority, or governance-token distribution) and request it from the chain foundation; flag single-signer or sub-honest-majority control of chain upgrade authority, or sub-day timelocks on production-critical upgrades, as critical conditions.
**Source / Precedent**: a published protocol risk framework, 9 Jun 2026, §4.5: single-signer or sub-honest-majority control of chain upgrade authorities, sub-day timelocks on production-critical upgrades, or undisclosed governance arrangements materially constrain the chain's exposure tier.
**Criterion ID(s)**: 13.5, RF45
