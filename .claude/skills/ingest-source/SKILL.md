---
name: ingest-source
description: |
  Structured methodology for ingesting external source material (industry
  research, methodology documents, market commentary, incident post-mortems,
  regulatory filings) and deciding how — or whether — it should update the
  VaultDiligence framework, data model, output specs, or platform delivery.
  Distinguishes "genuinely novel" from "restating known" before any backlog
  work. Forces registry audit before scoping new fields. Enforces
  ingestion-rate gate to prevent unvalidated-backlog accumulation. Required
  output is a structured ingestion record that ships to fixes.md or is
  explicitly rejected with documented reasoning.

  This skill is for EXTERNAL SOURCES that may improve the framework. It is
  NOT for operator-supplied raw material that is itself evidence about a
  specific vault (audit reports, vault documentation, regulatory filings
  on a specific protocol). Those flow through A1/A2's normal evidence
  collection, not this skill.

triggers:
  - ingest source
  - new methodology document
  - new research paper
  - new article
  - new framework
  - market commentary
  - incident post-mortem
  - industry standards
  - check against framework
  - what can we learn from this
  - does this change vaultdiligence
  - rating methodology
  - operator-side commentary

constraints:
  - Never ship fixes from an ingestion if INGESTION_RATE_GATE fails.
    Five ingestions without intervening D1 reality testing = automatic
    defer of all subsequent ingestions until D1 ships.
  - Never propose new fields without running the REGISTRY AUDIT phase
    first. The registry has 265 fields across 20 families; new field
    proposals must be checked against existing coverage before scoping
    effort.
  - Never produce ingestion analysis without explicitly classifying the
    source's author and incentive. Vendor positioning a product produces
    different signal than independent analysis. Both can be useful but
    must be disclosed.
  - Never collapse the four output dimensions into one. Every ingestion
    must explicitly assess impact on: field registry / methodology and
    specs / output presentation / platform delivery. If three of four
    dimensions are empty, the source is probably restating known
    knowledge and the ingestion record should say so.
  - Never ship a fix as immediate-ship if effort estimate exceeds 4
    hours OR if scope depends on unshipped fixes OR if the gap is
    speculative (resolves a hypothetical, not a known issue). All such
    fixes defer to post-D1 triage.
  - Never produce an ingestion record without anticipating sharp-operator
    pushback. The record must explicitly answer "what would a sharp
    operator critique about this analysis?" before being submitted.
  - Never treat ingestion-derived fixes as validated. They are
    speculative until first D1 reality data confirms or refutes them.
    The ingestion record states this explicitly.
---

# Ingest-Source Skill

When the operator brings external source material to assess against the
VaultDiligence framework, this skill is the protocol. It is a seven-phase
methodology that produces a structured ingestion record. The output is
one of:

1. **Ship now** — meets all immediate-ship criteria; create a versioned
   fix and ship as the next version
2. **Defer to post-D1 backlog** — real gap but doesn't meet immediate-ship
   criteria; create a backlog entry in fixes.md with structured framing
3. **Reject** — source doesn't produce a real framework improvement;
   document the rejection in the running ingest log so
   the question is closed and the source isn't re-litigated later

This skill exists because eight ingestions in three days (May 2026)
revealed five failure modes in conversation-dependent ingestion:
inconsistent depth, vibes-based ship/defer decisions, no scoping audit
before estimating, no platform/delivery dimension, no rate gate. This
skill is the response.

The skill is bias-toward-defer. Most market commentary should defer.
Shipping immediately requires explicit justification under tight criteria.

## Phase 1 — Source classification

Before reading deeply, classify the source on five dimensions. Write
these classifications into the ingestion record. They calibrate
expectations for the rest of the analysis.

