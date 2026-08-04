# Document Availability States

The per-document availability vocabulary, recorded in F-DOC-001 (Expected-Document
Availability Matrix, P0). It is the document-level analogue of the source-registry
`access_mode` (spec/external-sources-schema.md): `access_mode` models availability on the
data-SOURCE landscape (fetch / pointer-gated / pointer-paid); this models the availability
of a SPECIFIC document for a SPECIFIC vault, one level down.

This vocabulary is ADDITIVE and sits ALONGSIDE the evidence-states
(.claude/rules/evidence-standards.md: E / E(P) / G2 / G3 / I / N/A), which are UNCHANGED.
Only ONE state here is genuinely new — EXPECTED-UNCONFIRMED; the others map onto existing
evidence-states. The evidence-states describe what a field's value is; these describe a
document's availability.

## The states

| State | Meaning | Maps to evidence-state | Finding behaviour (RF48) |
|---|---|---|---|
| OBTAINED | The document is in hand. | E / E(P) | none |
| GATED-CONFIRMED | Confirmed to exist but access-firewalled (behind onboarding, a subscription, or a form). | G2 | NEUTRAL — a DDQ item, NOT a red flag. Obtain via the access route. |
| EXPECTED-UNCONFIRMED | Standard for the vault's archetype, but its existence cannot be confirmed (we do not know whether it exists). The epistemic middle that G2/G3 cannot express. | **new — neither G2 nor G3** | Critical condition (RF48). Stronger for an OFFCHAIN document of a yield-critical party (F-STD). |
| ABSENT-CONFIRMED | Confirmed not to exist. | G3 | Critical condition (RF48); where standard for the archetype, the operator must create/publish it. |
| N/A | Not applicable to the archetype. | N/A | none |

## Why EXPECTED-UNCONFIRMED is the one new state

G2 asserts the document EXISTS (gated); G3 asserts it does NOT exist. Neither expresses
"expected for this structure, existence unknown." Evidence-standards even biases toward G3
("Challenge every G2 — most G2s are actually G3"), pushing away from the epistemic middle.
EXPECTED-UNCONFIRMED preserves the honest "we do not know", which is exactly the state an
expected-but-unlocated offchain fund document sits in. The load-bearing evidence-states and
their validators are left untouched; this enum records the document-availability layer that
G2/G3 alone conflated.

## Anchor #3 / #4

Availability is recorded as a dated state, never a score. EXPECTED-UNCONFIRMED and
ABSENT-CONFIRMED SURFACE as critical conditions via RF48; GATED-CONFIRMED does not (neutral,
a DDQ item). RF48 also records the COUNT of EXPECTED-UNCONFIRMED + ABSENT-CONFIRMED documents
(the absence pattern) as a factual count — never a computed score, never an auto-block. The
allocator decides what an absence or an absence-pattern means.

## Cross-references

- F-DOC-001 (the per-vault matrix that records these states).
- knowledge/framework/archetype/expected-documents.md (which documents are expected, routed
  off the archetype tuple).
- spec/external-sources-schema.md `access_mode` (the source-level analogue, one level up).
- .claude/rules/evidence-standards.md (the evidence-states this sits alongside, unchanged).
- an internal analysis (the reconciliation that specified this).
