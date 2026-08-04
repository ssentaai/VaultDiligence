---
version: "1.0"
description: >
  Typed evidence object schema for VaultDiligence investigations.
  Every field write must produce a complete EvidenceObject.
  Any field missing required properties is rejected at write time.
  This is the type-level enforcement of the no-inference rule.
---

# Evidence Object Schema

## The Contract

No field enters a VaultDiligence pack without all five required properties
populated. Not partially. Not approximately. All five or the write is
rejected and the field is classified as G2 or G3.

This makes the evidence state system a reliable programming model.
E always means the same thing. Always.

---

## EvidenceObject (required for every field)

```json
{
  "field_id":    "F-COL-001",
  "value":       "<the confirmed value>",
  "state":       "E | E(P) | G2 | G3 | I | N/A",
  "source_uri":  "https://...",
  "source_type": "ON-CHAIN | FORMAL | EXPERT | INFORMAL",
  "retrieved_at": "2026-04-29T09:23:00Z",
  "confidence":  "HIGH | MEDIUM | LOW"
}
```

### Field Definitions

**field_id** (required)
  Must match a field ID in knowledge/data-model/fields/.
  No ad-hoc field names. No free-text descriptions.
  If the field does not exist in the registry: add it first.

**value** (required)
  The confirmed value. Exact. Not paraphrased. Not summarised.
  For numeric fields: the number with units (e.g. "847000000 USDC").
  For state=G2: the value is the name of the responsible entity.
  For state=G3: the value is what needs to be created.
  For state=I: the value is "CONFLICT: [source A value] vs [source B value]".

**state** (required)
  E:    Primary source confirmed. source_uri is the primary source.
  E(P): Partial. source_uri is the best available source.
  G2:   Restricted. source_uri is the responsible entity's URL or "NONE".
  G3:   Absent. source_uri is "NONE".
  I:    Conflict. source_uri is "CONFLICT:[uri_A]|[uri_B]".
  N/A:  Not applicable. source_uri is "N/A:[reason]".

**source_uri** (required)
  The exact URL where the value was confirmed.
  For on-chain: "https://etherscan.io/address/0x...#readContract"
                or "https://api.morpho.org/vaults/0x..."
  For G2/G3: "NONE" is the only acceptable non-URL value.
  For N/A:   "N/A:[one sentence reason]".
  NO markdown links. NO anchor text. Raw URL only.

**source_type** (required)
  ON-CHAIN: read directly from contract state or transaction history.
  FORMAL:   published documentation, regulatory filing, audit report.
  EXPERT:   published analysis from named expert, methodology stated.
  INFORMAL: blog post, tweet, forum post (rarely E, usually E(P)).

**retrieved_at** (required)
  ISO 8601 UTC timestamp of when the source was read.
  NOT the date the source was published.
  NOT today's date as a default.
  The actual moment the tool call was made.
  Format: "YYYY-MM-DDTHH:MM:SSZ"

**reasoning** (required)
  One sentence explaining why this evidence state was assigned.
  Not a description of the field. A justification of the classification.

  Examples:
    E: "TVL confirmed from Morpho API call at api.morpho.org/vaults/0x... —
       response returned typed JSON with totalAssets field, no interpretation required."
    E(P): "T+7 stress timeline stated in operator Gitbook but no formal SLA
          document exists — partial confirmation only."
    G2: "Largest redemption not in any public documentation — Steakhouse Labs
         is the named responsible party based on their operator role."
    UNVERIFIED: "Figure from agent training knowledge of Morpho protocol —
                 no API call made this session to confirm current value."

  If you cannot write a one-sentence justification: do not write the field.
  The inability to justify is the signal to re-classify or query the source.

**confidence** (required)
  HIGH:   source is unambiguous, value is exact, no interpretation required.
  MEDIUM: source requires minimal interpretation or value is approximate.
  LOW:    source is indirect, value is estimated, or source type is INFORMAL.
  If confidence is LOW and state is E: downgrade state to E(P).

---

## Optional Fields (v41)

