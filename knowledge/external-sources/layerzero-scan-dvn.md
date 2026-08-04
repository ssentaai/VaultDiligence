---
schema_version: 1
id: layerzero-scan-dvn
name: LayerZero Scan
provider: LayerZero Labs
url_base: https://layerzeroscan.com
docs_url: https://docs.layerzero.network/v2/concepts/modular-security/security-stack-dvns
source_tier: FORMAL
purpose:
  - dvn-verifier-set-discovery
  - cross-chain-message-status
  - send-receive-library-configuration
auth: rate-limited-anonymous
access_mode: pointer-gated
freshness_typical: minute
freshness_max_trusted: 24h
covers_chains:
  - ALL
covers_field_ids:
  - F-BRG-002
  - F-BRG-001
  - F-BRG-003
  - F-BRG-004
  - F-SEC-019
fallback_sources:
  - direct-rpc-read
status: candidate
added_in: v54
notes_url:
---

## What this source provides

Official explorer for LayerZero V2 omnichain messaging. Surfaces per pathway (source endpoint to destination endpoint): cross-chain message status/history, the configured DVN set split into required and optional DVNs, the X-of-Y-of-N verification threshold, the configured send/receive libraries, and the executor. The /tools/defaults view shows default pathway configurations by chain.

## Source tier rationale

FORMAL, not ON-CHAIN. The DVN configuration lives in the LayerZero Endpoint/SendUln/ReceiveUln contracts on each chain, but LayerZero Scan indexes and presents that state through its own off-chain explorer — the aggregation/methodology layer that defines FORMAL. Clears FORMAL on attributable maintainer (LayerZero Labs) and versioned public protocol documentation. The direct verified-contract read via RPC is the superseding ON-CHAIN source (direct-rpc-read). Not EXPERT (serves config records, not opinion).

## When to use it

Fast FORMAL source for F-BRG-002 (read required/optional DVN set and X-of-Y-of-N threshold per pathway carrying vault exposure), seeds F-BRG-001 (messaging system+version), F-BRG-003 (named DVN operators as independence input), F-BRG-004 (send/receive library config). Entry point for VT-5/VT-7 bridge-crossing vaults before the on-chain confirming read.

## When NOT to use it

Not the terminal source for the verifier threshold — F-BRG-002's primary source is the on-chain config read, so reconcile against a direct contract read before any RF44 critical-condition finding (flag I on divergence). Not for non-LayerZero bridges (Wormhole, Axelar, CCIP, native rollup bridges). Not for verifier-independence conclusions alone (F-BRG-003 needs per-operator org/jurisdiction/infra attribution). Not for the failover-collapse finding (F-SEC-019) without reading failover/default behaviour directly.

## Authentication and rate limits

Public, no key. Returned HTTP 429 to anonymous WebFetch (2026-06-19), indicating aggressive anonymous rate-limiting / bot gate on the rendered app. Underlying config readable on-chain via direct-rpc-read, the robust fallback when the explorer throttles. On 429/403, back off per tool-recovery and fall through to the direct contract read. No operator credential required.

Access probe: HTTP 429 Too Many Requests to anonymous WebFetch (2026-06-19) — aggressive anonymous rate-limit / bot gate on the rendered explorer; underlying DVN config is readable on-chain via direct-rpc-read as the robust fallback

## Cross-references

direct-rpc-read — ON-CHAIN superseding source for the DVN/verifier set and library config; reconcile against it for any material F-BRG-002 finding. Fields F-BRG-001/002/003/004 (bridging topology; Kelp DAO 1-of-1 DVN failover precedent, 18 Apr 2026) and F-SEC-019 (cross-chain infra audit/failover).

## Notes

The Kelp DAO precedent — 292M USD drained via forced failover to a 1-of-1 LayerZero DVN — is exactly the configuration this explorer is best at exposing; a pathway resolving to one required DVN, or whose failover collapses to one, is the finding. LayerZero shipped 1-of-1 as a common default, so /tools/defaults is a useful first check for vendor-default weakness. The explorer is the convenience layer; the contract read is the source of truth, so a divergence is itself a finding (I), not a tie to break silently. Reclassify to active when: (1) the verifier-set read has been reconciled against a direct contract read (direct-rpc-read) for at least one pathway so the indexer is confirmed faithful; (2) VaultDiligence has cited a specific pathway's DVN configuration for F-BRG-002 on at least one pack and A6 confirmed it held; (3) the anonymous 429 behaviour has been characterised and a robust explorer-then-RPC retrieval/fallback path is documented.

Ratification (2026-06-19): access_mode=pointer-gated; status=candidate. Aggressive anonymous rate-limit / bot gate (HTTP 429 2026-06-19); JS-rendered. Key second-order DVN source — needs a stable access route before active.
