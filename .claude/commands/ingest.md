---
name: ingest
description: Ingest an article, blog post, research paper, or document
  into the VaultDiligence knowledge graph. Extracts what is relevant to vault
  diligence, framework criteria, vault types, and risk categories.
  Flags anything that suggests a framework review is needed.
  Use when you encounter something that should inform future investigations.
---

# /ingest — Knowledge Graph Ingestion

## When to use this command vs the ingest-source skill

This command and the `ingest-source` skill have overlapping subject
matter but serve different purposes. Use the right one:

**Use `/ingest` (this command) when:**
- You want to capture a source's content for future investigation reuse
- Output goes to `knowledge/research/{slug}.md` (knowledge graph)
- A1/A2 will read this at the start of relevant vault investigations
- Lightweight; one-pass extraction; ~5 minutes per source
- Side effect: flags potential framework-review items to
  `knowledge/research/framework-review-queue.md` for later review

**Use the `ingest-source` skill when:**
- You want to assess whether a source should UPDATE the framework
  itself (fields, specs, principles, output presentation, platform
  delivery)
- Output is a structured ship/defer/reject decision with backlog entry
- Heavyweight; seven-phase methodology including registry audit and
  ingestion-rate gate; ~30-60 minutes per source
- Side effect: writes to the running ingest log
  (rate-gate tracking)

**Use BOTH for a single source when:**
- The source is substantively novel AND should be captured for agent
  reuse. Run `/ingest` first (captures content), then invoke the
  `ingest-source` skill if framework changes are warranted.
- The `framework_review_flagged: true` field in /ingest's output is
  the signal that ingest-source skill should be run next.

The two are not duplicates. `/ingest` builds the knowledge graph that
agents read from. The `ingest-source` skill decides whether the framework
itself should change. Most sources need only `/ingest`. A minority of
sources (methodology documents, major incident post-mortems, new
analytical primitives) warrant the heavier `ingest-source` treatment
in addition.

---

## Usage

/ingest [URL or file path] [optional context note]

Examples:
  /ingest https://centrifuge.io/blog/from-tokenization-to-vaults-onchain-capital-stack
  /ingest https://rekt.news/euler-rekt/ "New failure mode for oracle manipulation"
  /ingest /path/to/audit-report.pdf "Trail of Bits audit of Morpho Blue"
  /ingest https://governance.aave.com/t/horizon-weekly-highlights/23078

---

## What the Ingest Agent Does

Single-pass. Lightweight. Focused extraction only.

Step 1: Fetch the source.
  URL: use Scrapling for HTML, web_fetch for simple pages.
  PDF: use pdfplumber.
  Twitter/X: Scrapling StealthyFetcher for thread content.
  If fetch fails: state the failure and stop. Do not infer content.

Step 1b: Classify the source authority level.
  Ask three questions:
  1. Does the author have a verifiable track record in this domain?
  2. Is the methodology stated or are claims independently verifiable?
  3. Would a senior DeFi risk analyst cite this in their own work?

  All three yes = EXPERT ANALYSIS
  Any no = INFORMAL

  Known EXPERT ANALYSIS sources: ZachXBT, DeFiDojo, Tarun Chitra,
  Trail of Bits, Zellic, Spearbit, LlamaRisk, Chaos Labs, Certora,
  a research advisory Research, Hasu. Platform is irrelevant.

  If EXPERT ANALYSIS and the source cites on-chain tx hashes or
  contract addresses: verify them independently. If confirmed,
  the finding is ON-CHAIN. Credit the expert as the pointer.

  If INFORMAL: the research page must start with:
  "INFORMAL SOURCE. Cannot be cited as standalone fact in any pack.
   Use as investigation pointer only. Confirm in FORMAL or ON-CHAIN."