**memory_citations** (optional, defaults to `[]`)
  List of LESSONS.md or DECISIONS.md anchors that influenced this evidence write.
  Format: `["LESSONS#auto-2026-05-12-source-conflicts", "DECISIONS#2026-04-13-redis"]`.
  An anchor is the section heading slug. Empty list means: no semantic memory was
  consulted, or no memory was relevant. Populated by the agent at write time, not
  inferred. Used to surface lessons that have not
  been cited recently — the dead-knowledge audit.

  This field is NOT used by validate-evidence. It is optional metadata for memory
  observability only. An evidence object with no memory_citations is fully valid.

**reasoning_provenance** (optional, defaults to `null`)
  When the reasoning text was directly informed by a specific lesson, cite it:
  `"LESSONS#auto-2026-05-12-source-conflicts"`. This is more specific than
  memory_citations and is used to attribute *which* lesson did the work.

---

## Optional Fields (v42)

**agent_id** (optional, defaults to `'unknown'` when stamped by the writer)
  Which subagent produced this evidence object. One of: `A1`, `A2`, `A3`, `A6`,
  `A-VERIFICATION`, or `unknown`. Stamped automatically by `write_field()` and
  then carried through any subsequent disambiguation. Never modified after
  the first write.

**write_history** (optional, populated by `write_field()` not the agent)
  An ordered list of write events on this evidence object:

  ```json
  "write_history": [
    {
      "agent_id":  "A1",
      "action":    "created",
      "at":        "2026-05-12T10:14:00Z"
    },
    {
      "agent_id":  "A2",
      "action":    "overwritten-by-tier",
      "at":        "2026-05-12T10:42:00Z",
      "rationale": "incoming source_type=FORMAL outranks existing INFORMAL",
      "superseded_source": {
        "uri":          "https://substack.com/...",
        "value":        "Steakhouse Labs",
        "source_type":  "INFORMAL",
        "retrieved_at": "2026-05-12T10:14:00Z",
        "agent_id":     "A1"
      }
    },
    {
      "agent_id":  "A6",
      "action":    "downgraded-state",
      "at":        "2026-05-12T11:02:00Z",
      "rationale": "depth-3 source chain, terminal source not on-chain"
    }
  ]
  ```

  Action values:
  - `created` — first write of this field
  - `overwritten-by-tier` — disambiguation: incoming had higher source-tier
  - `overwritten-by-recency` — disambiguation: same tier, incoming newer
  - `inherited-incoming-discarded` — existing won, incoming attempt logged
  - `conflict-recorded` — disambiguation could not resolve, state forced to I
  - `downgraded-state` — A6 verification downgraded the state

  Read this field to answer audit questions like "is A2 systematically
  overwriting A1's evidence" or "which agent's evidence survived A6 review."

---

## Disambiguation rules (v42)

When `write_field()` is called for a field that already has a value, and the
incoming evidence object disagrees with the existing one, the validator
applies these rules in order:

1. **Source-tier wins.** ON-CHAIN beats FORMAL beats EXPERT beats INFORMAL.
   The higher-tier evidence object becomes the register entry. The lower-tier
   one is recorded in `write_history.superseded_source`.

2. **Within the same source-tier, recency wins.** The evidence object with
   the more recent `retrieved_at` becomes the register entry.

3. **If neither rule produces a winner**, the state is forced to `I`. Both
   sources are retained in the conflict object's `conflict.source_a` and
   `conflict.source_b`. The agent (or A3) must re-query against a
   higher-authority source to resolve.

This is deterministic — the same inputs always produce the same outcome.
The rules cannot silently resolve genuinely conflicting evidence; rule 3
is the safety valve that says "two equally-authoritative sources disagree,
this is an investigation problem, not a coding problem."

See `spec/evidence-disambiguation.md` for worked examples.

---

## Rejection Rules

The following writes are rejected. The field defaults to G2 or G3.

1. Missing source_uri when state = E or E(P).
2. Missing retrieved_at (any date will not do — it must be the actual retrieval time).
3. state = E with source_type = INFORMAL.
4. state = E with confidence = LOW.
5. value = null or value = "" or value = "unknown" or value = "N/A" when state = E.
6. source_uri is a markdown link, not a raw URL.
7. retrieved_at is a date only (YYYY-MM-DD) not a datetime (YYYY-MM-DDTHH:MM:SSZ).

