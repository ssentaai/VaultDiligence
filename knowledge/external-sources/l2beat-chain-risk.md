---
schema_version: 1
id: l2beat-chain-risk
name: L2BEAT
provider: L2BEAT (L2BEAT Foundation)
url_base: https://l2beat.com
docs_url: https://l2beat.com/faq
source_tier: FORMAL
purpose:
  - l2-rollup-architecture-and-stage
  - sequencer-and-proposer-decentralisation
  - cross-chain-interop-and-bridge-risk
auth: none
access_mode: fetch
freshness_typical: daily
freshness_max_trusted: 7d
covers_chains:
  - ALL
covers_field_ids:
  - F-CHN-003
  - F-CHN-002
  - F-CHN-001
  - F-BRG-001
fallback_sources:
  - direct-rpc-read
status: active
added_in: v54
notes_url:
---

## What this source provides

Reference tracker for the L2 and cross-chain-interop ecosystem. Per project: total value secured, proof system (Optimistic/Validity), a structured Risk Analysis (State Validation, Data Availability, Sequencer Failure, Proposer Failure, Exit Window), a Stage classification (0/1/2), sequencer/proposer decentralisation status including forced-inclusion/escape-hatch availability, and an Interop section covering cross-chain messaging.

## Source tier rationale

FORMAL. Attributable maintainer (L2BEAT Foundation), versioned documented risk-assessment methodology (risk-framework and stage definitions public and revised over time), and open-source (data and code public on GitHub) — clears FORMAL on three counts. Not ON-CHAIN: the risk classifications and stage labels are analytical aggregations over chain state (the methodology layer); a direct sequencer/validator contract read is the separate ON-CHAIN source. Not EXPERT: maintained methodology-driven dataset, not a single firm's opinion piece.

## When to use it

Primary FORMAL source for F-CHN-003 (sequencer model single/shared/permissionless and whether a forced-inclusion/escape-hatch path exists; proposer decentralisation) for any L2 in the deployment/dependency set, and the named fallback for F-CHN-002 (architecture, proof system, settlement layer) per that field's definition. Structured input to the F-CHN-001 chain-evaluation gate.

## When NOT to use it

Not the terminal source for a sequencer/validator finding where the contract is directly readable — for F-CHN-003 the on-chain sequencer/validator-set read supersedes the tracker if they conflict (flag I). Not for L1 validator-level detail outside its L2-focused scope. Not for the chain's own contract audits as documents (F-CHN-002's audit leg needs the named audit firm's report). Not for asset-level or bridging-verifier-set conclusions (F-BRG-002 from the bridge config itself).

## Authentication and rate limits

Public, no key. Homepage HTTP 200 to anonymous WebFetch (2026-06-19); project list, risk-analysis sections, and stage labels readable. Also exposes data via public GitHub repo for structured retrieval. Heavy scraping of the rendered app may be rate-limited; prefer documented data sources and back off per tool-recovery. No operator credential required.

Access probe: HTTP 200 on 2026-06-19 (homepage; project list, Risk Analysis sections, and Stage labels readable)

## Cross-references

direct-rpc-read — ON-CHAIN superseding source for the sequencer/validator-set read L2BEAT summarises. Fields F-CHN-001/002/003 (chain evaluation; F-CHN-002 names L2BEAT as a fallback directly, F-CHN-003 names L2BEAT-class trackers for sequencer/forced-inclusion status). F-BRG-001 for native-bridge interop topology context on L2 routes.

## Notes

L2BEAT's stage and risk classifications are the most widely cited L2-risk reference, but they are a methodology-driven assessment, so for a material F-CHN-003 finding (e.g. a single sequencer with no forced-inclusion path, cross-ref SC11) reconcile against the on-chain sequencer configuration. The Arbitrum single-sequencer outage precedent in F-CHN-003 is exactly the failure mode L2BEAT's Sequencer Failure and forced-inclusion rows surface. Coverage is strongest for established rollups; incomplete rows on newer/non-standard chains are themselves a gap to state. Reclassify to active when: (1) an L2BEAT sequencer/forced-inclusion classification has been reconciled against the on-chain sequencer configuration for at least one chain; (2) VaultDiligence has cited a specific L2BEAT project risk row for F-CHN-003 (or F-CHN-002 fallback) on at least one pack and A6 confirmed it; (3) a stable structured-retrieval path (GitHub data export vs rendered page) is confirmed for the fields cited.
