---
schema_version: 1
id: expert-curator-forum
name: Curator Risk-Methodology Posts (Named Curators)
provider: Various (named curators: Gauntlet, Steakhouse, Block Analitica, Re7, LlamaRisk)
url_base: https://forum.morpho.org
docs_url: https://forum.morpho.org
source_tier: EXPERT
purpose:
  - curator-risk-framework-disclosure
  - curator-track-record-statements
  - curator-conflict-disclosures
auth: none
access_mode: fetch
freshness_typical: daily
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-CUR-004
  - F-CUR-002
  - F-CUR-003
  - F-CUR-015
  - F-GOV-020
fallback_sources:
  - expert-governance-forum
  - snapshot-governance-votes
status: active
added_in: v54
notes_url:
---

## What this source provides

Generic category entry for risk-methodology and disclosure posts by named curators (Gauntlet, Steakhouse Financial, Block Analitica, Re7, LlamaRisk) on protocol governance forums and their own posts. They contain the curator's documented risk framework, statements about past bad debt, lists of other vaults managed, accounts of stress-event responses, and conflict-of-interest disclosures. Used to source curator-side P8/P2 fields when published on a forum.

## Source tier rationale

EXPERT: a named-curator post is domain-expert disclosure/opinion by an attributable firm (the EXPERT definition). Not FORMAL — a forum post is not a versioned methodology doc, a signed report, or a filing, even from a reputable curator. Distinct from expert-governance-forum because the author is specifically the vault's curator/risk-manager and the content is its own methodology/track record, carrying a self-interest caveat absent from third-party steward posts.

## When to use it

EXPERT source for F-CUR-004 (curator published risk framework, where it is a forum/blog post not a standalone doc) and corroborating EXPERT input for F-CUR-002 (bad-debt history), F-CUR-003 (other active vaults), F-CUR-015 (stress-event response record), and F-GOV-020 (conflict-of-interest disclosure). Ceiling E(P): curator self-statements corroborate but a material fact (e.g. zero bad debt) needs ON-CHAIN/FORMAL confirmation. Cite post URL, curator name, date.

## When NOT to use it

Not standalone for any material curator fact (EXPERT ceiling E(P)). A curator's zero-bad-debt claim (F-CUR-002) or clean stress response (F-CUR-015) must be corroborated on-chain or by an independent incident database (Rekt, DefiHackLabs) since the curator is the interested party. Not for anonymous curator posts (INFORMAL). Not for on-chain skin-in-the-game (F-CUR-016), which is a wallet read.

## Authentication and rate limits

Public, no key. forum.morpho.org returned HTTP 200 to anonymous WebFetch on 2026-06-19 and hosts named-curator posts (Gauntlet, Steakhouse observed). Discourse .json topic views aid structured retrieval. Curator posts may also live on the curator's own blog/docs (may be JS-rendered); prefer the forum copy where one exists. Back off on rate limits per tool-recovery.

Access probe: HTTP 200 to anonymous on 2026-06-19 (forum.morpho.org served named-curator posts from Gauntlet and Steakhouse without login)

## Cross-references

expert-governance-forum (companion EXPERT entry for third-party steward/risk-manager posts, as opposed to the curator's own); snapshot-governance-votes / tally-onchain-governance (binding record for parameter changes the framework describes); F-CUR-016 (on-chain curator skin-in-the-game, a wallet read not covered here); F-CUR-001 (curator identity, sourced on-chain via owner()).

## Notes

The defining caveat is self-interest: every fact here is stated by the party being evaluated, so the entry captures what the curator claims, not confirmation. Strongest use is F-CUR-004 (does a documented framework exist and what does it say), a what-the-curator-published question answered directly at E(P); track-record claims (F-CUR-002, F-CUR-015) always require independent corroboration. Anonymous curators have no entry here and are a flag in themselves (F-CUR-001). Reclassify to active when: (1) a corroboration rule is encoded so curator self-claims for F-CUR-002 and F-CUR-015 are always paired with an independent on-chain or incident-database source before any E-state write; (2) VaultDiligence has cited a specific named-curator post for F-CUR-004 on at least one pack and A6 confirmed the E(P) ceiling; (3) the curator-own-blog versus forum-copy retrieval preference is validated against at least two curators.
