# VT-8 — N/A CRITERIA GUIDANCE

VT-8 — N/A CRITERIA GUIDANCE | The following criteria should be scored N/A for standard VT-8 structures. State reason explicitly — do not leave blank. 

P4 — Collateral Quality & Liquidation Mechanics: N/A. Vault holds listed securities not DeFi collateral. No overcollateralisation ratio, no Dutch auction liquidation, no stability pool. Replace with: listed instrument price risk assessment in P6.8 concentration field. 

P5 — Hedge / Delta-Neutral Integrity: N/A unless vault explicitly hedges listed instrument price exposure. If no hedge: state N/A and note that yield is exposed to instrument price risk. 

P2 criteria 2.1-2.6 — Crypto Custody: N/A for assets held at TradFi prime broker. Replace with P2.11 TradFi Prime Brokerage Assessment. Do not attempt to assess the prime broker against crypto custodian criteria. 

P3 — Oracle Manipulation Cost & TWAP: N/A for Chainlink NAV oracle on daily-valued listed instrument. Oracle manipulation cost analysis applies to DeFi price feeds, not to Chainlink feeds on Nasdaq-listed securities. Assess P3 for update frequency, staleness, and deviation tolerance only.
TWO-DOCUMENT RULE
When a VT-7 strategy uses a VT-3/3a RWA token as collateral:

Document 1 — Collateral Asset Assessment (VT-3a). Subject = the RWA token (e.g. a tokenized CLO fund). Question: does this token meet the threshold for institutional allocation as a standalone instrument?

Document 2 — Strategy / Protocol Assessment (VT-7). Subject = the protocol (e.g. Resolv USR). P4 Collateral in Document 2 references Document 1 findings — it does not repeat the full RWA analysis.

Do not conflate the two subjects in a single assessment file.
FIVE RISK FAMILIES
Family A — Capital Safety and Legal Isolation | Is the capital actually there and is it actually mine? Legal isolation of assets, custody architecture, privileged key management, issuance mechanism integrity, smart contract security. The family that 18 audits miss because it asks architectural questions not code questions. | Legal claim, custody, segregation, bankruptcy remoteness. P1, P2.
Family B — Credit and Collateral Risk | What happens to my position in an orderly stress event? Collateral quality and concentration, recovery endogeneity (LGD is a function of liquidation size in DeFi not a fixed parameter), leverage loop exposure, issuance-layer dilution, borrower credit underwriting. | Hedge, collateral, oracle, liquidation. P3, P4, P5, P6.
Family C — Market, Oracle and Pricing Risk | Is the price the protocol uses to make decisions actually correct? Oracle design choice (DEX vs NAV vs blended), staleness risk, execution divergence at liquidation scale, NAV update frequency, market maker dependency, secondary market structure for RWA collateral. Oracle risk is a credit risk variable in DeFi, not operational noise. | Team, smart contracts, exchange. P7, P8.
Family D — Liquidity, Exit and Run Dynamics | Can I exit at fair value when I want to leave? Exit Liquidity Box (mandatory three numbers), redemption mechanics, withdrawal queue, primary market frictions for RWA collateral, full-information run dynamics (DeFi runs are faster and more complete than TradFi), leverage loop unwind at scale, automated allocation circuit breakers. | Market depth, redemption, peg, regulatory barriers. P9, P10.
Family E — Operational, Infrastructure and Governance Risk | Who controls the protocol and can they fail? Off-chain infrastructure (cloud key management, signing services), privileged role documentation and architecture, curator conflict of interest, automated allocation without circuit breakers, timelock vs stress response window, team and key person risk, governance design, regulatory and legal compliance.
SOURCE TIERS
Tier 1 — Free Public APIs | DeFiLlama, Etherscan, Immunefi, OFAC SDN, GLEIF LEI. Real-time, automatable. | Primary automation target.
Tier 2 — Partnership Required | Gauntlet Vaultbook, Accountable, Nansen, RWA.xyz premium. | G2 gap — request from named party.
Tier 2a — Third-Party Rating Reports | Particula rating reports, Steakhouse Financial. Institutional-grade secondary sources. | Cite with date. Flag as stale if >6 months old.
Tier 3 — Document Parsing | Audit PDFs, legal opinions, governance forum posts, fund docs. | G2 or G3 depending on public accessibility.
Tier 4 — Human Only | Private legal opinions, custody agreements, subscription agreements. | G2 — request from operator/allocator.
P7 TECHNICAL DESIGN CRITERIA — RWA VAULTS (7.6–7.12)
7.6 — Cross-Protocol Stack Contagion | Failure propagation across multi-protocol stacks. Hub pause → token freeze → health factor collapse → forced liquidation. | Identify all protocols in stack. Document failure cascade. State whether coordinated circuit breakers exist.
7.7 — Withdrawal / Redemption Mechanics | ERC-7540 asynchronous redemption. Queue depth limits. Admin pause capability. | State mechanism (async vs instant). Confirm max queue depth. State admin pause governance.
7.8 — On-Chain / Off-Chain NAV Linkage | NAV oracle provider, update frequency, validator decentralisation. Precedent: a tokenized CLO fund NAV fell below $1.00 July 2025 (T+2 settlement timing). | Confirm oracle, update frequency, staleness threshold. State response to NAV anomaly.
7.9 — Yield and Fee Accounting | Fee parameters on-chain vs off-chain. Off-chain = governance risk. | Confirm fee schedule location. State whether changes require governance vote with timelock.
7.10 — Guardrails and Circuit Breakers | Root contract pause function. Deposit caps. Redemption limits. Health factor thresholds. | List all circuit breakers with trigger conditions. Absence = G3.
7.11 — Governance and Permissioning | Multisig threshold, timelock, investor whitelisting, unilateral control. | State multisig config and timelock. Identify single-entity control. Confirm no unilateral admin key.
7.12 — Cross-Chain Architecture | Hub-and-spoke: hub exploit propagates to all spokes. Bridge dependencies: Wormhole, LayerZero, Axelar. | Identify all bridges. State what hub pause means for spoke-chain holders.
[SCORING GUIDE removed 2026-07-09 (Phase 3 hygiene) -- anchor-#4 violation: VaultDiligence never scores. The 4/3/2/1 PASS/WATCH/CONCERN/FAIL rubric contradicted the never-score rule and is deleted. VaultDiligence surfaces evidence; the allocator decides.]
