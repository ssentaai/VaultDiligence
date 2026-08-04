# F-STR-018

**Field ID**: F-STR-018
**Category**: Financial
**Sub-Category**: Counterparty
**Field Name**: CEX Counterparty Credit & Failure-Mode Assessment
**What to Collect / Question to Answer**: For each named hedging venue in `F-FIN-049`, what is that exchange's own solvency and failure-mode profile — does it publish proof-of-reserves (source + date), what is its insurance/backstop fund size, does it operate auto-deleveraging (ADL), what is its withdrawal-halt / socialised-loss history, and what is its regulatory/jurisdictional standing? State the fact per venue with source and date. This is the *credit-of-the-venue* question, distinct from the *how-much-is-at-each-venue* question `F-FIN-049` already answers.
**Data Type**: Structured (per venue → {proof-of-reserves: URL+date | none; insurance-fund size; ADL: y/n; withdrawal-halt/socialised-loss events: dated list | none; regulatory standing})
**Vault Types**: `Strategy = basis/funding-trade`
**Collection Tier**: T2a
**Pillar(s)**: P2 (propose; cross-refs P5) — operator confirms
**Primary Source**: Each exchange's published proof-of-reserves / insurance-fund page and terms of service; regulatory registries for the venue's operating entity
**Fallback Source**: Operator counterparty-risk disclosure naming per-venue solvency assessment; reputable reporting of venue withdrawal-halt / socialised-loss events (corroborated to a primary release)
**Evidence Pathway**: Third-party-evidenced: for each venue in `F-FIN-049`, retrieve its proof-of-reserves attestation, insurance-fund disclosure, ADL policy, and any dated withdrawal-halt / auto-deleverage / socialised-loss event, plus its regulatory registration.
**Institutional Standard**: For every hedging venue, a dated record exists of proof-of-reserves (or its explicit absence), insurance-fund size, whether ADL applies, any historical withdrawal halt or socialised loss, and the venue's regulatory standing — so the allocator sees each counterparty's failure-mode, not only the position split. (Fact to record, not a pass/fail bar.)
**Status**: Gap with action
**If Not Found — Gap Action**: Per-venue solvency facts retrieved with source + date: E. Venue named but its proof-of-reserves / insurance-fund undisclosed by the exchange: E(P), and G2 if the operator is asked and the assessment is withheld. Venue is unregulated and publishes no reserves and this is confirmed: state it as the finding (E on the absence). No venue list at all: defer to `F-FIN-049` gap. N/A only if the vault runs no CEX hedge leg.
**Source / Precedent**: FTX collapse (Nov 2022) — a delta-neutral hedge concentrated on an *insolvent* venue could not be unwound; `F-HED-001` criterion 5.1 failure-anchor. `F-FIN-049` names venues + % but assesses no venue's own credit. a synthetic-dollar issuer discloses use of multiple exchanges and custodian-mediated PnL transfer specifically to bound exchange-failure exposure (issuer documentation).
**Criterion ID(s)**: propose new under P2 (operator assigns); relates to criterion 2.6
**Cross-references**: F-STD-001/F-STD-004/F-STD-005 (party-standing of the CEX venue as a yield-critical party).
