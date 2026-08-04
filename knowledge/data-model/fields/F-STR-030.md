# F-STR-030

**Field ID**: F-STR-030
**Category**: Strategy Risk
**Sub-Category**: LP/AMM — Incentive Dependency
**Field Name**: LP Incentive-Emission Dependency & Mercenary-Liquidity Flight
**What to Collect / Question to Answer**: What share of the pool's LP APR is liquidity-mining token emissions versus organic swap fees, what is the emissions schedule/end-date, and what share of the pool's TVL is emission-dependent ("mercenary") liquidity that would exit at an emissions cliff? If emissions ended, what would the pool's depth and the vault's residual IL/LVR-at-that-depth become? Distinguish the *pool's* emission dependence from the vault's own headline yield.
**Data Type**: Structured (pool fee APR vs emission APR, emissions end-date, mercenary-TVL share, post-cliff depth estimate)
**Vault Types**: Strategy = LP/AMM-provision
**Collection Tier**: T1 (DefiLlama/DEX emission + fee APR) + T3 (tokenomics/emissions schedule)
**Pillar(s)**: P6 (Yield Sustainability) primary; cross P9 (pool-TVL stability) — propose; operator confirms
**Primary Source**: DEX/DefiLlama pool APR split (fee vs reward tokens), emissions schedule from protocol tokenomics/governance; on-chain pool-TVL history around prior emission changes
**Fallback Source**: Governance-forum emissions plan; operator disclosure
**Evidence Pathway**: Inspection-validatable — the fee-vs-emission APR split and the emissions schedule are published; historical pool-TVL response to prior emission changes is on-chain and evidences mercenary-liquidity flight.
**Institutional Standard**: A well-run vault records the pool's fee-vs-emission APR split, the emissions end-date, and the share of pool TVL that is emission-dependent, plus the post-cliff depth and the vault's residual IL/LVR at that depth. A pool whose depth is majority mercenary liquidity with an approaching emissions cliff is a recorded structural fact.
**Status**: Gap with action
**If Not Found — Gap Action**: If the APR split and emissions schedule are available, record the mercenary-TVL share and post-cliff depth and classify E. If the split is known but the schedule is not, classify E(P). If neither is disclosed, classify G2/G3 per whether the data exists but is withheld (G2) or has never been produced (G3). Extends F-FIN-009 (Token Incentive APY), F-FIN-016 (Yield Source Breakdown) and F-FIN-059 (Capital Source Stickiness): those capture the *vault's* yield/depositor mix; the missing delta is the *pool counterparties'* emission dependence and the depth-collapse feedback onto the vault's LP position.
**Source / Precedent**: F-FIN-009 / F-FIN-016 (existing framework, RF14 emissions-decay logic); Anchor Protocol precedent (P6 criterion 6.1 — subsidised yield collapse). "Mercenary liquidity / mercenary capital" is an established industry term from the liquidity-mining / protocol-owned-liquidity literature rather than a single canonical paper — flagged as such.
**Criterion ID(s)**: propose at ratification; RF14 (candidate — emissions decay)
