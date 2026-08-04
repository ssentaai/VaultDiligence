# Critical-Document Directory & Minimum-DD Floor — Canonical Standard

**Status:** framework standard (additive; sibling to expected-documents.md). Built 2026-07-14,
per an internal analysis Finding 1. This is the canonical
required-document STANDARD the framework measures a vault against — the *yardstick*.
F-DOC-001 (Expected-Document Availability Matrix, P0) is the per-vault *measurement* against
it. Reverse-engineered from a competitor tokenized-fund note plus the allocator ODD checklist
(an operational due-diligence checklist). The competitor note defines no standard;
VaultDiligence does — that is the credibility differentiator.

This standard has two parts:

1. **The Critical-Document Directory** — the canonical set of documents that constitutes the
   minimum for credible diligence, routed by the archetype tuple, each tagged with its layer,
   owning party, and criticality.
2. **The Minimum-DD Floor** — the completeness threshold beneath which an assessment is a
   surface read, not diligence.

**Anchor-#4:** the directory is a factual reference set and the floor is a factual COUNT
against a threshold ("X of Y floor-critical documents obtained"). Neither is a score, grade,
rank, or verdict on the vault. The floor measures the DILIGENCE's completeness — never the
vault's quality. The allocator decides what any count means.

---

## How this relates to the neighbouring files (all by cross-reference; none edited)

| File | Role | This standard's relationship |
|---|---|---|
| `dimensions.md` | the archetype tuple (Exposure, Management, Strategy, …) | supplies the routing key |
| `expected-documents.md` | routing mechanic: f(tuple) -> which documents are EXPECTED | this standard adds the CRITICALITY layer (floor-critical vs supplementary) + the FLOOR on top of that routing |
| `F-DOC-001` | per-vault MATRIX: what THIS vault OBTAINED / GATED / ABSENT | measures a vault against this directory; directory = yardstick, F-DOC-001 = measurement |
| `spec/document-availability-states.md` | the availability enum (OBTAINED / GATED-CONFIRMED / EXPECTED-UNCONFIRMED / ABSENT-CONFIRMED / N/A) | how F-DOC-001 records each document's state against this directory |
| `F-ROL-*` | Counterparty & Role Registry | names the party each document belongs to |
| `F-STD-*` | Party Standing | flags whether the owning party is yield-critical |

The layering: **expected-documents.md says which documents are expected; THIS file says which
of them are floor-critical and defines the floor; F-DOC-001 records, per vault, which were
obtained.** Three layers, no duplication.

---

## Criticality vocabulary

Each document carries one criticality value. Criticality states whether a document is REQUIRED
for the diligence to count — it is a property of the DILIGENCE requirement, not a ranking of
the vault:

- **floor-critical** — must be OBTAINED for the assessment to clear the Minimum-DD Floor. Its
  absence puts the assessment below floor (a surface read, not diligence).
- **supplementary** — enriches the diligence; its absence does NOT drop the assessment below
  floor.
- **supplementary-to-critical** — supplementary by default, but RISES to floor-critical for the
  archetypes where that document is the primary risk surface (e.g. the custody agreement when
  the exposure is off-chain-custodied; the governance documentation when control is the primary
  concern). Recorded per archetype, never inferred.

