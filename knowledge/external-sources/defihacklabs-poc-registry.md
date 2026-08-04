---
schema_version: 1
id: defihacklabs-poc-registry
name: DeFiHackLabs Incident PoC Registry
provider: SunWeb3Sec (DeFiHackLabs)
url_base: https://github.com/SunWeb3Sec/DeFiHackLabs
docs_url: https://github.com/SunWeb3Sec/DeFiHackLabs
source_tier: FORMAL
purpose:
  - exploit-incident-record
  - reproducible-root-cause-poc
  - attack-technique-classification
auth: none
access_mode: fetch
freshness_typical: weekly
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-RIS-001
  - F-RIS-006
  - F-RIS-002
fallback_sources:
  - defillama-hacks-db
  - slowmist-hacked-db
  - rekt-news-postmortems
status: active
added_in: v54
notes_url:
---

## What this source provides

Open-source GitHub repository (named directly in the field definitions: github.com/SunWeb3Sec/DeFiHackLabs) that reproduces past DeFi exploits as Foundry proof-of-concept tests, organised chronologically by year, with root-cause analysis per incident. At probing it held 725 documented incidents. Used to confirm an exploit occurred and to obtain a reproducible, inspectable root cause rather than a prose label.

## Source tier rationale

FORMAL. Attributable maintainer (SunWeb3Sec organisation), open-source with a stable maintainer community, and per-incident PoC tests that are records of record anyone can re-run to verify root cause — satisfies at least two FORMAL criteria. Not ON-CHAIN: the PoC re-executes historical chain state but the curated catalogue and classification are the methodology layer, so FORMAL.

## When to use it

Primary or strong corroborating FORMAL source for F-RIS-001 when an incident has a PoC (the reproducible test is the strongest technique/root-cause evidence short of reading the chain). Named fallback for F-RIS-006 (field definition lists DeFiHackLabs GitHub as the verify-against source when a protocol is not on Rekt). For oracle-manipulation incidents in its price-oracle category, seeds F-RIS-002. Cite the specific incident folder/file and commit or date.

## When NOT to use it

Not for incidents without a PoC entry (coverage is curated, not exhaustive; absence is not proof of no incident). Not for operator-side resolution/remediation narrative (whether a vulnerability persists in the current version requires reading current contracts, not the historical PoC). Not for non-exploit incidents — bad debt (F-RIS-005), NAV anomalies (F-RIS-004), governance-concentration without an exploit.

## Authentication and rate limits

Public, no key. Repository returned HTTP 200 to anonymous WebFetch on 2026-06-19. GitHub raw-file and API reads are rate-limited for anonymous access; use gh CLI or an authenticated path for bulk reads, and back off on 403/429 per tool-recovery. No operator credential required for single-file reads.

Access probe: github.com/SunWeb3Sec/DeFiHackLabs HTTP 200 on 2026-06-19 (README, structure, 725 incidents, 6.6k stars, 3,388 commits readable)

## Cross-references

defillama-hacks-db (structured amount/date companion — PoC here, dollar figure and classification there); slowmist-hacked-db (independent incident DB for cross-checking the incident set); rekt-news-postmortems (narrative analysis on the same incidents).

## Notes

Strongest incident source for root cause because the PoC is reproducible, rare among incident sources that publish prose only. Dollar figures are less authoritative than DefiLlama's, so pair the two (PoC here, amount from defillama-hacks-db) and flag cross-source disagreement as I (Investigate). Maintainer continuity is a single-organisation risk; if the repo stalls, defillama-hacks-db and slowmist-hacked-db remain. Reclassify to active when: (1) VaultDiligence has cited a specific DeFiHackLabs incident PoC as the root-cause source for F-RIS-001 on at least one pack and A6 confirmed it; (2) at least one cited PoC has been re-run or the test file inspected to confirm the root cause matches the field claim; (3) the curated coverage has been checked against a known incident absent from the repo to bound the absence-is-not-evidence caveat.
