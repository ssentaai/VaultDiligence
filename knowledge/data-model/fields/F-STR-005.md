# F-STR-005

**Field ID**: F-STR-005
**Category**: Strategy Risk
**Sub-Category**: Lending — Insolvency
**Field Name**: Bad-Debt Socialization Pathway & Loss Order
**What to Collect / Question to Answer**: Given a realized deficit in a market the vault supplies (liquidation left collateral worth less than debt), by what exact accounting is the loss borne, and in what order? Specifically: is the deficit absorbed pro-rata by the remaining suppliers of the borrowed asset via a reduction of the supply exchange rate / share price; does it draw first on a named reserve, insurance, or backstop fund before touching suppliers; and what condition triggers realization (e.g. persistent depeg, liquidation permanently unprofitable → "shadow bad debt")? Source: protocol accounting docs + the loss-realization function read on-chain.
**Data Type**: Text (socialization mechanism enumerated; loss-order / waterfall stated; realization trigger; named backstop + size if any)
**Vault Types**: Strategy = lending
**Collection Tier**: T3
**Pillar(s)**: P9 (propose; secondary P6)
**Primary Source**: Protocol bad-debt / deficit-accounting documentation + on-chain read of the loss-realization mechanism (exchange-rate write-down, deficit accounting, insurance-fund draw order)
**Fallback Source**: Governance-forum post-mortems of prior deficit events on the same protocol (cross-ref F-RIS-005, F-CUR-002)
**Evidence Pathway**: Inspection-validatable — trace how a realized deficit flows: whether a reserve/insurance fund absorbs it first, then whether the residual writes down the supply exchange rate pro-rata across remaining suppliers of that asset, and the on-chain condition under which realization occurs.
**Institutional Standard**: What a well-run vault evidences: the socialization pathway is stated explicitly — whether losses are contained to the affected market's suppliers or reach a shared backstop, the order in which a reserve/insurance fund is drawn before supplier write-down, and the trigger condition — so a supplier can see, in advance, how a co-borrower's default would reach their share price.
**Status**: Gap with action
**If Not Found — Gap Action**: Read the deficit-realization mechanism and record the loss-order (E). If the mechanism is documented but the backstop size is undisclosed, mark E(P) and name the fund. If the socialization pathway is undocumented and unreadable, classify G2 and name the loss-allocation policy required; if no isolation and no backstop exist so a realized deficit silently writes down all suppliers, record that as a G3 finding (the operator must publish the policy). Cross-ref F-FIN-081. Cross-ref F-STR-022 (reserve-adequacy facet).
**Source / Precedent**: Morpho Blue realizes bad debt pro-rata within the affected market only — it reduces the market's total borrow/supply assets and shares, socializing the loss across that market's lenders, with no protocol-wide insurance fund (`docs.morpho.org/learn/concepts/liquidation/`). Aave CRV event (Nov 2022): ~$1.6–1.7M bad debt left after a failed CRV short by the Mango exploiter; socialized until covered by an Aave governance/DAO-treasury purchase (The Defiant; a research advisory; CoinDesk).
**Criterion ID(s)**: propose 9.4 / 4.3 · RF35 (leave for ratification)
