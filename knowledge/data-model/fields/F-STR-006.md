# F-STR-006

**Field ID**: F-STR-006
**Category**: Strategy Risk
**Sub-Category**: Lending — Pool Architecture
**Field Name**: Market Isolation vs Shared-Pool Architecture
**What to Collect / Question to Answer**: For each market the vault supplies, is it an isolated market (one collateral / one loan asset, losses contained to that pair — e.g. Morpho Blue, Euler v2 vault) or a shared / cross-collateral pool where many collaterals back a common borrowable pool (e.g. Aave, Compound, or an E-Mode / cross-collateral cluster)? Where the design is shared, what is the intra-protocol contagion scope: which other collaterals or E-Mode groupings can transmit a loss or a utilisation freeze to the vault's supplied asset even though the vault has no exposure to the failing collateral? Source: protocol architecture docs + on-chain market/pool configuration.
**Data Type**: Structured (per market: isolated | shared/cross-collateral; if shared, the cross-collateral / E-Mode set that shares the borrowable pool; contagion scope described)
**Vault Types**: Strategy = lending
**Collection Tier**: T2
**Pillar(s)**: P4 (propose; secondary P9)
**Primary Source**: Protocol architecture documentation + on-chain read of the market/pool configuration (isolated market id vs shared reserve list / E-Mode grouping)
**Fallback Source**: Protocol risk dashboard identifying which assets share a pool / E-Mode category
**Evidence Pathway**: Inspection-validatable — read whether the vault's supplied asset sits in an isolated pair or a shared pool; where shared, enumerate the co-collaterals / E-Mode members that draw on the same borrowable liquidity, since a depeg or run in any of them can freeze or impair a supplier with no exposure to the failing asset.
**Institutional Standard**: What a well-run vault evidences: each market's isolation status is stated, and where the market is a shared or cross-collateral pool, the set of assets that share the borrowable liquidity and the contagion scope are enumerated — so the allocator can see whether the vault's loss surface is confined to its chosen pair or extends to co-tenants of a shared pool.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the market architecture and record isolated vs shared per market (E). Where shared, enumerate the co-collateral / E-Mode set (E, or E(P) if the grouping is only partially disclosed). If the pool membership cannot be read and is undisclosed, classify G2 and name the pool. N/A only if the vault supplies solely isolated single-pair markets (state that as the evidenced fact).
**Source / Precedent**: Morpho Blue isolated markets (loss contained to the pair) vs pooled protocols. Kelp DAO / Aave (18 Apr 2026): E-Mode treated depegged rsETH as valid, and host-pool utilisation reaching full froze ETH/USDC depositors with no rsETH exposure (Buzko Krasnov legal analysis, per F-COL-008 refinement and F-LIQ-048). Extends F-COL-008.
**Criterion ID(s)**: propose 4.5 · RF35 · cross-ref SC6 (leave for ratification)
