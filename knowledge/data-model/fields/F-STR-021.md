# F-STR-021

**Field ID**: F-STR-021
**Category**: Contract
**Sub-Category**: Custody Architecture
**Field Name**: Off-Exchange Settlement (OES) Custody Mechanics & Exchange-Default Recovery
**What to Collect / Question to Answer**: For collateral held off-exchange while margin is mirrored to the trading venue: which custodian(s) hold the collateral, is legal title / beneficial ownership retained by the vault (not the exchange, not the OES provider) — evidenced how — what is the settlement / mirror cycle (e.g. rolling N-hour), and what is the documented process to recover PnL-at-risk and collateral if an exchange defaults mid-cycle? This is the *basis-trade OES mechanism* layer on top of the custody-chain enumeration `F-CTR-015` already requires.
**Data Type**: Structured (per custodian → {name; collateral held; title/beneficial-ownership evidence; settlement/mirror cycle; exchange-default PnL-recovery procedure})
**Vault Types**: `Strategy = basis/funding-trade`
**Collection Tier**: T3
**Pillar(s)**: P2 (propose; cross-refs P1, P7) — operator confirms
**Primary Source**: Custody / OES agreements and custodian attestations naming the collateral held and the title/settlement terms; operator custody documentation
**Fallback Source**: On-chain / custodian-published attestation of balances held per OES provider; operator disclosure with third-party verification
**Evidence Pathway**: Inspection-validatable / third-party-evidenced: confirm each OES custodian and balance from attestation, confirm title/beneficial-ownership is retained by the vault per the agreement, and read the documented settlement cycle and exchange-default recovery procedure.
**Institutional Standard**: Each OES custodian is named with its attested balance, title/beneficial ownership of the collateral is evidenced as retained by the vault (not the exchange or the OES provider), the settlement/mirror cycle is stated, and a documented exchange-default PnL-recovery procedure exists — so the counterparty-mitigation the OES structure claims is verified, not asserted. (Fact to record.)
**Status**: Gap with action
**If Not Found — Gap Action**: Custodians named, balances attested, title-retention and settlement/recovery terms evidenced: E. OES providers named but agreement terms / title-retention not reviewed: E(P). Custody chain at the funding leg undisclosed: G2 (per `F-CTR-015` gap action — a protocol that cannot enumerate its funding-leg custody is itself the finding). N/A if there is no off-exchange collateral (all collateral on-exchange — itself a finding to record, not N/A).
**Source / Precedent**: a synthetic-dollar issuer OES design — non-US institutional custody/settlement providers, "Protocol assets are never held in control or beneficially owned by the 'Off-Exchange Settlement' provider at any point," a rolling intraday settlement cycle, and reliance on custodians to "facilitate the expedient transfer of any PnL at risk with an exchange" (the issuer documentation). Resolv precedent — smart-contract-noncustodial at the top layer but a custodial OTC venue at the funding leg, exactly the layer `F-CTR-015` was written for (published vault-mechanics research; the source diligence Resolv wrong-way-risk section).
**Criterion ID(s)**: propose new under P2 (operator assigns); relates to criterion 1.4, 7.5
**Cross-references**: F-STD-001/F-STD-004/F-STD-005 (party-standing of the OES-custody counterparty as a yield-critical party).
