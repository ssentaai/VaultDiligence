---
description: VaultDiligence source authority hierarchy. Always apply.
alwaysApply: true
---

# Source Authority

## Hierarchy

ON-CHAIN beats FORMAL beats EXPERT ANALYSIS beats INFORMAL.
Higher tier supersedes lower tier when they conflict.
Same tier conflict: flag as I (Investigate). State both. Never resolve silently.

## ON-CHAIN

Read directly from contract state, transaction history, or event logs.
Independently verifiable by anyone with the address and block explorer.
Supersedes all documentation when they conflict.
Format: [value]. On-chain: [address], [function/event], block [N], [date].

## FORMAL

Authoritative published documentation or a regulated filing.
The reader can go to the URL and read the same text independently.
Includes: protocol Gitbooks, fund prospectuses, SEC filings, audit reports,
  legal opinions, regulatory registries (GLEIF, FCA, SEC EDGAR).
Format: [value]. Source: [document name], [URL], [date published].

## EXPERT ANALYSIS

Published research from recognised domain experts where methodology
is stated and claims are independently verifiable.
Cannot be the sole source for a material fact.
Must be corroborated by ON-CHAIN or FORMAL for material claims.
Includes: Particula, Credora, LlamaRisk, Gauntlet, Chaos Labs reports.
Format: [claim]. Expert analysis: [firm/author], [URL], [date].

## INFORMAL

Social posts, Discord, Telegram, interviews, press releases, blog posts.
Cannot be cited as a standalone fact.
If it appears: label explicitly as "not confirmed in formal documentation."
If the claim matters: it is a G2 gap until confirmed by FORMAL or ON-CHAIN.

## Practical application

When two sources conflict:
  Identify their tiers.
  Higher tier wins if both are the same claim.
  Same tier conflict: flag as I (Investigate), state both sources and dates.
  Do not pick the more convenient source silently.
  Do not average conflicting TVL figures.
