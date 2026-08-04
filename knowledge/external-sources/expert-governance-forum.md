---
schema_version: 1
id: expert-governance-forum
name: Protocol Governance Forums (Discourse) — Named-Author Posts
provider: Various (protocol-operated Discourse instances)
url_base: https://governance.aave.com
docs_url: https://governance.aave.com
source_tier: EXPERT
purpose:
  - governance-discussion-record
  - risk-manager-and-steward-posts
  - service-provider-disclosures
auth: none
access_mode: fetch
freshness_typical: hourly
freshness_max_trusted: 7d
covers_chains:
  - ALL
covers_field_ids:
  - F-CUR-009
  - F-OPS-005
  - F-CUR-002
fallback_sources:
  - snapshot-governance-votes
  - tally-onchain-governance
  - expert-curator-forum
status: active
added_in: v54
notes_url:
---

## What this source provides

Generic category entry for protocol-operated Discourse governance forums (governance.aave.com, forum.morpho.org, Compound's community forum). They host proposals, risk-manager/steward updates, service-provider disclosures, and community research, all publicly readable. Covers posts authored by named individuals/firms; anonymous posts on the same forums fall to the informal floor.

## Source tier rationale

EXPERT for named-author posts: a forum post is analysis/disclosure by a named participant (LlamaRisk, Gauntlet, a named steward), matching the EXPERT definition (named individual/firm producing opinion/disclosure, not a record of record). Not FORMAL — a thread is not a versioned methodology doc or a filing, and the forum operator does not vouch for content. Anonymous posts are INFORMAL and cannot support state=E.

## When to use it

EXPERT corroborating source for F-CUR-009 (third-party risk manager named in a post), F-OPS-005 (incident response SLA disclosed in a thread), and F-CUR-002 (bad-debt history a named steward describes). Ceiling is E(P): a named-author disclosure corroborates but does not alone establish a material fact (needs ON-CHAIN/FORMAL). Cite post URL, author identity, and date.

## When NOT to use it

Not standalone for any material fact (EXPERT ceiling E(P)). Not for anonymous/pseudonymous posts — those are INFORMAL, cite the generic informal category, never this entry. Not for the binding governance outcome (use Snapshot/Tally). Not for the curator's own published risk framework as a document (F-CUR-004), which is better cited via expert-curator-forum.

## Authentication and rate limits

Public, no key. Aave (governance.aave.com) and Morpho (forum.morpho.org) Discourse instances both returned HTTP 200 to anonymous WebFetch on 2026-06-19 and serve threads without login. Discourse exposes a JSON view (append .json to a topic URL) for structured retrieval. Heavy scraping may be rate-limited per host config; back off per tool-recovery.

Access probe: HTTP 200 to anonymous on 2026-06-19 (governance.aave.com Discourse forum served thread content without login; forum.morpho.org also HTTP 200)

## Cross-references

expert-curator-forum (companion EXPERT entry for named-curator risk-methodology posts; use for F-CUR-004 substance); snapshot-governance-votes / tally-onchain-governance (the binding vote records the threads discuss); a generic informal-forum category (not yet registered) is the correct cite for anonymous posts on the same forums.

## Notes

The same forum carries both EXPERT (named) and INFORMAL (anonymous) content; tier follows the author not the venue, so author identity must be established before citing. Forum disclosures are self-serving (poster is usually interested), so treat as disclosures to corroborate, not neutral records. No fallback fully substitutes for the discussion record itself; listed fallbacks cover the adjacent vote and curator-methodology layers. Reclassify to active when: (1) the named-author-versus-anonymous tier split is encoded so anonymous posts route to an informal category and never to this entry; (2) VaultDiligence has cited a specific named-author post as an EXPERT corroborating source on at least one pack and A6 confirmed the E(P) ceiling was respected; (3) a stable retrieval path (Discourse topic .json) is confirmed across at least two protocol forums.