Step 2: Extract only what is relevant to VaultDiligence.
  Relevant: vault types, risk criteria, infrastructure patterns,
  counterparty relationships, regulatory developments, failure modes,
  new exploit vectors, framework gaps, market structure changes.
  Ignore: marketing copy, product announcements without substance,
  price speculation, unrelated DeFi topics.

  If the source has nothing relevant to VaultDiligence:
  Write a one-line note and stop. Do not force relevance.

Step 3: Write knowledge/research/{slug}.md

Step 4: Check for framework review flags.
  Does this source suggest:
  - A new vault type not in the current VT-1 through VT-A taxonomy?
  - A failure mode not covered by existing red flags RF01-RF40?
  - A risk category that does not fit the six current categories?
  - A counterparty pattern that changes how criteria should be assessed?
  If yes: append to knowledge/research/framework-review-queue.md

---

## Output Format

knowledge/research/{slug}.md

Slug is derived from the URL or filename. Lowercase, hyphens, no special chars.

```markdown
---
source_url: [exact URL or file path]
source_name: [publication or document name]
source_date: [date published or date of document]
ingested: [YYYY-MM-DD]
context_note: [your note if provided, else blank]
source_authority: [ON-CHAIN / FORMAL / EXPERT ANALYSIS / INFORMAL]
relevance_tags:
  vault_types: [VT-1, VT-3a, VT-7 etc — only if specifically relevant]
  risk_categories: [Legal and Custody Risk, Smart Contract Risk etc]
  framework_criteria: [1.3, 7.6, 9.4 etc — criteria this directly informs]
  counterparties: [named entities if relevant]
  red_flags: [RF numbers if this relates to specific conditions]
framework_review_flagged: [true/false]
---

## What This Source Says (relevant to VaultDiligence only)

[Concise extraction. What does an investigation agent need to know
from this source. Not a summary of the whole article. Only what
changes how an agent should investigate or what it should look for.
Maximum 300 words. Cite specific claims with page or section reference.]

## Framework Review Flag (if applicable)

[What the source suggests should be reviewed in the framework.
Be specific: which criterion, which vault type, which red flag.
This is a flag for your review, not an automatic update.]

## Backlinks

[Link to relevant criteria, vault types, or red flags in the knowledge graph]
[[knowledge/framework/pillars/P7]] (if relevant)
[[knowledge/framework/vault-types/VT-7]] (if relevant)
[[knowledge/red-flags/RF26]] (if relevant)
```

---

## Framework Review Queue

knowledge/research/framework-review-queue.md accumulates flags.
Format per entry:

```
## [YYYY-MM-DD] [source slug]

Source: [URL]
Flag: [one sentence — what should be reviewed]
Specific: [criterion ID, vault type, or red flag number]
Priority: [High / Medium / Low]
Status: [Open / Reviewed / Actioned]
```

Review this file before each framework update.
Do not action flags automatically. Your judgment required.

---

## How Investigation Agents Use This

At the start of every investigation run, Agent 1 and Agent 2 check:

knowledge/research/ for pages tagged with the current vault's type
and risk categories.

If a relevant research page exists: read the summary before going
to the web. Apply its insights to the investigation.

This prevents agents from re-discovering known patterns on every run.
The knowledge compounds. The token cost per investigation falls.

---

## Example: This Article

/ingest https://centrifuge.io/blog/from-tokenization-to-vaults-onchain-capital-stack

Would produce knowledge/research/centrifuge-onchain-capital-stack.md tagged:

vault_types: [VT-3, VT-3a, VT-7]
risk_categories: [Smart Contract Risk, Liquidity and Exit Risk]
framework_criteria: [7.6, 7.12, 9.8]
red_flags: [RF23, RF25, RF26]

Extracting: the four-layer composable vault stack architecture,
hub-and-spoke multichain design implications for RF26 (bridge risk),
cross-protocol contagion path for VT-7 assessments,
progression from tokenisation wrapper to native onchain origination
as a vault type classification consideration.

Framework review flag: VT-7 contagion map criteria (7.6) may need
updating to reflect the allocator vault > strategy vault > tranche vault
> base collateral layer structure explicitly.
