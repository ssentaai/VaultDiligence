# F-FIN-082

**Field ID**: F-FIN-082
**Category**: Financial
**Sub-Category**: Loss Waterfall
**Field Name**: Full Ordered Loss Waterfall — Party, Amount, Sequence
**What to Collect / Question to Answer**: Which parties bear losses, up to which amount each, and in what sequence — stated as a complete ordered waterfall rather than a single senior-or-junior binary — so the allocator can locate its own position in the loss-absorption order and identify who absorbs loss ahead of and behind it?
**Data Type**: Ordered list (party -> amount/cap -> sequence rank)
**Vault Types**: ALL
**Collection Tier**: T3
**Pillar(s)**: P9
**Primary Source**: Protocol documentation + governing legal terms defining loss allocation order (extends F-FIN-069)
**Fallback Source**: Operator interview reconstructing the ordering, labelled not-confirmed-in-formal-documentation until a governing document is produced
**Evidence Pathway**: Third-party-evidenced: obtain the governing loss-allocation document and transcribe the full ordering as party, amount or cap, and sequence rank; cross-check any first-loss tranche size against on-chain balances where the tranche is on-chain.
**Institutional Standard**: A complete ordered waterfall is documented: every loss-bearing party is named, its maximum loss-absorption amount or cap is stated, and the sequence in which parties absorb loss is explicit; the allocator's own rank in that sequence is unambiguous.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the full ordered waterfall (party, amount, sequence); if only a senior/junior binary exists (F-FIN-069) without amounts and ordering, classify the ordering and amount dimensions as G2 and state that the operator must publish the complete loss-allocation order.
**Source / Precedent**: Steakhouse Financial stablecoin-issuer DDQ v1.0, section 4.10: 'Please outline which parties, and to which amount, bear any losses ... in which order.' The single most decision-relevant senior-allocator question: am I first- or last-loss, and behind whom.
**Criterion ID(s)**: 9.4
