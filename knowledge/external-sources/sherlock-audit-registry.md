---
schema_version: 1
id: sherlock-audit-registry
name: Sherlock Audit Contest Registry
provider: Sherlock (Sherlock Protocol)
url_base: https://audits.sherlock.xyz
docs_url: https://docs.sherlock.xyz
source_tier: FORMAL
purpose:
  - skin-in-the-game-audit-verification
  - smart-contract-audit-records
  - audit-coverage-staking-confirmation
auth: rate-limited-anonymous
access_mode: pointer-gated
freshness_typical: weekly
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-ENT-063
  - F-ENT-060
  - F-ENT-061
fallback_sources:
  - sec-edgar-filings
status: candidate
added_in: v54
notes_url:
---

## What this source provides

Sherlock runs audit contests and bug bounties in which security researchers compete on a protocol's codebase, and in its coverage model backs findings with staked capital. The public registry at audits.sherlock.xyz lists contests per protocol: scope, dates, participating researchers, leaderboards, judging/escalation status, and finished-contest results. Used to confirm whether a protocol engaged a skin-in-the-game auditor and to read the resulting audit records.

## Source tier rationale

FORMAL. Sherlock is a named firm operating a documented contest-and-coverage process (docs.sherlock.xyz) and the contest registry is a record of record for which protocols ran which audits with which scope and outcome. Meets FORMAL on attributable maintainer and records of record. Individual researcher findings are expert analysis, but the field this source primarily answers (F-ENT-063: is there a skin-in-the-game auditor) is a factual is-it-present question the registry answers directly, so it can support state=E there. Not ON-CHAIN (the coverage-stake reads would be a separate direct-rpc entry).

## When to use it

Primary for F-ENT-063 (skin-in-the-game auditor present, named firm); corroborating audit-record source for F-ENT-060 and F-ENT-061 when the protocol ran a Sherlock contest. Cite the specific contest page and date. The skin-in-the-game/coverage distinction is the meaningful quality signal F-ENT-063 asks for.

## When NOT to use it

Not for protocols that never ran a Sherlock contest (absence is not evidence of no audit; the protocol may have used Trail of Bits, OpenZeppelin, or Spearbit/Cantina, which need their own sources). Not as the sole audit record when the primary audit was a non-Sherlock firm. Not for the substance of individual findings as established fact without reading the report; findings are researcher opinion until resolved.

## Authentication and rate limits

Public, no key. The contests UI is anonymous and JavaScript-rendered, so HTML scrapes may return navigation chrome without the contest data; prefer the rendered contest page or any documented API. Reachable during probing (2026-06-19) but did not return a clean status to anonymous WebFetch due to client-side rendering. No operator credential required.

Access probe: Reachable on 2026-06-19 but JS-rendered; anonymous WebFetch returned navigation chrome (Contests/Leaderboards/Bug Bounties) without a clean status code or contest data

## Cross-references

Fields F-ENT-060/061 (general audit fields where Sherlock is one possible firm among Trail of Bits, OpenZeppelin, Spearbit/Cantina); a future direct-rpc entry would cover the on-chain coverage-stake reads backing Sherlock's model.

## Notes

Sherlock's value for diligence is the coverage/staking model, not contest volume; F-ENT-063 is specifically about financial accountability of the auditor. A finished contest with unresolved high/critical findings is a flag, not a pass, so read the contest outcome, not just its existence. Other skin-in-the-game models (Code4rena, Cantina competitions) are equivalents for F-ENT-063 and would warrant their own candidate entries. Reclassify to active when: (1) a retrieval path returning actual contest data (not just JS chrome) is confirmed against at least one finished contest; (2) VaultDiligence has cited a specific Sherlock contest as primary source for F-ENT-063 on at least one pack and A6 confirmed it; (3) the coverage-stake reading is tied to an on-chain source so the skin-in-the-game claim is corroborated beyond the dashboard.

Ratification (2026-06-19): access_mode=pointer-gated; status=candidate. JS-rendered; anonymous fetch returns navigation chrome only (2026-06-19). Analyst opens in-browser.
