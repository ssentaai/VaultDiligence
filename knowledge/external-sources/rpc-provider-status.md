---
schema_version: 1
id: rpc-provider-status
name: RPC Provider Status / Liveness pages
provider: Alchemy / Infura / QuickNode (status pages)
url_base: (provider status subdomains)
docs_url: 
source_tier: FORMAL
purpose:
  - rpc-liveness
  - rpc-provider-diversity
auth: none
access_mode: fetch
freshness_typical: realtime
freshness_max_trusted: 1h
covers_chains:
  - ALL
covers_field_ids:
  - F-CHN-008
fallback_sources:
  - l2beat-chain-risk
status: candidate
added_in: v54
notes_url:
---

## What this source provides

Published uptime/incident/status pages for the major RPC providers (Alchemy, Infura, QuickNode, Ankr), used to evidence RPC liveness and provider diversity for a chain.

## Source tier rationale

FORMAL: provider-published operational status with attributable maintainers. Not ON-CHAIN (it is a hosted status artifact, not a chain read).

## When to use it

F-CHN-008 (chain tooling & monitoring) where RPC-provider diversity and single-RPC-dependence are the question.

## When NOT to use it

Not for chain-state values (use direct-rpc-read). Not authoritative for outage root cause.

## Authentication and rate limits

Public status pages; no auth. Formats differ per provider — no unified API, hence candidate status.

Access probe: not probed (2026-06-19) — provider status pages, formats vary

## Cross-references

Pairs with direct-rpc-read (the ON-CHAIN read entry) and l2beat-chain-risk (chain decentralisation).

## Notes

Registered v54 (Fix 70). Candidate — added per ratification rule (b) optional provider-status entry to cover F-CHN-008 (otherwise uncovered). Reclassify to active when: (1) a stable per-provider status route is confirmed; (2) cited on a pack for F-CHN-008; (3) F-CHN-008 cross-ref applied.
