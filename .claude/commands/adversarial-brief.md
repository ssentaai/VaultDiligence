---
name: adversarial-brief
description: Run before every D1. Generates five questions this vault does
  not want you to ask. Human reviews and approves before collection begins.
  Runs automatically. Logs questions. Collection begins immediately.
---

# Adversarial Brief

## Purpose

The research is only as good as the research questions.
This command runs before data collection. It shapes what to look for.
It is not a checklist. It is adversarial thinking applied to a specific vault.

## Inputs Required

Vault name:
Vault type (VT-1 through VT-A):
Issuer or curator page URL:
Protocol Gitbook or docs URL (if known):

## Opening Question (ask before anything else)

Before generating the adversarial brief, ask the user:

  "Do you have an existing DDQ, reporting template, or preferred output
  format you would like this investigation to also render into?
  If yes, share it and I will produce a VaultDiligence-formatted version
  alongside the standard D1-D5 pack.
  If no, continue — standard outputs will be produced."

If they share a document:
  - Save it to packs/{vault-slug}/custom-template/input.{ext}
  - Note the format and required fields in packs/{vault-slug}/plan.md
  - After all standard outputs are complete, render a custom output
    using the same evidence object, mapped to their required fields
  - Save to packs/{vault-slug}/custom-template/output.{ext}
  - Note: this is an additional render only. It does not change
    what is investigated or how evidence is classified.
    The standard D1-D5 outputs are always produced first.

If they say no or do not respond: proceed immediately to Step 1.
This is not a gate. Do not wait more than one exchange.

## Step 0: Social and Narrative Mapping

Runs before the adversarial brief. Output: packs/{vault-slug}/social-map.md
This step is not optional for any vault with a public CT presence.

### 0a. Influence network

Search CT, Substack, and research platforms for coverage of this vault.
For each piece found, classify and record:

  Author: [name / handle]
  Tier: INDEPENDENT | CONFLICTED | PROTOCOL_TEAM | SPONSORED | AGGREGATOR
  Conflict: [angel investor, paid partnership, token holder — or NONE]
  Claim: [one-line summary of what they assert about the vault]
  URL + date

Conflicted sources found here must be flagged in the evidence register
when encountered during D3 collection. They are INFORMAL tier regardless
of how they present themselves.

### 0b. Narrative audit

Identify claims circulating on CT that are not in the primary documentation.
Specifically look for:
  Marketing language that diverges from product mechanics
  Yield claims that compress product distinctions
  Risk disclosures present in docs but absent from social promotion
  Questions asked publicly that the team has consistently deflected

Each divergence becomes a gap candidate in the investigation.
Consistent deflection on a specific question = pattern of non-disclosure.
Note this in packs/{vault-slug}/social-map.md. It upgrades the D4 action.

### 0c. Key CT nodes

Identify the 3-5 accounts with most influence over this vault's narrative:
  Direct team / founders
  Named investors (check for undisclosed promotions)
  Independent analysts covering it
  Aggregators republishing claims

These become the MiroFish seed actors in Step 0d.

### 0d. MiroFish Actor Graph (steps 1-2 only)

Upload to mirofish.my:
  Vault documentation (PDF/MD)
  Social map findings from 0a-0c (as plain text seed)

Extract from steps 1 and 2 only:
  Actor graph: who has leverage over this vault's outcomes
  Tension map: undisclosed relationships, narrative conflicts
  Disclosure gaps: relationships present in the graph but absent from docs

Do not use steps 3-4 (post-event simulation). Pre-event only.

### Output: social-map.md

Write to packs/{vault-slug}/social-map.md:

  ## Influence Network
  [table: author, tier, conflict, claim, URL, date]

  ## Narrative Divergences
  [list: claim in circulation vs what primary docs actually say]

  ## Non-Disclosure Patterns
  [list: questions deflected publicly, frequency, last occurrence]

  ## Key CT Nodes
  [list: handle, follower count, relationship to vault, conflict flag]

  ## MiroFish Actor Graph Findings
  [tensions and undisclosed relationships surfaced in steps 1-2]

This file feeds directly into adversarial question generation.
It is not cited in the pack. It improves the questions asked.



## Process

Step 1: Read knowledge/adversarial/{VT-X}.md for this vault type.
  Load the questions that vaults of this type do not want asked.
  These are derived from prior packs and incident post-mortems.
  If the file does not exist yet: start from first principles below.

Step 2: Read the issuer page and protocol docs via Scrapling.
  Do not collect data. Read to understand the architecture.
  Specifically identify:
    The stated yield mechanism and who controls each input.
    The named counterparties and their stated roles.
    What the documentation emphasises and what it does not address.
    The governance structure and who holds privileged roles.
    The redemption mechanism and how many counterparties it crosses.

Step 3: Apply the five question principles from SOUL.md.

  Absence of evidence:
    What mechanism is conspicuously undocumented for a protocol of
    this sophistication? What would a well-run protocol of this type
    normally disclose that this one does not?

  Follow the money:
    Who profits if the stated yield mechanism is correct?
    Who profits if it is gamed or fails?
    Who profits if the evidence is ambiguous or incomplete?
    The question the incentive structure discourages is the
    question to ask first.

  The unnamed counterparty:
    Who is not named in any document but bears risk if something
    fails? Oracle operators, market makers, informal arrangements,
    unnamed multisig signers, undisclosed dependencies.

  Stress the redemption:
    Walk the redemption waterfall under 30% TVL outflow with one
    counterparty unavailable. Where does it break? Who is the
    bottleneck? Is that entity named anywhere?

  The audit gap:
    What changed in this protocol after its most recent audit?
    Does the out-of-scope section of the audit cover the same
    mechanisms that failed in the three most recent exploits of
    this vault type? State the overlap explicitly.

Step 4: Generate exactly five questions. No more. No fewer.

  Each question must be:
    Specific to this vault. Not a generic checklist item.
    Answerable in principle (there is evidence that would close it).
    One the protocol documentation does not address.
    Derived from the principles above, not from the framework criteria.
    Stated as a question, not a criterion.

Step 5: Log the five questions and begin collection immediately.

  Write to packs/{vault-slug}/adversarial-brief.md:

  ADVERSARIAL BRIEF — [Vault Name] — [Date]

  Q1: [question] | Derived from: [principle + trigger]
  Q2: [question] | Derived from: [principle + trigger]
  Q3: [question] | Derived from: [principle + trigger]
  Q4: [question] | Derived from: [principle + trigger]
  Q5: [question] | Derived from: [principle + trigger]

  No human approval required. Questions are generated and logged.
  D1 collection begins immediately.

## After Brief is Logged

D1 collection runs with these questions shaping what matters.
When a field or source speaks to one of the five questions: flag it.
When evidence is absent: classify as G2 with the adversarial brief
question as context for the gap.

## After Pack Completion

Human writes to packs/{vault-slug}/questions-not-asked.md:
  Questions that became obvious only after the pack was complete.
  What the question is.
  Why it was not asked initially.
  What evidence would answer it.

These questions feed knowledge/adversarial/{VT-X}.md.
That file grows with every pack.
The agent gets better at forming the right questions over time.
