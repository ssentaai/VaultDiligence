---
name: comparables-table
description: Build factual side-by-side comparables table. Same fields for
  every vault. Sourced and dated. Always includes TradFi anchor row. No
  judgment column. Runs once per vault investigation.
---

# Comparables Table Skill

## When to Use

Every D3 full pack. No exceptions. Five comparables plus one TradFi anchor.

## Selection Criteria

Select by dollar mandate: what else would this allocator consider?
Not by vault type similarity alone.

Five comparables:
  Two to three of the same vault type (direct alternatives).
  One to two adjacent vault types with similar yield/risk mandate.
  Always confirm each comparable is live before including.
  Check knowledge/research/ for prior comparable work first.

One TradFi anchor:
  The most direct TradFi equivalent by mandate.
  VT-1 USDC: T-bill money market fund (e.g. SGOV, BIL).
  VT-3a tokenised T-bill: a tokenized CLO fund CLO ETF on NYSE.
  VT-2 delta-neutral: prime brokerage repo rate.
  Source from Bloomberg, fund factsheet, or SEC filing.

## Standard Fields (same for every row)

All fields must have a source URL and retrieval date.
If a field cannot be sourced: state G2 or G3. Do not estimate.

| Field | Source |
|-------|--------|
| Vault / fund name | Issuer page |
| Vault type | Classification |
| Primary collateral / underlying | Protocol docs |
| TVL / AUM ($M) | DefiLlama or fund factsheet |
| Net APY to depositor | Vaults.fyi share-price basis |
| Yield vs 3M T-bill (bps) | FRED DGS3MO cross-ref |
| Redemption timeline (standard) | Protocol docs or prospectus |
| Legal structure | Formal documentation |
| Audit firm(s) and most recent date | Solodit or issuer page |
| Bug bounty max payout | Immunefi or G3 |
| Chain | On-chain confirmation |
| Custody model | Protocol docs |
| Third-party assessment | Particula/Credora link + date |

## What Not to Include

No judgment column. No "subject advantage Y/N."
No colour coding that implies a verdict.
No ranking or ordering that implies preference.
No fields that cannot be sourced from a primary or formal source.

## Process

Step 1: Check knowledge/research/ for any prior comparable work.
  Do not re-fetch data already confirmed in a prior session.

Step 2: Identify five comparables and one TradFi anchor.
  Confirm each is live: current TVL > $0, not deprecated.

Step 3: For each comparable, run T1 sources:
  DefiLlama for TVL and APY.
  Vaults.fyi for share-price APY.
  FRED for risk-free rate cross-reference.
  Protocol docs / Scrapling for redemption and legal structure.
  Solodit for audit confirmation.
  Immunefi for bug bounty.

Step 4: For TradFi anchor:
  Bloomberg ticker or SEC EDGAR for AUM.
  Fund factsheet for yield and redemption.
  State explicitly: "TradFi equivalent — for yield premium context only."

Step 5: State evidence state for each cell.
  E: sourced with URL and date.
  G2: information exists but not publicly accessible.
  G3: information does not exist publicly.

Step 6: Render table. Every cell: value | source URL | retrieval date.
  Cells with G2 or G3: state the gap explicitly in the cell.

## Output Format

COMPARABLES TABLE — [Subject Vault] — [Assessment Date]

Note: Factual data only. All values sourced and dated.
No judgment, ranking, or advantage assessment.
Allocator draws their own conclusions.

| | [Subject] | [C1] | [C2] | [C3] | [C4] | [C5] | [TradFi] |
|--|--|--|--|--|--|--|--|
| Type | | | | | | | TradFi anchor |
| Collateral | | | | | | | |
| TVL/AUM | | | | | | | |
| Net APY | | | | | | | |
| vs T-bill (bps) | | | | | | | |
| Redemption | | | | | | | |
| Legal | | | | | | | |
| Audit | | | | | | | |
| Bug bounty | | | | | | | |
| Chain | | | | | | | |
| Custody | | | | | | | |
| 3rd party | | | | | | | |

Sources: [list each source URL with retrieval date]

---


## Common Rationalizations

These are the excuses agents use to skip steps in this skill.
They are documented here so they can be recognised and rejected.

| Rationalization | Reality |
|---|---|
| "I know the comparable vaults from the DeFi ecosystem" | Training data is stale. TVL, APY, and vault structure change weekly. Fetch current data for every comparable. |
| "Five comparables is too many, three is enough" | Five comparables plus one TradFi anchor is the minimum for a credible comparables table. Less is not sufficient. |
| "The TradFi anchor is obvious, no need to include it" | TradFi allocators need the explicit bridge. The tokenized CLO fund or T-bill equivalent anchors the yield conversation. |
| "I can estimate APY from the protocol's marketing materials" | Marketing APY and share-price-basis APY diverge. Use share price methodology. Source from Vaults.fyi. |
| "Adding a judgment column would be more useful for the allocator" | No judgment column. No advantage assessment. Factual side-by-side only. The allocator judges. |

## Verification Checklist

Exit criteria. Every item must be confirmed before the skill output
is accepted. "Seems right" is never sufficient.

- [ ] Five comparables present plus one TradFi anchor row.
- [ ] Every cell has a source URL and retrieval date. No cell is blank or estimated.
- [ ] APY uses share-price-basis methodology, not marketing APY.
- [ ] TVL is from DefiLlama or Morpho API, retrieved within 24h of assessment date.
- [ ] No judgment column. No advantage or disadvantage language.
- [ ] TradFi anchor row present: T-bill, a tokenized CLO fund, or equivalent named with current yield sourced from FRED.
- [ ] Comparables selected by dollar mandate alignment, not by name recognition.

## When NOT to Use

- Comparables table already complete in evidence register from this session.
- D1 only run (comparables are D2/D3 output, not D1).
- Vault type has no meaningful comparables (rare — note explicitly if so).

---

## Self-Rewrite Protocol

After every 5 uses OR on any failure:

1. Read any recorded session learnings
   tagged with this skill name.
2. Read this skill's KNOWLEDGE.md for existing accumulated lessons.
3. Check: are there new patterns, recurring failures, or changed assumptions?
4. If yes:
   a. Append new lessons to KNOWLEDGE.md (never delete existing lessons).
   b. Update trigger phrases if a new trigger pattern has emerged.
   c. Update constraints if a safety-relevant pattern was found.
   d. Update procedures only if a step is now obsolete or incorrect.
5. If a constraint was violated during execution: escalate to
   a durable lessons record (not just this skill's local KNOWLEDGE.md).
6. Do NOT rewrite on every run. Only rewrite when evidence is clear.

Most runs produce nothing worth changing. Conservative updates only.
