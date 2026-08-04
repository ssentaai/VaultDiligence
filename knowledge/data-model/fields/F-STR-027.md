# F-STR-027

**Field ID**: F-STR-027
**Category**: Strategy Risk
**Sub-Category**: LP/AMM — MEV Execution
**Field Name**: MEV / Sandwich Exposure on Vault Rebalancing & Deposit/Withdrawal Swaps
**What to Collect / Question to Answer**: When the vault swaps to rebalance a range, deploy deposits, or fund withdrawals, are those transactions exposed to sandwich (front-run + back-run) extraction? What protection is in use — private orderflow / MEV-protected RPC, slippage limits, batch/auction execution, CoW/solver routing — and is there on-chain evidence of value extracted from the vault's historical swaps?
**Data Type**: Structured (protection mechanism named, slippage-limit policy, evidence of historical sandwich extraction with amounts/dates)
**Vault Types**: Strategy = LP/AMM-provision
**Collection Tier**: T2 (on-chain MEV forensics + execution-config inspection)
**Pillar(s)**: P3 (Market & Oracle Risk — price/execution) — propose; operator confirms whether P8 (Operational) is the better home
**Primary Source**: On-chain transaction forensics on the vault's historical swaps (sandwich detection via mempool/bundle analysis, e.g. MEV-attribution datasets that are independently reproducible); execution-configuration inspection (router, RPC, private-orderflow relay)
**Fallback Source**: Operator disclosure of MEV-protection design (private relay, slippage bounds, batch execution)
**Evidence Pathway**: Inspection-validatable — sandwich attacks are identifiable on-chain from the front/back-run bracketing the victim swap; the vault's execution path and slippage policy are readable from its transactions and configuration.
**Institutional Standard**: A well-run vault routes value-moving swaps through MEV-protected execution (private orderflow, tight slippage bounds, or batch/solver auctions) and can show that its historical swaps were not systematically sandwiched. Public-mempool execution with loose slippage and observable extraction is the gap.
**Status**: Gap with action
**If Not Found — Gap Action**: If execution config and swap history are available, record the protection mechanism and any evidence of extraction, and classify E. If the mechanism is disclosed but extraction cannot be checked, classify E(P). If neither the config nor history is available, classify G2 and name the transactions/relay requiring disclosure.
**Source / Precedent**: Daian, Goldfeder, Kell, Li, Zhao, Bentov, Breidenbach & Juels, "Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges", arXiv:1904.05234 (2019) — formalises and empirically evaluates sandwich attacks and MEV on DEX transactions.
**Criterion ID(s)**: propose at ratification
