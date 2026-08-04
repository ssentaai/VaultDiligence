---
schema_version: 1
id: snapshot-governance-votes
name: Snapshot Hub GraphQL API
provider: Snapshot Labs
url_base: https://hub.snapshot.org/graphql
docs_url: https://docs.snapshot.box/tools/api
source_tier: FORMAL
purpose:
  - offchain-governance-votes
  - governance-proposal-records
  - voting-power-snapshot
auth: rate-limited-anonymous
access_mode: fetch
freshness_typical: minute
freshness_max_trusted: 24h
covers_chains:
  - ALL
covers_field_ids:
  - F-CUR-008
  - F-CUR-011
fallback_sources:
  - tally-onchain-governance
  - expert-governance-forum
status: active
added_in: v54
notes_url:
---

## What this source provides

Snapshot is the dominant off-chain gasless governance voting platform; its Hub GraphQL API at hub.snapshot.org/graphql exposes per-space and per-proposal data: proposal title/body, choices, start/end timestamps, state, vote records, and computed voting power (vp). Used to read the governance decision trail behind curator parameter changes and other vault-relevant proposals.

## Source tier rationale

FORMAL, not ON-CHAIN: Snapshot votes are signed off-chain messages indexed by Snapshot's Hub, and what VaultDiligence consumes is the indexed/aggregated GraphQL response with methodology-dependent voting-power strategies, not a direct chain read. Clears FORMAL on attributable maintainer (Snapshot Labs), open-source codebase, and versioned public API docs. Not EXPERT (records of governance events, not opinion).

## When to use it

Primary FORMAL source for F-CUR-008 (parameter change log) when the curator/protocol routes decisions through a Snapshot space, and corroborating for F-CUR-011 (auto-allocation enabled) where governance-ratified. Cite proposal id, space, and close date. Prefer for off-chain signaling votes.

## When NOT to use it

Not for on-chain timelock duration or executed on-chain governance (F-GOV-005) — Snapshot votes are off-chain signals; use Tally or a direct contract read. Not as proof a vote was implemented (signal, not execution). Not for curator risk-framework substance (F-CUR-004), which lives in forum posts.

## Authentication and rate limits

Public, no key for reads; anonymous reads rate-limited to 60 requests/minute, higher throughput needs an API key via Snapshot's application process. Endpoint returned HTTP 200 (GraphiQL) to anonymous WebFetch on 2026-06-19. Back off on 429 per tool-recovery.

Access probe: HTTP 200 to anonymous on 2026-06-19 (endpoint served GraphiQL UI; docs confirm anonymous reads at 60 requests/minute)

## Cross-references

tally-onchain-governance (on-chain executed governance + timelock); expert-governance-forum (the Discourse debate preceding the vote); F-GOV-005 (on-chain timelock Snapshot does not cover).

## Notes

Voting-power strategies are configurable per space, so the same address shows different vp across spaces — cite the space context. Off-chain signaling is non-binding, so a passed proposal must be reconciled against on-chain execution before treating it as implemented. Reclassify to active when: (1) VaultDiligence has cited a specific Snapshot proposal id as primary for F-CUR-008 on at least one pack and A6 confirmed it held; (2) the off-chain-signal-versus-execution gap was resolved for that pack by corroborating implementation on-chain; (3) the 60-request/minute anonymous limit was validated as sufficient or an API-key path confirmed.
