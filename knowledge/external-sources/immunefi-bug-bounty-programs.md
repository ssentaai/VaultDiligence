---
schema_version: 1
id: immunefi-bug-bounty-programs
name: Immunefi Bug Bounty Program Directory
provider: Immunefi
url_base: https://immunefi.com
docs_url: https://immunefi.com/bug-bounty/
source_tier: FORMAL
purpose:
  - bug-bounty-scope
  - max-bounty-disclosure
  - assets-in-scope
  - responsible-disclosure-program
auth: rate-limited-anonymous
access_mode: fetch
freshness_typical: weekly
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-SEC-006
  - F-SEC-010
fallback_sources:
  - immunefi-bug-bounty-programs
  - vault-docs
status: active
added_in: v54
notes_url:
---

## What this source provides

Immunefi hosts a directory of web3 bug-bounty programs. Each program page publishes the protocol's maximum bounty, severity tiers and payout schedule, assets-in-scope (named smart-contract addresses and websites), out-of-scope items, KYC/payout requirements, and the program's last-updated state. Immunefi also runs audits, audit competitions, and Safe Harbor (on-chain responsible-disclosure) programs.

## Source tier rationale

FORMAL. Immunefi is a named firm operating a structured, consistently-formatted program directory whose listings function as records of record for a protocol's bounty scope and severity terms (researchers and protocols both rely on the published scope as authoritative). It satisfies the FORMAL two-of-four test on attributable maintainer plus records-of-record. It is not ON-CHAIN (the directory is a hosted listing, not a verified-contract read) and is more than EXPERT opinion (it is the operative program terms, not analysis).

## When to use it

Use as FORMAL evidence of a protocol's security posture inputs feeding F-SEC-006 and F-SEC-010: the assets-in-scope list corroborates which privileged contracts/roles the protocol itself treats as in-scope, and the presence, size, and scope of a live bounty (and Safe Harbor terms) is a documentable input to the security-process picture. Best when a vault's contracts appear in a current Immunefi program page within the freshness window.

## When NOT to use it

Do not treat the presence or size of a bounty as evidence that the privileged roles (F-SEC-006) or key-storage (F-SEC-010) are correctly enumerated or safe — that is bytecode enumeration and CTO disclosure, not a bounty page. Do not infer audit quality from an Immunefi listing. Scope can be marketing-shaped; verify named in-scope addresses on-chain. A paused or stale program page is not evidence of current coverage.

## Authentication and rate limits

Public program pages are reachable without authentication (root returned HTTP 200 on 2026-06-19); pages are client-rendered, so a WebFetch HTML scrape may miss program details — cite the specific program URL and transcribe scope/bounty figures honestly. No documented public API was found for bulk program data. If accessed via curl, operator adds immunefi.com to the settings.json allow-list at Step 5.

Access probe: HTTP 200 on 2026-06-19 (immunefi.com root)

## Cross-references

vault-docs (the protocol's own security/bounty disclosure, to cross-check Immunefi's listed scope); contract-reading skill and direct-rpc-read (higher-authority verification of the in-scope privileged contracts F-SEC-006 enumerates). No second bounty-aggregator is registered, so Immunefi is the single source for hosted-bounty scope (self-listed as fallback to flag that).

## Notes

Differentiated from a generic ratings source: it carries the operative bounty terms, not analysis. Status candidate pending operator ratification. Reclassify to active when: (1) a citation method is confirmed that survives client-side rendering (a stable program-page route or an Immunefi data export); (2) a VaultDiligence pack has cited an Immunefi program page to corroborate assets-in-scope for F-SEC-006 and A6 verified the in-scope addresses on-chain; (3) the 30d freshness_max_trusted plus a program-status (active/paused) check is validated, since a bounty page can go stale or be paused without notice.
