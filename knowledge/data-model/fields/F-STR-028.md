# F-STR-028

**Field ID**: F-STR-028
**Category**: Strategy Risk
**Sub-Category**: LP/AMM — Pool Concentration
**Field Name**: Vault Share of Pool TVL & Pool-Depth Concentration
**What to Collect / Question to Answer**: What share of the target pool's total liquidity does the vault's LP position represent, and what is the pool's total TVL/depth? At the vault's position size, what price impact would exiting or halving the position cause, and is the vault the marginal (last-in) liquidity the pool depends on? Name the pool, its contract address, its TVL, and the vault's share.
**Data Type**: Structured (pool named + address, pool TVL, vault share of pool %, exit price impact at position size)
**Vault Types**: Strategy = LP/AMM-provision
**Collection Tier**: T1 (on-chain pool state + position size)
**Pillar(s)**: P9 (Liquidity, Peg & Exit Infrastructure) — propose; operator confirms
**Primary Source**: On-chain pool reserves/liquidity and the vault's position size read from the pool and position-manager contracts; DEX/DefiLlama pool TVL
**Fallback Source**: DEX analytics pool page; operator disclosure of position size and pool share
**Evidence Pathway**: Inspection-validatable — pool TVL, the vault's liquidity share, and the simulated price impact of an exit at position size are all readable/derivable from on-chain pool state.
**Institutional Standard**: A well-run vault records its share of the pool it provides into, the pool's total depth, and the price impact of exiting at its position size. A dominant share of a thin pool (the vault is the liquidity) or a pool too shallow to absorb an exit at position size is a recorded structural fact for the Exit Liquidity Box.
**Status**: Gap with action
**If Not Found — Gap Action**: If pool state and position size are available, compute the share and exit price impact and classify E. If pool TVL is available but the vault's share is not disclosed, classify E(P). If pool state is not readable and undisclosed, classify G2 and name the pool. Cross-reference F-LIQ-041 (Within-Venue LP Diversity — depth of venues where the *vault token* trades) and F-FIN-001 (headline TVL): this field concerns a different object — the vault's own share of the *pool it LPs into*.
**Source / Precedent**: Cross-references F-LIQ-041 precedent (a published protocol risk framework §1.5, 9 Jun 2026: LP diversity within a venue is the primary structural concern). The vault-as-dominant-LP / thin-pool exit-impact angle is the strategy-specific extension. General AMM price-impact mechanics; illustrative, no single canonical paper — flagged as such.
**Criterion ID(s)**: propose at ratification (adjacent to 9.1)
