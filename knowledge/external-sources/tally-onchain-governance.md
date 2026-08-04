---
schema_version: 1
id: tally-onchain-governance
name: Tally Governance API
provider: Tally (Withtally, Inc.)
url_base: https://api.tally.xyz/query
docs_url: https://apidocs.tally.xyz
source_tier: FORMAL
purpose:
  - onchain-governance-proposals
  - governor-and-timelock-parameters
  - delegate-and-vote-records
auth: api-key
access_mode: pointer-gated
freshness_typical: minute
freshness_max_trusted: 24h
covers_chains:
  - ethereum
  - arbitrum
  - optimism
  - base
covers_field_ids:
  - F-GOV-005
  - F-CUR-008
fallback_sources:
  - snapshot-governance-votes
  - expert-governance-forum
status: candidate
added_in: v54
notes_url:
---

## What this source provides

Tally indexes on-chain Governor (OpenZeppelin/Compound-style) and timelock contracts for 500+ protocols; its GraphQL API at api.tally.xyz/query returns governor parameters, proposals and proposal events, vote records/statistics, delegate and delegation relationships, and timelock contract identifiers. Used to read executed on-chain governance and surface the timelock behind parameter changes.

## Source tier rationale

FORMAL, not ON-CHAIN: the underlying proposals/timelocks are on-chain but Tally indexes and normalises that state off-chain and serves it via its own API (the methodology layer). Clears FORMAL on attributable maintainer (Withtally, Inc.) and versioned public API docs. A direct governor/timelock contract read would be the separate ON-CHAIN source; Tally is the indexed convenience layer. Not EXPERT.

## When to use it

Primary FORMAL source for F-GOV-005 (timelock duration, read from the indexed timelock contract) and F-CUR-008 (parameter change log via executed on-chain proposals) for Governor-based protocols; feeds the F-GOV-007 ratio. Cite proposal id and governor/timelock address. Prefer over Snapshot when the question is on-chain execution, not signaling.

## When NOT to use it

Not as source-of-truth for the timelock value where a direct contract read is available (on-chain supersedes the indexer; flag any conflict as I). Not for off-chain signaling (use Snapshot). Not for non-Governor governance Tally does not index (G2 against a direct read). Not for curator risk-framework substance (F-CUR-004).

## Authentication and rate limits

API key required: every request sends an Api-Key header; keys obtained from a Tally user-settings page. Endpoint returned HTTP 401 to anonymous WebFetch on 2026-06-19, confirming the gate. Rate limits apply (increases via support@tally.xyz). Operator sets the key as an env var or settings.json entry; document where before first use. Back off on 401/429 per tool-recovery.

Access probe: HTTP 401 to anonymous on 2026-06-19 (api.tally.xyz/query requires Api-Key header, as documented at apidocs.tally.xyz)

## Cross-references

snapshot-governance-votes (off-chain signaling companion); expert-governance-forum (the discussion layer); F-GOV-005 / F-GOV-007 — Tally is the indexed source, a direct contract read is the ON-CHAIN superseding source if registered.

## Notes

As an indexer, Tally's timelock/proposal values are FORMAL corroboration and, for F-GOV-005 specifically, should be reconciled against a direct contract read where TTL/materiality warrant. Chain coverage is broad but not universal; confirm the protocol's chain is indexed. Platform observed mid-rebrand (Tally to Cactus) on 2026-06-19; api.tally.xyz endpoint and Api-Key scheme remained the documented path. Reclassify to active when: (1) an operator-set API key path is confirmed and a live query returns governor/timelock data for a target protocol; (2) VaultDiligence has cited a Tally proposal id or timelock address as primary for F-CUR-008 or F-GOV-005 on at least one pack and A6 confirmed it; (3) for any F-GOV-005 citation, the indexed timelock value was reconciled against a direct contract read at least once to confirm the indexer is faithful.

Ratification (2026-06-19): access_mode=pointer-gated; status=candidate. api.tally.xyz requires an Api-Key header (HTTP 401 anonymous 2026-06-19).
