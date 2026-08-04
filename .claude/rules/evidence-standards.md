---
description: VaultDiligence evidence state definitions. Always apply.
alwaysApply: true
---

# Evidence Standards

## Evidence States

E      Evidenced. Primary source confirmed. URL cited. Date stated.
       Format: [value]. Source: [name], [URL], retrieved [YYYY-MM-DD].

E(P)   Partial. Something confirmed but material gap remains.
       OR: source exists but URL or date is missing.
       OR: source chain depth > 2 steps without terminal primary source.
       OR: claim is more precise than source text warrants.

G2     Gap: information exists but is not publicly accessible.
       Action: name the entity, the specific document required, why it matters.
       Do not use G2 when the information simply does not exist. That is G3.

G3     Gap: information does not exist publicly.
       Action: operator must create and publish it.
       Challenge every G2 — most G2s are actually G3.

I      Investigate: conflicting sources. State both with URLs and dates.
       Do not leave unresolved in a final pack.
       Do not pick one source silently.

N/A    Not applicable to this vault type. State explicitly why.
       Never use N/A to avoid a difficult criterion.

## Downgrade triggers

Downgrade E to E(P) when:
  Source chain depth exceeds 2 steps without terminal primary source.
  Claim is more specific than source text supports.
  Retrieval date exceeds threshold for this field type.
  Source is EXPERT ANALYSIS without primary corroboration for material facts.

## The gap is the finding

A gap stated clearly is more valuable than a fact stated wrongly.
A wrong fact is worse than no fact.
