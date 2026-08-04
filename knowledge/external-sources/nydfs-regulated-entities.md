---
schema_version: 1
id: nydfs-regulated-entities
name: NYDFS Regulated Virtual Currency Entities
provider: New York State Department of Financial Services
url_base: https://www.dfs.ny.gov/virtual_currency_businesses
docs_url: https://www.dfs.ny.gov/virtual_currency_businesses
source_tier: FORMAL
purpose:
  - custodian-regulatory-status
  - trust-charter-verification
  - qualified-custodian-confirmation
auth: none
access_mode: fetch
freshness_typical: weekly
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-ENT-041
  - F-ENT-040
fallback_sources:
  - gleif-lei
  - sec-edgar-filings
status: active
added_in: v54
notes_url:
---

## What this source provides

NYDFS publishes a public list of regulated virtual currency businesses, distinguishing Virtual Currency (BitLicense) licensees from Limited Purpose Trust Company charters, with the grant date for each. Used to confirm the regulatory status and charter type of named crypto custodians including Coinbase Custody Trust Company, BitGo New York Trust Company, Gemini, and Paxos. The trust-charter distinction is material to qualified-custodian status.

## Source tier rationale

FORMAL. Maintained by NYDFS, a named state regulator; a record of record for who holds a NY charter or BitLicense. Meets FORMAL on attributable regulator maintainer and records of record. Not ON-CHAIN; not EXPERT.

## When to use it

Primary for F-ENT-041 (custodian regulatory status) and corroborating name source for F-ENT-040 when assets sit with a NY-chartered custodian. The Limited Purpose Trust Company charter is the relevant qualified-custodian marker; cite the entity row and grant date.

## When NOT to use it

Not for custodians chartered outside New York (a Wyoming SPDI, South Dakota trust, or non-US custodian will not appear; that becomes a G2 against the relevant regulator). Not for custody-agreement terms such as segregation or rehypothecation (F-ENT-042, F-ENT-043), which require the agreement. Not for insurance amounts (F-ENT-044). The page itself notes it does not capture real-time surrenders or revocations.

## Authentication and rate limits

Fully public, no auth, no key. Returned HTTP 200 to anonymous WebFetch during probing (2026-06-19) and rendered the full regulated-entities table server-side, so HTML scraping is viable. No operator credential required.

Access probe: HTTP 200 on 2026-06-19 (anonymous WebFetch; full regulated-entities table rendered server-side, listing Coinbase Custody Trust, BitGo New York Trust, Gemini, Paxos)

## Cross-references

gleif-lei-index (entity-identity cross-check for the chartered custodian's legal name); sec-edgar-filings (for custodians whose parent files with the SEC); fields F-ENT-042, F-ENT-043, F-ENT-044 (custody-agreement fields this list does not answer).

## Notes

This is a NY-specific register; many institutional crypto custodians are chartered elsewhere (Anchorage holds an OCC national trust charter; some hold Wyoming SPDI or SD trust charters), so a custodian's absence here means check the correct regulator, not that it is unregulated. The page warns it may lag voluntary surrenders and revocations, so confirm status freshness for any negative finding. Reclassify to active when: (1) VaultDiligence has cited a specific NYDFS entity row as primary source on at least one pack and A6 confirmed it; (2) the trust-charter-to-qualified-custodian mapping is validated against the F-ENT-041 field definition; (3) the page's update lag is characterised against at least one known charter change to bound freshness_max_trusted.
