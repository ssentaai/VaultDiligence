---
schema_version: 1
id: rekt-news-postmortems
name: Rekt News Exploit Post-Mortems
provider: RektHQ
url_base: https://rekt.news
docs_url: https://rekt.news/leaderboard
source_tier: EXPERT
purpose:
  - exploit-root-cause-analysis
  - incident-narrative-postmortem
  - largest-loss-leaderboard
auth: none
access_mode: fetch
freshness_typical: weekly
freshness_max_trusted: 30d
covers_chains:
  - ALL
covers_field_ids:
  - F-RIS-006
  - F-RIS-001
  - F-RIS-002
  - F-RIS-003
fallback_sources:
  - defillama-hacks-db
  - slowmist-hacked-db
  - defihacklabs-poc-registry
status: active
added_in: v54
notes_url:
---

## What this source provides

Rekt News publishes detailed narrative post-mortems of crypto exploits, hacks, and security failures, with technical breakdowns of the vulnerability and attack path, plus a leaderboard ranking incidents by financial impact. Run by RektHQ, founded by Julien Bouteloup. Used for the root-cause narrative behind an incident and as the direct answer to F-RIS-006 (the field asks 'Is this protocol listed on Rekt.news?').

## Source tier rationale

EXPERT, not FORMAL. Rekt is a named outlet (RektHQ, founder Julien Bouteloup) producing investigative analysis and opinion, not a regulator-grade record of record; individual post-mortems are editorial reconstructions, not reproducible or filed records — named reputation producing analysis, i.e. EXPERT. The committed source-authority rule treats EXPERT as unable to be the sole source for a material fact, so Rekt corroborates a FORMAL/ON-CHAIN record except for the narrow F-RIS-006 presence question.

## When to use it

Two uses. First, F-RIS-006 is a factual presence question ('is this protocol listed on Rekt.news, URL if yes') that Rekt answers directly, so Rekt supports state=E for F-RIS-006 specifically. Second, for F-RIS-001/002/003, use Rekt for the root-cause narrative as EXPERT corroboration alongside a FORMAL incident record (defillama-hacks-db, slowmist-hacked-db, or defihacklabs-poc-registry). Cite the specific article URL and date.

## When NOT to use it

Not as the sole source for a material exploit fact such as the dollar amount — that downgrades to E(P) under the EXPERT rule and needs a FORMAL corroborating figure. Not for non-exploit incidents it does not cover (bad debt F-RIS-005, NAV anomalies F-RIS-004 unless Rekt wrote them up). Not for any allocation judgement; VaultDiligence records the evidence, not the verdict.

## Authentication and rate limits

Public, no key. Homepage returned HTTP 200 to anonymous WebFetch on 2026-06-19; navigation, leaderboard, and footer attribution readable. No login or credential required. Treat anonymous reads as best-effort and back off on failure per tool-recovery.

Access probe: rekt.news HTTP 200 on 2026-06-19 (navigation, leaderboard, footer attribution to RektHQ / founder Julien Bouteloup readable)

## Cross-references

defillama-hacks-db / slowmist-hacked-db (the FORMAL incident records Rekt's narrative must corroborate for material facts); defihacklabs-poc-registry (reproducible PoC counterpart to Rekt's prose root cause); field F-RIS-006 names Rekt.news as primary source directly, and F-RIS-001/006 list DeFiHackLabs as fallback.

## Notes

Key precision point: Rekt is EXPERT, so its amounts and root-cause claims are E(P) until a FORMAL source confirms them, but the narrow F-RIS-006 question (presence on Rekt) is answered by Rekt itself and can be E. The leaderboard is useful for sizing an incident relative to the largest historical losses. RektHQ also publishes opinion pieces; only the incident post-mortems are the evidence surface here. Reclassify to active when: (1) VaultDiligence has cited a specific Rekt article as the F-RIS-006 presence answer or as EXPERT corroboration for F-RIS-001 on at least one pack and A6 confirmed it; (2) the E vs E(P) split (E for the F-RIS-006 presence question, E(P) for material exploit facts) has been applied correctly in at least one pack; (3) a Rekt root-cause claim has been confirmed against a FORMAL record to validate the corroboration workflow.