**Source type:**
- Methodology document (e.g., Moody's stablecoin rating methodology) — analytical machinery, high signal-to-noise typically
- Market commentary (e.g., a risk-infrastructure provider research piece) — opinion + analysis mixed, must separate
- Incident post-mortem (e.g., KelpDAO/LayerZero analysis) — concrete failure modes, high signal typically
- Operator-side narrative (e.g., Centro/Centura webinar) — production reality, high signal but heavy positioning
- Vendor pitch (e.g., InsForge product page) — positioning a product; lower signal unless we're evaluating that product
- Academic paper — high analytical rigor, possibly impractical
- Regulatory filing — structural requirements, high signal for compliance dimensions
- Job description — adjacent role at adjacent company; limited signal for framework
- Aggregated thread (e.g., Pharos pmUSD thread) — distilled findings, very high signal typically

**Author and incentive:**
- Who wrote this?
- What's their commercial incentive? (vendor pitching product / independent analyst / regulator with mandate / academic seeking citation / operator describing their work to attract clients)
- Does the incentive distort the substantive claims? Note specifically what to discount and what to credit.

**Publication date relative to v52 cutoff:**
- Pre-v40 (April 2026 or earlier) — content may have been incorporated into existing v40-v52 architecture
- Post-v40 (after April 2026) — newer than current framework
- Future-looking (predictions/thesis) — discount accordingly

**Substantive density (estimated):**
- High density methodology — typically produces multiple genuine fixes (Moody's, Egalite)
- Synthesis of existing arguments — typically produces incremental fixes or none (a risk-infrastructure provider piece in May 2026 retrospect)
- Single-finding analysis — typically produces one fix (specific incident analyses)
- Position paper — typically produces zero direct framework fixes; may produce strategic insight

**Prior probability of real framework improvement:**
A rough estimate before reading. Calibrate against the eight May 2026
ingestions: high-confidence-novel sources (Moody's, Egalite, Pharos
thread) produced major fixes; medium-confidence sources (Centro,
bridge-risk article) produced 2-4 fields each; low-confidence sources
(a risk-infrastructure provider, Morpho job description) produced 2-3 minor candidates.
Be honest about prior expectations before reading.

If prior probability is very low AND the source type is "vendor pitch"
or "job description," consider whether to invest deep-read time at all.
A 5-minute scan-and-reject is sometimes correct.

## Phase 2 — Claim extraction (forced before analysis)

List the substantive claims in the source, separated from positioning,
marketing language, and editorial framing. A claim is a falsifiable
statement about the world ("bridge exploits dominate 2026 stolen-value
rankings"), not an opinion or aspiration ("the industry needs minimum
verification standards").

For each claim, classify:
- **Novel** — not currently encoded anywhere in v52 (the core rules, fixes.md
  shipped fixes, field registry, specs, principles)
- **Restated** — duplicates existing framework content; one-line note and
  drop from further analysis
- **Refinement** — sharpens or extends existing framework content; flag
  as candidate amendment, not new addition
- **Contradicts existing** — disagrees with current VaultDiligence
  architecture or principle; requires explicit reconciliation, NOT silent
  override

Only claims classified as "novel" or "refinement" or "contradicts" advance
to Phase 3. Restated claims are dropped with a note.

If all claims are "restated," the ingestion record is short: source
restates existing knowledge, no framework changes. This is a valid and
common outcome.

## Phase 3 — Cross-walk against existing framework (MANDATORY audit)

For each surviving claim from Phase 2, run the registry audit BEFORE
scoping effort. This is the step that prevented Fix 84/85 from being
shipped at 16-20 hours when actual scope was 3 hours.

Walk the actual codebase:

1. **Field registry** (knowledge/data-model/fields/):
   ```
   ls knowledge/data-model/fields/F-{relevant}-*.md
   grep -li "{concept}" knowledge/data-model/fields/*.md
   ```
   For every novel claim that proposes a "new field," check whether the
   concept is already in the registry. The registry has 265 fields. Most
   "missing" concepts are actually present under different names.

2. **Specs** (spec/):
   ```
   grep -li "{concept}" spec/*.md
   ```
   Check whether the claim is addressed in verdict-block-spec.md,
   yield-source-classification.md, agent-scopes.json, etc.

3. **Principles** (the core rules):
   Check whether the claim is covered by an existing load-bearing
   principle (no-scores, no-blocking, structured-output-first, one-source-per-field,
   UNVERIFIED flag, four agents, source-tier hierarchy).

4. **Pending backlog** (fixes.md):
   Check the pending fixes list to avoid proposing something that's
   already on the backlog from a prior ingestion.

5. **Shipped fixes** (fixes.md, status SHIPPED):
   Check whether the claim duplicates work already done in v45-v52.

Output of Phase 3: per claim, explicit classification of:
- "Covered by [specific field IDs / spec / principle / shipped fix]"
- "Partially covered by [X], gap is [specific delta]"
- "Genuine gap not in v52"
- "On backlog as [Fix N], duplicates"

Only "genuine gap not in v52" claims advance to Phase 4.

## Phase 4 — Gap classification and effort estimation

For each genuine gap, produce structured classification:

**Type:**
- Field addition (1 field)
- Field cluster (2-5 related fields, same family)
- New family (5+ fields, new prefix)
- Methodology document
- Spec amendment (e.g., verdict-block-spec.md)
- Principle addition (the core rules)
- Output presentation (rendering / display)
- Platform delivery (API / interactive / PDF export)
- Process/discipline (skill, workflow, automation)

**Scope and effort:**
- Estimate hours to ship AFTER registry audit, not before
- Be honest about historical accuracy: Fix 63 was 1h estimated, 2h actual;
  Fix 84/85 was 16-20h estimated, 3h actual. The audit reduces
  overestimates; the lived experience reduces underestimates.
- For estimates above 8 hours, decompose into sub-fixes before estimating

**Dependencies:**
- What other shipped fixes does this depend on? (e.g., Fix 70 source
  registry must exist before per-source confidence scoring)
- What other PENDING fixes does this depend on?
- What requires D1 reality data to scope correctly?

**Buyer impact:**
- Which audience does this serve? (Allocator / agent / issuer / internal
  operator)
- Without this, what specifically is the buyer missing?
- Is this load-bearing for IC-defensibility (the vaultdiligence.io promise)?

## Phase 5 — Ship vs defer decision (RULE-BASED, not vibes)

Apply the ingestion-rate gate FIRST.

**Ingestion rate gate:**
Read the running ingest log. Count ingestions since the
last validated D1 (or since project inception if no D1 has run yet).

If count >= 5: ALL further ingestions defer to post-D1 triage,
regardless of how "obviously good" the fix seems. The lesson from
May 2026 is that ingestion-without-reality-testing produces accumulating
speculative backlog that mostly doesn't survive D1 contact.

If count < 5: continue to per-fix evaluation.

**Per-fix immediate-ship criteria (ALL must be true):**
1. Required effort under 4 hours
2. No dependencies on unshipped fixes
3. Affects content quality of first D1 output (or whatever the next
   diligence pack is)
4. Doesn't require D1 reality data to scope correctly
5. Source is methodology document, incident post-mortem, or regulatory
   filing — NOT market commentary or vendor pitch
6. Cross-walk in Phase 3 confirmed gap is real, not duplication

**If ALL six criteria met:** ship-now candidate. Create a versioned fix
(v53, v54, etc.), follow standard ship sequence (fix, test, CHANGELOG,
tar update).

**If ANY criterion fails:** defer to post-D1 backlog. Create entry in
fixes.md following the structured template in Phase 7.

This is bias-toward-defer by design. The discipline matters more than
shipping every plausible fix.

## Phase 6 — Multi-dimensional impact assessment

Even for deferred fixes, the ingestion record must explicitly assess
impact across four dimensions:

**1. Field registry** — what data should be collected?
   - New fields proposed (with proper IDs)
   - Existing fields to amend
   - Field families to extend

**2. Methodology and specs** — how should analysis be done?
   - New spec documents
   - Amendments to existing specs (verdict-block-spec.md,
     yield-source-classification.md, etc.)
   - Principle additions to the core rules

**3. Output presentation** — how should findings be rendered?
   - Document structure changes
   - Cross-walk sections (Fix 95 territory)
   - Per-evidence-state rendering rules
   - Charts and visual elements
   - Cover/header/provenance sections

**4. Platform delivery** — how does the report reach the buyer?
   - PDF / interactive web / API / hybrid
   - Three-audience render variants (allocator / agent / issuer)
   - Authentication and access patterns
   - Real-time data refresh patterns (structured-output 30d auto-renew)

**If three of four dimensions are empty for this ingestion:** the source
is probably restating known knowledge. The ingestion record should say
so explicitly. Most market-commentary sources hit this pattern.

**If all four dimensions are populated meaningfully:** this is a major
source. Treat it accordingly with deeper scrutiny.

## Phase 7 — Backlog entry with structured framing

If deferred: append to fixes.md using this template.

```markdown
---

### Fix N: [Source name and primary insight]

**STATUS: DEFERRED until after first D1. [Or "SHIPPED in v53" if immediate-ship.]**

Origin: [Date] ingestion of [source name and author]. [One-sentence
honest framing of what this source is.]

Author and incentive disclosure: [Who wrote this and what their
commercial interest is. Honest read on whether the incentive distorts
the substantive claims.]

What this fix is, with honest framing:
[2-3 sentences. NOT marketing-shaped. NOT "this insight changes
everything." Specifically what the source surfaced and what it doesn't.]

Cross-walk results (Phase 3 output):
- Claim 1: [covered by / partially / genuine gap]
- Claim 2: ...
- (Drop "covered by" and "restated" claims from full entry — note in
  one line if useful)

Genuine gaps identified:

  1. [Gap description]
     Type: [field / spec / principle / presentation / platform / process]
     Scope: [single field / cluster / new family / spec / etc.]
     Effort estimate: ~X hours
     Dependencies: [list]
     Buyer impact: [allocator / agent / issuer / operator]

  2. [Next gap...]

Multi-dimensional impact (Phase 6 output):
- Field registry: [populated or empty]
- Methodology/specs: [populated or empty]
- Output presentation: [populated or empty]
- Platform delivery: [populated or empty]

Triage approach (post-D1):
[Specific guidance for when to revisit. What D1 output would confirm
the gap is real? What would refute it?]

Sharp-operator pushback anticipation:
[Explicitly state what a sharp operator would critique about this
ingestion. Then address it. This is the step that produces honest
analysis on the first pass instead of waiting for operator complaint.]

What this fix is NOT:
- [Explicit anti-scope. What this fix does not commit to.]
- [What this fix does not change.]
- [What deferral does not imply.]

Cross-references:
- Related field families: [...]
- Related shipped fixes: [...]
- Related pending fixes: [...]
- Source: [URL or document identifier, date]

```

If shipped: same template but with SHIPPED status and CHANGELOG-vN.md
notation.

After every ingestion, append a one-line entry to
the running ingest log:

```
2026-05-DD | [source name] | [author] | [outcome: shipped vN / deferred as Fix N / rejected]
```

This is the data the ingestion-rate gate reads.

## Anti-patterns this skill prevents

The May 2026 ingestion-without-discipline pattern produced these
failure modes. The skill prevents each:

**1. Inconsistent depth.** Phase 1 (source classification) sets explicit
expectations before reading. Phase 6 (four-dimension impact) prevents
shallow analysis from being recorded as if it were thorough.

**2. Vibes-based ship/defer.** Phase 5 has rule-based criteria. Six
explicit conditions, ALL must be true for immediate ship.

**3. No scoping audit before estimating.** Phase 3 is mandatory.
Effort estimates only produced AFTER registry audit.

**4. No platform/delivery dimension.** Phase 6 requires four-dimension
assessment. Three-empty-dimensions triggers explicit "restating known
knowledge" outcome.

**5. Diminishing returns not caught early.** Phase 5's ingestion-rate
gate hard-stops at 5 ingestions without D1 reality testing.

**6. Operator-pushback-dependent quality.** Phase 7's template requires
anticipating sharp-operator pushback BEFORE submitting the analysis.

## When this skill is used

- New industry research/methodology arrives — primary use
- Operator brings article/transcript/document — primary use
- Reviewing accumulated backlog post-D1 — also applies; triage existing
  Fix 90-97 entries through the same lens for prioritization

## When this skill is NOT used

- Operator-supplied raw material that IS evidence about a specific vault
  (audit reports, vault documentation, regulatory filings on a specific
  protocol). Those flow through A1/A2's normal evidence collection.
- Internal VaultDiligence documentation changes (the core rules edits driven by
  operator decision, not external source).
- Code fixes driven by observed runtime behavior (bug reports, test
  failures, hook errors).

## Relationship to the `/ingest` slash command

The `/ingest` slash command (.claude/commands/ingest.md) and this skill
have overlapping subject matter but serve different purposes:

- **`/ingest`** captures a source's content for future investigation
  reuse. Output goes to `knowledge/research/{slug}.md`. A1/A2 read
  this at the start of relevant vault investigations. Lightweight;
  one-pass extraction. Side effect: flags potential framework-review
  items to `knowledge/research/framework-review-queue.md`.

- **`ingest-source` (this skill)** decides whether a source should
  update the FRAMEWORK ITSELF (fields, specs, principles, output
  presentation, platform delivery). Heavyweight; seven-phase
  methodology with registry audit and ingestion-rate gate.

The two are not duplicates. The `/ingest` command builds the knowledge
graph that agents read from. This skill decides whether the framework
itself should change. Most sources need only `/ingest`. A minority of
sources (methodology documents, major incident post-mortems, new
analytical primitives) warrant the heavier treatment of this skill IN
ADDITION to `/ingest`.

Typical operator workflow for a substantively novel source:
1. Run `/ingest URL` first — captures the source in the knowledge
   graph; produces research note with `framework_review_flagged: true`
   if the source suggests framework changes
2. If framework_review_flagged is true, then invoke this skill (the
   `ingest-source` skill) to run the disciplined seven-phase
   methodology and produce a ship/defer/reject decision

Sources that produce only knowledge-graph capture (most sources) skip
this skill entirely. Sources that produce framework changes go through
both.

## Examples

**Good ingestion outcome (a risk-infrastructure provider piece, May 2026):**
- Phase 1: market commentary, vendor (a risk-infrastructure provider positioning their analytics
  product), May 2026, synthesis of existing arguments, low-medium prior
  probability of novel framework input
- Phase 2: 8 claims; 5 restated (yield decomposition, concentration,
  curator quality, AI-curation thesis, stress simulation), 3 candidate
  novel (rate sensitivity, cross-asset correlation, automation
  generation classification)
- Phase 3: 3 candidate novel claims; rate sensitivity → genuine gap;
  cross-asset correlation → genuine gap distinct from F-COL-008;
  automation generation → genuine gap, structural primitive
- Phase 4: 3 fields, F-MKT and F-COL family extensions, ~3-4 hours total
- Phase 5: ingestion-rate gate would have already failed at this point
  (this was the 7th ingestion since the prior shipped fix); defer all
- Phase 6: field registry populated; specs empty; presentation empty;
  platform empty → modest impact, restating common pattern
- Phase 7: deferred as Fix 94, three candidate fields, post-D1 triage

**Honest reject outcome (Concrete job description, May 2026):**
- Phase 1: job description, Concrete (infrastructure company), May 2026,
  position description rather than methodology, low prior probability
- Phase 2: 0 substantive framework claims; describes a role and company
- Phase 3: N/A (no claims advanced)
- Phase 4: N/A
- Phase 5: rejected; not all ingestions produce backlog entries
- Phase 7: log in ingest-log.md as rejected, document reason (job spec
  for adjacent role at infrastructure company, no framework signal),
  question closed

**Immediate-ship outcome (Pharos pmUSD thread, May 2026, retrospective):**
- Phase 1: aggregated thread distilling findings, Pharos (independent
  analyst), May 2026, high density, high prior probability
- Phase 2: 7 substantive findings, all novel for VaultDiligence at time of
  ingestion
- Phase 3: structural narrative pattern not in any v50 spec — verdict
  block structure was the genuine gap
- Phase 4: spec amendment to verdict-block, single file, ~3 hours
- Phase 5: all six immediate-ship criteria met (under 4h, no deps,
  affects content quality, doesn't need D1 data, methodology document,
  cross-walk confirmed gap); ingestion-rate gate would have passed
  (early in session); ship as v51's Fix 86
- Phase 6: methodology/specs populated; field registry empty (no new
  fields); presentation populated (verdict block IS a presentation
  spec); platform empty → 2-of-4 dimensions → meaningful but not all-up
- Phase 7: shipped as Fix 86 in v51

## Loading order

This skill is loaded when the operator triggers ingestion. Read
the full SKILL.md (this file). Then proceed phase-by-phase. Do not
skip phases. The phases are the discipline.
