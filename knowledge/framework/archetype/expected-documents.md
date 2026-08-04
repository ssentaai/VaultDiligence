# Expected-Document Sets — Archetype Routing

**Status:** archetype reference (additive; alongside dimensions.md). Built 2026-07-09,
unblocked by the archetype migration. Basis:
an internal analysis §9.

The expected-document SET for a vault is a function of its archetype tuple:
**expected-documents = f(Exposure, Management, Strategy)** (per dimensions.md). F-DOC-001
(Expected-Document Availability Matrix, P0) records the per-vault answer against this
template; each document's availability uses spec/document-availability-states.md.

The MECHANIC below generalizes across ALL archetypes; the per-archetype CONTENT is filled
in per assessment. The CLO-fund tuple (a tokenized CLO fund) is seeded in full below; other archetypes'
expected sets are a documented follow-on — same mechanic, different content.

## Routing

### ONCHAIN-base (always — every tokenized vault)
tokenization / wrapper terms · smart-contract audit(s) · oracle / NAV methodology ·
proof-of-reserves where custody is off-chain · governance / parameter documentation.

### OFFCHAIN-set (when Management = delegated-offchain-IM, or an off-chain-custodied exposure)
These belong to the YIELD-CRITICAL parties (F-STD-001); their absence is the sharpest risk:
- offering memorandum / prospectus / PPM — party: Issuer (F-ROL-002) / Investment Manager (F-ROL-003)
- IM / sub-advisory agreement — party: Investment Manager (F-ROL-003) / Sub-Advisor (F-ROL-004); yield-critical (F-STD-001)
- audited financials — yield-critical party (F-STD-005)
- custody agreement — party: Custodian (F-ROL-007)

### Exposure addenda (by Exposure class, per dimensions.md)
- **structured-credit › CLO** (the tokenized CLO fund set): tranche schedule · underlying loan / collateral schedule · rating letters · servicer / trustee reports
- private-credit: loan tape / schedule · servicer reports · borrower-concentration disclosure
- treasuries / sovereign-fixed-income: holdings attestation · custody attestation
- real-estate: property schedule · independent appraisals · SPV / title documents
- equities / corporate-fixed-income (listed, tradfi-primary): holdings + custody attestation · prime-broker agreement · issuer public filings
- commodities: warehouse / custody attestation · assay / inspection reports

### Strategy addenda (NEW — now possible via the F-STR strategy cluster)
- **basis/funding-trade**: hedge-venue / exchange terms · OES / margin-custody attestation · funding-rate history (F-STR-018/021/022; F-HED-004)
- **restaking**: AVS / operator set · slashing terms (F-STR-009/011/014)
- **lending**: market parameters · liquidation / bad-debt policy (F-STR-003/004/005/007)
- **LP/AMM-provision**: pool / position disclosure (F-STR-023..030)

### crypto-native + protocol-native -> NO offering memorandum
A fully on-chain, protocol-native vault has no delegated off-chain manager and no offchain
fund-document set; the OFFCHAIN-set is N/A. An absent OM here is CORRECT (record N/A) and
RF48 must NOT fire. This is the case the epistemic states protect against mis-flagging.

## Seeded archetype: CLO-fund (a tokenized CLO fund)

Tuple: Exposure = structured-credit › CLO · Management = delegated-offchain-IM ·
Structure = tranched · Seniority = senior · Liquidity = daily · Strategy = passive-carry.

Expected set = ONCHAIN-base + OFFCHAIN-set + structured-credit›CLO exposure addenda:
- ONCHAIN: tokenization terms; contract audit; NAV / oracle methodology; governance docs.
- OFFCHAIN (yield-critical, F-STD): OM / PPM (F-ROL-002/003); IM / sub-advisory agreement (F-ROL-003/004, F-STD-001); audited financials (F-STD-005); custody agreement (F-ROL-007).
- CLO exposure addenda: tranche schedule; underlying loan / collateral schedule; rating letters; servicer / trustee reports.
- Strategy (passive-carry): no strategy-specific addendum beyond the exposure set.

a tokenized CLO fund is the worked case: the offchain fund documents (sub-advisory agreement, audited
financials, tranche / loan schedule) belong to the yield-critical sub-advisor
(the CLO fund manager, F-STD) and are the offchain-absent surface F-DOC-001 + RF48 make visible.

## Generalization

The routing mechanic — ONCHAIN-base + OFFCHAIN-set (gated on Management / custody) +
Exposure addenda + Strategy addenda — applies to EVERY archetype. Only the CLO-fund content
is seeded here; each other archetype's expected set is filled in per assessment (a
documented follow-on), reusing this mechanic. Cross-references: dimensions.md (the tuple);
F-DOC-001 (the per-vault matrix); spec/document-availability-states.md (the states); RF48
(the finding); F-ENT-075 (executed service-provider agreements on file);
an operational due-diligence checklist (the an ODD source ODD "Document Set" source).
