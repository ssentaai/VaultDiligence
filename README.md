# VaultDiligence by Sonny Sood

https://enta.ai/
https://templewood.io/ 

**An open due-diligence framework for onchain yield vaults.**

VaultDiligence is a structured, evidence-first methodology for assessing tokenized and
onchain yield vaults — DeFi lending vaults, tokenized funds, synthetic-dollar vaults,
structured-credit wrappers, and the counterparties behind them. It is a **template of
questions, not a set of answers**: a reusable framework you apply to any vault to produce a
sourced, gap-honest diligence pack.

> **The one rule: evidence only, gaps stated, the allocator decides.**
> No scores. No ratings. No recommendations. VaultDiligence surfaces what is evidenced and
> what is missing — it never tells you whether to allocate.

---

## Why it exists

Most vault "risk write-ups" assert conclusions without showing their evidence, and hide the
gaps that matter most. VaultDiligence inverts that: every claim carries a source and a date,
every missing piece is classified and given a precise action to close it, and conflicting
sources are flagged rather than silently resolved. A gap stated clearly is more valuable than
a fact stated wrongly.

---

## Architecture

### 1. Pillars (P0–P18)
Risk is organised into eighteen pillars. Each pillar is a set of criteria with an
institutional standard, a red-flag condition, and a failure-case anchor.

| | | | |
|---|---|---|---|
| **P0** Project Gate | **P1** Legal | **P2** Custody | **P3** Oracle |
| **P4** Collateral | **P5** Hedge | **P6** Credit | **P7** Smart Contract |
| **P8** Team & Ops | **P9** Liquidity | **P10** Regulatory | **P12** Bridging |
| **P13** Chain | **P14–P16** Risk Control Operator | **P17** Counterparty & Role Registry | **P18** Party Standing |

*(P11 is reserved for a future token-mechanics pillar.)*

### 2. The field model (~420 fields)
Each pillar is decomposed into atomic **fields** — one precise question each — grouped into
clusters by prefix (e.g. `F-FIN` financial metrics, `F-CTR` contract configuration, `F-ROL`
counterparty registry, `F-LEG` legal/discretionary powers, `F-STR` strategy risk, `F-BRG`
bridging, `F-CHN` chain, `F-STD` party standing). Every field defines what to collect, its
primary and fallback sources, the evidence pathway, the institutional standard, and the exact
action to take if the answer is not found.

### 3. Archetype classification
Before assessment, a vault is classified on separable **dimensions** — primary
economic-**Exposure**, plus **Strategy**, **Management**, **Structure**, **Seniority**,
**Liquidity**, and a venue-of-primary-risk flag — with separate **risk-attributes**
(concentration, maturity, liquidity-mismatch). The archetype routes which fields, which
expected documents, and which red flags apply. A clean tuple is not a clean vault — the
archetype tells you *what to look at*, never *whether it's safe*.

### 4. Evidence-states
Every value carries one state, so a reader always knows how much weight it can bear:

| State | Meaning |
|---|---|
| **E** | Evidenced — primary source confirmed, URL + date cited |
| **E(P)** | Partial / indicative — a material gap or secondary-source caveat remains |
| **G2** | Gap: information exists but is access-restricted (a request item) |
| **G3** | Gap: information does not exist publicly (must be created/published) |
| **I** | Investigate — sources conflict; both stated, never silently resolved |
| **N/A** | Not applicable to this vault's archetype (with a stated reason) |

### 5. The document standard + minimum-DD floor
A canonical, archetype-routed **critical-document directory** defines the documents that
constitute the minimum for credible diligence, and a **minimum-DD floor** states the
completeness threshold beneath which an assessment is a surface read rather than diligence —
reported as a factual count ("X of Y floor-critical documents obtained"), **never** a verdict
on the vault.

---

## How to use it

1. **Classify** the vault on the archetype dimensions (`knowledge/framework/archetype/`).
2. **Route** to the applicable pillars and fields for that archetype.
3. **Source** each field, recording value + evidence-state + source + as-of-date. Never infer;
   state the gap with its action.
4. **Audit documents** against the critical-document directory and compute the minimum-DD
   floor.
5. **Assemble** the pack: obtained evidence, gaps as first-class findings, conflicts flagged,
   and the document-request list (the framework generates the precise ask).

The framework ships as plain Markdown so it is diffable, forkable, and toolable. The `spec/`
schemas define the evidence object, the availability states, and the output formats; the
`.claude/` directory ships the methodology as agent skills for those who want to run it with
an AI assistant.

---

## Repository layout

```
knowledge/framework/pillars/      P0–P18 criteria
knowledge/framework/archetype/    dimension vocabulary, document standard, expected-doc routing
knowledge/data-model/fields/      ~420 field definitions (the questions)
knowledge/data-model/sources/     source-venue registry
knowledge/external-sources/       external data-venue registry
knowledge/red-flags/              red-flag conditions
knowledge/framework/scenarios/    stress scenarios
knowledge/framework/vault-types/  legacy vault-type notes
knowledge/adversarial/            adversarial-lens prompts
knowledge/incidents/              public incident case studies
spec/                             evidence-object, availability-state, and output schemas
.claude/                          the methodology as agent rules, skills, commands
scripts/                          validation and build tooling
```

---

## Author / Contact

By **Sonny Sood**
Website: **https://sonny.templewood.io/**
LinkedIn: **https://www.linkedin.com/in/sonnysood**
Email: **sonny@enta.ai**

---

## License

**MIT — see [LICENSE](LICENSE).**

---

## Contributing

Contributions that add fields, sharpen criteria, extend the archetype vocabulary, or seed a
new archetype's document set are welcome. The non-negotiable rule holds for every contribution:
**evidence only, gaps stated — never a score, rating, or recommendation.**
