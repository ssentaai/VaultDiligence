# F-STR-007

**Field ID**: F-STR-007
**Category**: Strategy Risk
**Sub-Category**: Lending — Risk Caps
**Field Name**: Supply & Borrow Cap Configuration and Change Authority
**What to Collect / Question to Answer**: For each market the vault supplies, what is the configured supply cap AND borrow cap (state the value, and state explicitly whether a borrow cap exists at all — its absence is itself the finding, since an uncapped borrow permits utilisation to be driven to 100%), how do those caps compare to the liquidatable on-chain depth for the collateral, and who holds the authority to change the caps under what timelock? This is the cap *configuration and control*, distinct from how full the cap currently is. Source: on-chain market cap configuration + cap-setter access control.
**Data Type**: Structured (per market: supply cap value; borrow cap value or "none"; cap-vs-liquidatable-depth comparison; cap-setter authority + timelock)
**Vault Types**: Strategy = lending
**Collection Tier**: T1
**Pillar(s)**: P4 (propose; secondary P9)
**Primary Source**: On-chain read of supply/borrow cap parameters and the cap-setter role/access control
**Fallback Source**: Protocol risk dashboard / governance parameter registry (cross-ref F-CUR-006 cap utilisation, F-FIN-035 DEX depth)
**Evidence Pathway**: Inspection-validatable — read the supply and borrow cap values and the cap-setter authority on-chain, and set the caps against the liquidatable depth for the collateral; an absent or oversized borrow cap relative to exit depth is the mechanism by which utilisation is driven to a freeze and a forced-unwind cannot clear.
**Institutional Standard**: What a well-run vault evidences: supply and borrow caps are configured and on-chain-readable per market, the presence/absence of a borrow cap is stated, the caps are recorded against liquidatable depth, and the authority + timelock to change them is disclosed — so the allocator can see the configured limit, not only its current utilisation.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the supply/borrow caps and the cap-setter authority on-chain (E). If caps are readable but the depth comparison is modelled, mark that element E(P). If a borrow cap is absent, record "no borrow cap" as the evidenced fact for the allocator. If cap parameters cannot be read and are undisclosed, classify G2 and name the market.
**Source / Precedent**: Aave introduced/tightened supply and borrow caps and delisted low-liquidity assets after the Nov 2022 CRV bad-debt event, precisely to bound the utilisation/manipulation surface (crypto.news; Aave governance). Distinct from F-CUR-006, which measures *utilisation of* an existing cap.
**Criterion ID(s)**: propose 4.5 / 9.1 (leave for ratification)
