# F-STR-024

**Field ID**: F-STR-024
**Category**: Strategy Risk
**Sub-Category**: LP/AMM — Adverse Selection
**Field Name**: Loss-Versus-Rebalancing (LVR) — Realised Adverse-Selection Cost
**What to Collect / Question to Answer**: What is the pool/position's realised loss-versus-rebalancing over a stated window — the value arbitrageurs extracted by trading the vault's stale AMM quote against the reference price — expressed as a rate (e.g. bps of position value per day or annualised) with the data source and method? LVR is the rebalancing-benchmarked cost, distinct from HODL-benchmarked IL (F-STR-023). The adverse-selection mechanism underlying LVR is toxic (informed) order flow — together with just-in-time (JIT) liquidity crowding that skims the profitable single-block flow — trading against the vault's stale quote, and it is this mechanism that erodes passive-LP fees; where reconstructable, also record the toxic-flow share and the JIT-captured fee share over the window with source. This field subsumes the former proposal-06 (toxic-order-flow / JIT-liquidity crowding) mechanism: LVR measures the realised adverse-selection cost, and the toxic-flow / JIT composition is the flow that produces it.
**Data Type**: Rate (bps/day or annualised %) + window + method + source
**Vault Types**: Strategy = LP/AMM-provision
**Collection Tier**: T2 (on-chain swap flow + reference price series)
**Pillar(s)**: P6 (Family B: Strategy Integrity) — propose; operator confirms
**Primary Source**: On-chain per-block pool reserves/price vs a reference (CEX) price series, from which the arbitrage/adverse-selection component is computed; a reproducible LVR dashboard where the method is disclosed
**Fallback Source**: Operator or third-party research disclosure of LVR with stated methodology and window
**Evidence Pathway**: Inspection-validatable — LVR has a closed-form expression given the pool's marginal-price process and reference-price volatility (Milionis et al.); it is computable from on-chain price/reserve history plus a reference feed and reproducible by a third party.
**Institutional Standard**: A well-run vault (or its curator) can state the pool's realised LVR over its live window and read it against fee income (F-STR-025). Treating fee APR as the return without acknowledging LVR is the gap; LVR is the more precise measure of the cost of providing liquidity because it isolates the arbitrage cost from directional price moves.
**Status**: Gap with action
**If Not Found — Gap Action**: If per-block pool price and a reference series are available, compute LVR and classify E. If only a qualitative acknowledgement exists, classify E(P). If neither the operator nor reproducible data yields a figure, classify G3 (the metric exists in principle but has not been produced — the operator should publish it). N/A only for pool designs with no informed arbitrage exposure (e.g. an oracle-priced pool that quotes at the reference price) — state the mechanism.
**Source / Precedent**: Milionis, Moallemi, Roughgarden & Zhang, "Automated Market Making and Loss-Versus-Rebalancing", arXiv:2208.06046 (2022, rev. 2024) — defines LVR as the adverse-selection cost from stale AMM prices picked off by better-informed arbitrageurs; the "Black-Scholes formula for AMMs". Toxic-order-flow / JIT mechanism (merged from the former proposal-06): Uniswap Labs, "Just-In-Time Liquidity on the Uniswap Protocol" (blog); "Demystifying Just-in-Time (JIT) Liquidity Attacks on Uniswap V3", IACR ePrint 2023/973 (IEEE); "The Paradox of Just-in-Time Liquidity in Decentralized Exchanges", arXiv:2311.18164 — JIT LPs provide only to uninformed orders and crowd out passive LPs, who retain the toxic residue.
**Criterion ID(s)**: propose at ratification
