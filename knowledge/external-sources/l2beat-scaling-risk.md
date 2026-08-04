---
schema_version: 1
id: l2beat-scaling-risk
name: L2BEAT Scaling Risk & Bridge Risk Tracker
provider: L2BEAT
url_base: https://l2beat.com
docs_url: https://l2beat.com/scaling/risk
source_tier: FORMAL
purpose:
  - l2-risk-profile
  - bridge-risk-framework
  - sequencer-proposer-status
  - chain-decentralisation
auth: none
access_mode: fetch
freshness_typical: daily
freshness_max_trusted: 7d
covers_chains:
  - ALL
covers_field_ids:
  - F-CHN-001
  - F-CHN-003
  - F-BRG-001
  - F-BRG-005
fallback_sources:
  - direct-rpc-read
  - chain-foundation-docs
status: active
added_in: v54
notes_url:
---

## What this source provides

L2BEAT tracks the Ethereum L2 ecosystem and publishes per-rollup risk profiles across five dimensions (State Validation, Data Availability, Sequencer Failure, Proposer Failure, Exit Window) plus a Stage classification (Stage 0/1/2), total value secured, proof system, and sequencer/forced-inclusion status. It maintains versioned, changelog-tracked frameworks (Risk Rosette, L2Bridge Risk Framework, Data Availability Risk Framework) and views for Summary, Risk, Value, Activity, Liveness, and Costs.

## Source tier rationale

FORMAL, not ON-CHAIN. L2BEAT is an off-chain tracker that applies human-reviewed, versioned risk frameworks to chain and bridge configurations; the reader does not recompute the rating from chain state. It satisfies FORMAL on at least three counts: versioned methodology with public changelog (Risk Rosette, L2Bridge Risk Framework), an attributable maintainer (L2BEAT team), and an open-source codebase. This is the key second-order bridge/chain source the venue notes call out.

## When to use it

Primary FORMAL corroboration for the chain-evaluation gate (F-CHN-001) and consensus/sequencer decentralisation (F-CHN-003 — sequencer model, forced-inclusion/escape path, stage), and for bridge route-topology and authority/timelock context (F-BRG-001, F-BRG-005 — L2Bridge Risk Framework characterises the messaging/verifier trust model and exit-window assumptions). The field definitions for F-CHN-003 explicitly name L2BEAT as a fallback decentralisation tracker.

## When NOT to use it

Do not use L2BEAT as the authoritative read of a specific bridge contract's admin owner or configured timelock delay — those are on-chain reads (direct-rpc-read) per F-BRG-001/005 evidence pathway; L2BEAT is framing and corroboration, not the verified-contract state. Do not cite it for L1-validator-set specifics it does not track, and do not treat a Stage label as a substitute for reading the specific authority controls a VaultDiligence pack requires.

## Authentication and rate limits

Public website, no authentication for reading the scaling/risk pages. The values are partly client-rendered, so a WebFetch HTML scrape may miss live figures; cite the specific page route and transcribe values honestly, or use the L2BEAT API/GitHub data where available. If accessed via curl, operator adds l2beat.com to the settings.json allow-list at Step 5.

Access probe: HTTP 200 on 2026-06-19 (l2beat.com/scaling/summary)

## Cross-references

direct-rpc-read (higher tier for the actual bridge admin/timelock and sequencer-contract reads that F-BRG-005 and F-CHN-003 require); chain-foundation-docs (primary chain documentation L2BEAT summarises). F-CHN-003 already lists L2BEAT as a fallback source.

## Notes

Strong reputation in L2 risk; the methodology changelog makes source-side methodology changes auditable. Status candidate pending operator ratification. Reclassify to active when: (1) the operator confirms which L2BEAT surface (rendered page vs API vs GitHub data export) VaultDiligence will cite and that it is reachable without client-render loss; (2) a pack has used L2BEAT to corroborate F-CHN-003 or F-BRG-001 and A6 confirmed the bridge/sequencer claim against a direct-rpc-read; (3) the 7d freshness_max_trusted is validated against L2BEAT's actual refresh cadence for risk-profile changes.