Layer is **onchain** or **offchain** per the two-layer stack (an offchain-layer absence is the
sharper risk, and usually a yield-critical party's fund document). Owning party is the F-ROL
role; the F-STD flag marks a yield-critical party.

---

## PART 1 — The Critical-Document Directory (archetype-routed)

The required-document set is a function of the archetype tuple: **required-documents =
f(Exposure, Management, Strategy)** (per dimensions.md). The MECHANIC below generalizes across
ALL archetypes; the per-archetype CONTENT is seeded here for the CLO-fund / delegated-offchain-IM
archetype (which a tokenized CLO fund needs) and filled in per assessment for others — same mechanic, growing
content.

### Seeded archetype: CLO-fund (delegated-offchain-IM)

Tuple: Exposure = structured-credit › CLO · Management = delegated-offchain-IM · Structure =
tranched · Seniority = senior · Liquidity = daily · Strategy = passive-carry. (a tokenized CLO fund is the
worked case.)

#### LEGAL / STRUCTURAL — the constitutional and mandate documents (offchain)

| Document | Layer | Owning party (F-ROL) | Yield-critical (F-STD) | Criticality |
|---|---|---|---|---|
| Offering Memorandum / PPM / prospectus | offchain | Issuer (F-ROL-002) / Investment Manager (F-ROL-003) | — | floor-critical |
| Trust Agreement / Declaration of Trust / MAA (the constitutional document) | offchain | Issuer (F-ROL-002) | — | floor-critical |
| Investment Management Agreement + sub-advisory agreement | offchain | Investment Manager (F-ROL-003) / Sub-Advisor (F-ROL-004) | yes (F-STD-001) | floor-critical |
| Subscription / Investment Agreement | offchain | Issuer (F-ROL-002) | — | floor-critical |

#### FINANCIAL / PORTFOLIO — what the fund holds and how it is valued (offchain)

| Document | Layer | Owning party (F-ROL) | Yield-critical (F-STD) | Criticality |
|---|---|---|---|---|
| Audited financials | offchain | Fund; audited by Auditor (F-ROL-010) | yes (F-STD-005) | floor-critical |
| Portfolio holdings file (dated, position-level) | offchain | Fund / Investment Manager (F-ROL-003) | yes (F-STD-001) | floor-critical |
| NAV methodology / valuation policy | offchain | Administrator / NAV Agent (F-ROL-009) / Investment Manager (F-ROL-003) | — | floor-critical |

#### SERVICE-PROVIDER — who holds, administers, and registers (offchain)

| Document | Layer | Owning party (F-ROL) | Yield-critical (F-STD) | Criticality |
|---|---|---|---|---|
| Custody agreement | offchain | Custodian (F-ROL-007) | — | supplementary-to-critical (floor-critical when the exposure is off-chain-custodied) |
| Administrator agreement | offchain | Administrator / NAV Agent (F-ROL-009) | — | supplementary-to-critical |
| Transfer-agent terms | offchain | Transfer Agent (F-ROL-011) | — | supplementary-to-critical |

#### TECHNICAL — the on-chain wrapper and its verification (onchain)

| Document | Layer | Owning party (F-ROL) | Yield-critical (F-STD) | Criticality |
|---|---|---|---|---|
| Smart-contract audit report(s) | onchain | Tokenization Platform (F-ROL-006) | — | floor-critical |
| Contract addresses / deployment verification | onchain | Tokenization Platform (F-ROL-006) | — | floor-critical |

#### GOVERNANCE / OPERATIONAL — parameter control and asset proof (mixed)

| Document | Layer | Owning party (F-ROL) | Yield-critical (F-STD) | Criticality |
|---|---|---|---|---|
| Governance / parameter documentation | mixed | Governance Body (F-ROL-020) / Tokenization Platform (F-ROL-006) | — | supplementary-to-critical |
| Proof-of-reserves / attestations (where custody is off-chain) | onchain attestation of offchain assets | Custodian (F-ROL-007) / Auditor (F-ROL-010) | — | supplementary-to-critical |

### Generalization

The routing mechanic — categories × (layer, owning party, criticality), keyed off the archetype
tuple — applies to EVERY archetype. Only the CLO-fund content is seeded here. Each other
archetype's required set is filled in per assessment (a documented follow-on), reusing this
mechanic, and drawing its EXPECTED set from expected-documents.md (the Exposure and Strategy
addenda there become criticality-tagged rows here). Notably:

- **crypto-native + protocol-native** correctly has NO offering memorandum, IM agreement, or
  audited-financials row in its floor — its floor-critical set is the TECHNICAL rows (audit,
  deployment verification) plus any governance/parameter documentation. An absent OM here is
  CORRECT (N/A), not a floor breach. This matches the correct-absence logic in
  expected-documents.md, so the floor does not mis-flag a vault that legitimately has no
  offchain layer.

---

## PART 2 — The Minimum-DD Floor

The floor is the set of **floor-critical** documents that must be OBTAINED for the assessment to
count as diligence rather than a surface read. It is defined per archetype (the floor-critical
subset of that archetype's directory above).

### The two labels (factual, threshold-based)

- **Below floor** → the assessment is labelled:
  > "PRELIMINARY / below minimum-DD threshold — X of Y floor-critical documents obtained; the
  > following prerequisites are gated or absent: [list]."
- **At or above floor** → the assessment is labelled:
  > "meets minimum-DD document threshold — X of Y floor-critical documents obtained."

X and Y are a COUNT (floor-critical documents obtained / floor-critical documents required for
the archetype), read directly from F-DOC-001's availability states: a floor-critical document
counts toward X only when its availability_state is OBTAINED. GATED-CONFIRMED, EXPECTED-UNCONFIRMED,
and ABSENT-CONFIRMED do NOT count toward the floor (a gated document is a real access route, not
an obtained document — the diligence is still incomplete until it is in hand).

### CLO-fund floor (seeded)

For the CLO-fund archetype, the floor-critical set is the nine documents tagged floor-critical
above: the four LEGAL / STRUCTURAL, the three FINANCIAL / PORTFOLIO, and the two TECHNICAL. Y = 9.
The three SERVICE-PROVIDER and two GOVERNANCE / OPERATIONAL documents are supplementary-to-critical
and sit outside the floor unless the archetype raises them (e.g. custody agreement when custody is
off-chain). So a CLO-fund assessment holding, say, only the on-chain audit and deployment
verification reads: "PRELIMINARY / below minimum-DD threshold — 2 of 9 floor-critical documents
obtained; the following prerequisites are gated or absent: OM/PPM, Trust/MAA, IMA + sub-advisory,
subscription agreement, audited financials, holdings file, NAV methodology."

### The floor measures the diligence, NOT the vault (anchor-#4)

This distinction is load-bearing and must never be collapsed:

- The floor is a factual statement about **document completeness** — how much of the required
  evidence base is in hand. It is NEVER a verdict on the vault's quality, safety, or
  allocation-worthiness.
- **A vault can meet the floor and still be a bad allocation** (all documents obtained, and they
  disclose a poor structure). **A vault can sit below the floor and be sound** (its documents are
  merely gated behind an onboarding wall, not deficient). The floor tells the allocator how
  complete the DILIGENCE is, so they know how far the findings can be relied on — not what to do.
- Below-floor is a LABEL on the assessment, not a gate on the allocation. It never blocks and
  never resolves the decision (anchors #3 and #8). The allocator decides.
- The honest below-floor label is itself the credibility feature: "PRELIMINARY — 2 of 9
  floor-critical documents obtained; OM gated (G2 → DDQ)" is more useful to an allocator than a
  polished note that implies full access it does not have.

### The floor is archetype-specific

A CLO fund's floor-critical set (nine documents, OM through on-chain audit) differs from a
crypto-native protocol-native vault's floor (the technical rows only — no OM, no IM agreement, no
audited financials, because none is expected). The floor is always the floor-critical subset of
THAT archetype's directory; it is never a fixed universal list. This is why the standard is
archetype-routed and not a single global checklist.

---

## PART 3 — Relationship to F-DOC-001 (by cross-reference; F-DOC-001 not edited)

F-DOC-001 is the per-vault Expected-Document Availability Matrix. It enumerates the vault's
expected documents (from expected-documents.md) and records each one's availability state (from
spec/document-availability-states.md). **This directory is the yardstick that F-DOC-001's
expected set is measured against, and the source of each document's floor-critical / supplementary
criticality tag.** F-DOC-001 supplies the per-vault availability; this file supplies the required
set + the criticality + the floor. Together they answer "how complete is this vault's diligence?"
via the floor count.

**Follow-up (NOT done here — a later one-line cross-reference, not an edit now):** F-DOC-001 may
later gain a one-line pointer back to this file in its Source / Precedent line, and RF48's
absence-pattern count may later be expressed against the floor (floor-critical absences counted
distinctly in the operator's reading, still as a factual count, never a score). Both are additive follow-ups
recorded here so this build stays additive and edits nothing existing.

---

## Cross-references

- `dimensions.md` — the archetype tuple that routes the required set.
- `expected-documents.md` — the EXPECTED-document routing mechanic this standard tags with
  criticality and a floor.
- `F-DOC-001` — the per-vault availability matrix that measures a vault against this directory.
- `spec/document-availability-states.md` — the availability enum (only OBTAINED clears the floor).
- `knowledge/red-flags/RF48.md` — the finding raised when expected documents are
  EXPECTED-UNCONFIRMED / ABSENT-CONFIRMED.
- `F-ROL-001..020` — the party each document belongs to.
- `F-STD-001` (Yield-Critical Party Flag), `F-STD-005` (Party Financial Strength) — the
  yield-critical marking on a document's owning party.
- an operational due-diligence checklist — the allocator ODD "Document Set" source.
- `an internal analysis` Finding 1 — the finding this standard builds.
