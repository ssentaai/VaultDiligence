# F-STR-008

**Field ID**: F-STR-008
**Category**: Strategy Risk
**Sub-Category**: Lending — Vault-Share Integrity
**Field Name**: First-Depositor / Share-Price Inflation (Donation) Attack Surface
**What to Collect / Question to Answer**: Where the lending vault issues a tokenized (ERC4626-style) share, is the share-price / exchange-rate manipulable by the first-depositor "inflation" or "donation" attack — an actor minting a minimal share supply, then directly transferring (donating) a large asset amount to inflate `totalAssets` against a tiny `totalSupply`, so a later depositor's `assets × totalSupply / totalAssets` rounds down to near-zero shares and their deposit is captured? What mitigation is implemented: OpenZeppelin virtual-shares/decimals offset, a dead-shares seed deposit, or an internal-balance accounting that ignores donated assets? Source: the vault share contract source + audit report.
**Data Type**: Structured (share standard; mitigation present {virtual-shares offset | dead-shares seed | internal-balance accounting | none}; rounding-direction note)
**Vault Types**: Strategy = lending
**Collection Tier**: T2
**Pillar(s)**: P4 (propose; secondary P7 — smart-contract integrity)
**Primary Source**: Vault share-contract source code (deposit / share-mint / `totalAssets` logic) on Etherscan + the vault's audit report
**Fallback Source**: Protocol documentation stating the inflation-attack mitigation used
**Evidence Pathway**: Inspection-validatable — read the share-mint and `totalAssets` logic to see whether a direct asset transfer moves the exchange rate, and confirm whether a virtual-shares offset, a seeded dead-share, or donation-immune internal accounting is present; the attack is a code-level property of the share contract, not a market parameter.
**Institutional Standard**: What a well-run vault evidences: the share standard is stated and the inflation/donation mitigation is identified and readable in the deployed contract (virtual-shares offset, seeded dead-shares, or internal-balance accounting), so the first-depositor manipulation surface is closed by construction rather than assumed absent.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the share-mint / `totalAssets` logic and record the mitigation (E). If the source is verified but the mitigation is ambiguous, mark E(P) and cite the audit finding. If the share contract is unverified / not readable, classify G2 and name the contract requiring source verification. Where no mitigation is present on a live low-supply vault, record that as the evidenced fact for the allocator (do not score it).
**Source / Precedent**: ERC4626 first-depositor / donation / inflation attack — a known share-price-manipulation class where an attacker donates assets to move the exchange rate and capture subsequent deposits (OpenZeppelin, "A Novel Defense Against ERC4626 Inflation Attacks"; Euler Finance, "Exchange Rate Manipulation in ERC4626 Vaults"). Real incident ~$200K plus audited near-misses (Sommelier, Idle) per the same references.
**Criterion ID(s)**: propose 4.1 (leave for ratification — candidate P11 Token Mechanics once built)