When a write is rejected: classify as G2 if the information exists but
could not be confirmed. Classify as G3 if the information does not exist.
State the rejection reason in the gap action field.

---

## Conflict Object (for state = I)

When two sources produce different values for the same field:

```json
{
  "field_id":    "F-FIN-010",
  "value":       "CONFLICT: 847000000 USDC vs 851000000 USDC",
  "state":       "I",
  "source_uri":  "CONFLICT:https://api.llama.fi/protocol/morpho|https://app.morpho.org",
  "source_type": "ON-CHAIN",
  "retrieved_at": "2026-04-29T09:23:00Z",
  "confidence":  "LOW",
  "conflict": {
    "source_a": {
      "uri":          "https://api.llama.fi/protocol/morpho",
      "value":        "847000000",
      "retrieved_at": "2026-04-29T09:20:00Z"
    },
    "source_b": {
      "uri":          "https://app.morpho.org",
      "value":        "851000000",
      "retrieved_at": "2026-04-29T09:23:00Z"
    },
    "resolution_action": "Verify against on-chain totalAssets() call on 0x..."
  }
}
```

Conflict objects are never silently resolved. They always appear in the
gap register with a specific resolution action.

---

## One Source Per Field Rule

If Agent 1 has already written a confirmed E for field F-FIN-010,
Agent 3 must inherit that value. Agent 3 does not re-query the same field.

This prevents the FMA precision violation: two computations of "the same thing"
from slightly different sources at different times producing values that diverge
downstream in the loss scenario calculation.

Inheritance rule:
  Before querying any field: check if it is already in the session
  evidence register with state = E.
  If yes: inherit. Do not re-query.
  If no: query and write.

The session evidence register is written to:
  packs/{vault-slug}/agent-outputs/evidence-register.json

All agents read from this file before querying any field.
All agents write to this file after confirming any field.

---

## Validator

```python
# scripts/validate-evidence-object.py
# Call before writing any field to the evidence register.

REQUIRED_FIELDS = ['field_id', 'value', 'state', 'source_uri',
                   'source_type', 'retrieved_at', 'confidence', 'reasoning']

VALID_STATES = ['E', 'E(P)', 'G2', 'G3', 'I', 'N/A']
VALID_SOURCE_TYPES = ['ON-CHAIN', 'FORMAL', 'EXPERT', 'INFORMAL']
VALID_CONFIDENCE = ['HIGH', 'MEDIUM', 'LOW']

REJECTION_RULES = [
    lambda e: e['state'] in ['E', 'E(P)'] and not e.get('source_uri'),
    lambda e: not e.get('retrieved_at') or len(e['retrieved_at']) < 19,
    lambda e: e['state'] == 'E' and e.get('source_type') == 'INFORMAL',
    lambda e: e['state'] == 'E' and e.get('confidence') == 'LOW',
    lambda e: e['state'] == 'E' and not e.get('value'),
    lambda e: e.get('source_uri', '').startswith('['),  # markdown link
    lambda e: not e.get('reasoning') or len(e.get('reasoning','')) < 10,  # no justification
]

def validate(evidence_object: dict) -> tuple[bool, str]:
    for field in REQUIRED_FIELDS:
        if field not in evidence_object:
            return False, f"Missing required field: {field}"
    if evidence_object['state'] not in VALID_STATES:
        return False, f"Invalid state: {evidence_object['state']}"
    if evidence_object['source_type'] not in VALID_SOURCE_TYPES:
        return False, f"Invalid source_type: {evidence_object['source_type']}"
    if evidence_object['confidence'] not in VALID_CONFIDENCE:
        return False, f"Invalid confidence: {evidence_object['confidence']}"
    for i, rule in enumerate(REJECTION_RULES):
        if rule(evidence_object):
            return False, f"Rejection rule {i+1} triggered"
    return True, "valid"
```
