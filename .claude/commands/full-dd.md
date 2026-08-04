---
name: full-dd
description: Run full diligence pack for a vault. Requires D1 complete and no
  unresolved hard gates. Spawns three investigation agents (A1 Evidence,
  A2 Document and Counterparty in parallel; A3 Adversarial Synthesis after),
  then A6 Verification. Produces D3 full pack and D4 gap brief. Takes 60-90
  minutes.
---

# Full DD — D3 + D4 Pack Generation

## Prerequisite

D1 and D2 must be complete.
Load packs/{vault-slug}/D1-allocability-screen.md
Load packs/{vault-slug}/D2-executive-summary.md

VT-7 vaults require two separate full-dd runs:
  Run 1: the collateral asset (VT-3/3a)
  Run 2: the strategy protocol (VT-7)

## Pre-Dispatch Planning (RECOMMENDED)

Before launching the 3+1 agent dispatch, run a plan-mode session
(shift+tab to enter) to:

  a. Read packs/{vault-slug}/D1-allocability-screen.md and
     packs/{vault-slug}/D2-executive-summary.md, then identify the open
     questions that survived D1/D2.
  b. Seed findings-live.md with the triggers those open questions imply.
     A1/A2 will pick up these triggers when they start, instead of
     discovering the same questions again from scratch.
  c. Decide which subagents need extended scope for this vault — for
     example, VT-7 strategy protocols often need A2 to dig deeper on
     audit history; VT-3a stablecoin issuers need A1 to verify reserve
     attestations on-chain.
  d. Surface any VaultDiligence field-registry gaps for this vault type.
     If a field is needed but not in knowledge/data-model/fields/, raise
     it as a framework gap before the run, not after.
  e. Consult the incidents registry:
     `python3 scripts/load-incidents.py --vault-type <VT>`
     Each matched incident's diligence-signature fields are candidate
     findings-live triggers. After A1/A2 produce evidence, A3 will
     cross-reference the pack against the registry automatically;
     pre-seeding the triggers here means A1/A2 work toward resolving them
     during the run rather than discovering them at synthesis time.

Switch to auto-accept after the plan is solid. Long pack runs without
a plan-mode preamble tend to surface the same gaps after 60 minutes
that 10 minutes of planning would have caught upfront.

## Agent Dispatch — 3+1 scheme

The agent count is fixed: A1, A2, A3, A6.
Definitions are in `.claude/agents/architecture.md` (A1, A2, A3) and
`.claude/agents/agent-verification.md` (A6).

Each agent writes output to:
  packs/{vault-slug}/agent-outputs/{agent-name}.json

A1 and A2 run in parallel. Both read and write
`packs/{vault-slug}/agent-outputs/findings-live.md` for trigger handoffs.
See `spec/findings-live-schema.md` for the trigger contract.

### Dispatch A1: Evidence Agent
Instruction: Read .claude/agents/architecture.md "Agent 1: Evidence Agent" scope.
  Collect all on-chain and free-registry T1 fields for vault address {address}
  on {chain}. For each field: value, source URL, date, evidence state.
  Read findings-live.md at start; check periodically for new triggers from A2.
  Append on-chain verification triggers for A2 to findings-live.md as needed.
  Output: packs/{vault-slug}/agent-outputs/evidence.json

### Dispatch A2: Document and Counterparty Agent
Instruction: Read .claude/agents/architecture.md "Agent 2: Document and
  Counterparty Agent" scope. Extract from FORMAL operator documentation
  (Gitbooks, whitepapers, audits, filings) and build the counterparty register
  (named entities, registries, jurisdictions). Run all entity checks against
  GLEIF, OpenCorporates, SEC EDGAR, FCA Register, Solodit, Immunefi.
  Read findings-live.md at start; check periodically for new triggers from A1.
  Append document/counterparty verification triggers for A1 as needed.
  Output: packs/{vault-slug}/agent-outputs/evidence.json (appends to A1)
          packs/{vault-slug}/agent-outputs/counterparties.json

## Synthesis — A3 (after A1 and A2 complete)

Run A3: Adversarial Synthesis.
  Read evidence.json, counterparties.json, findings-live.md.
  Confirm every trigger in findings-live.md was resolved by A1 or A2.
  Check every E field has URL + date. Downgrade missing → E(P).
  Run all 40 red flag conditions against field values.
  Detect conflicts between A1 and A2: state I, do not resolve.
  Run scripts/validate-evidence.py disambiguation rules to surface
  source-tier-resolvable conflicts (see spec/evidence-disambiguation.md).
  Output: packs/{vault-slug}/agent-outputs/synthesis-report.json

## Verification — A6 (after A3 completes)

Run agent-verification after adversarial synthesis.
Input: synthesis-report.json + all scratchpad JSONL files.
Step limit: 60 steps. Monitor context at 70%.

Three checks in sequence:

1. Source chain tracing: for every E field, trace to primary source.
   Depth 3+ = downgrade to E(P) unless terminal source is on-chain.

2. Temporal consistency: build date matrix for all fields.
   Flag any field outside the assessment window for its type.

3. Logic gap check: read claim and source side by side.
   Downgrade where claim is more precise than source warrants.
   Zero tolerance: "typically" cited as a specific number,
   "we aim to" cited as a commitment, blog post cited as legal structure.

A6 also runs scripts/validate-evidence.py over the synthesis output to catch
document-level structural errors (missing field IDs, state-vs-source-uri
mismatches, invalid pack-completion claims).

Output: packs/{vault-slug}/agent-outputs/verification-report.json

After A6 writes the verification report, a human reviews the flagged
downgrades and decides whether to re-run: if yes, re-dispatch the agents
named in the report, scope-narrowed to the flagged fields. Maximum three
iterations per pack. After that, accept remaining gaps or scrap the pack.

Note: verification downgrades evidence states. It does not make
allocation recommendations. It does not flag conditions as blocking.
VaultDiligence never decides. The allocator or agent decides.

The final question before completing:
"Would a senior allocator with 20 years of TradFi diligence experience
find a claim here that is more confident than the evidence warrants?"
If yes: find it. Downgrade it. State why.
If no: state this explicitly. Absence of downgrades is a finding.

---

## Document Generation

After synthesis, render two documents:

D3 Full Pack: packs/{vault-slug}/D3-full-diligence-pack.md
  Six risk category sections.
  Each criterion: question asked, what was found, source, evidence state, gap.
  Comparables table (skill: comparables-table).
  Triggered conditions register.
  Source appendix.

D4 Gap Brief: packs/{vault-slug}/D4-gap-action-brief.md
  Every open gap.
  Named responsible party.
  Specific action.
  Priority: Pre-Allocation / Within 30 Days / Ongoing.

## D3 Section Structure

### VAULTDILIGENCE
#### Full Diligence Pack — [Vault Name]
Assessment date: [date] | Vault type: [VT-X]

---

#### Exit Liquidity Box
[From D1/D2 — always leads]

---

#### Vault Structure
[Block 2: what it is. Block 3: subscription/deposit flow. Block 4: redemption flow.]
[Block 5: live data at assessment date. Every field sourced.]

---

#### Legal and Custody Risk
[For each criterion in this category:]
Question: [what the criterion asks]
Finding: [what was confirmed, with source URL and date]
Evidence state: [E / E(P) / G2 / G3 / I / N/A]
Gap action: [if G2 or G3: precise action, named responsible party]

---

#### Credit and Collateral Risk
[Same structure]

---

#### Market and Oracle Risk
[Same structure]

---

#### Liquidity and Exit Risk
[Same structure]

---

#### Operational and Governance Risk
[Same structure]

---

#### Smart Contract Risk
[Same structure]

---

#### Triggered Conditions
[Every triggered red flag condition.]
[Format per condition:]

Condition ID: [RF##]
What was observed: [fact + source]
Structural consequence: [what this means structurally, no judgment]
Evidence to close: [what document or data point resolves this]
Responsible party: [who provides it]

---

#### Comparables
[Factual table. Sourced. Dated. TradFi anchor row included.]

| Vault | Type | Collateral | TVL | Net APY | Redemption | Legal | Audit | Source/Date |
|-------|------|-----------|-----|---------|------------|-------|-------|-------------|

---

#### Source Appendix
[Every source used. URL. Access date. Methodology. Tier. Reliability note.]

---

## Post-Completion Step (human writes — not agent)

After D3 and D4 are rendered and the allocator has reviewed the pack,
write the following to packs/{vault-slug}/questions-not-asked.md:

  # Questions We Did Not Ask — [Vault Name]
  Pack completed: [date]
  Reviewed by: [name]

  ## Questions that became obvious only in retrospect

  For each question:

  Question: [the question]
  Why not asked initially: [what in the process caused it to be missed]
  What evidence would close it: [specific document, API, or person]
  Vault type: [VT-X]

  ## Framework gaps surfaced by this pack

  [Any criteria that did not exist in the framework but should.
   Any field IDs that were missing. Any source that was needed
   but not in the source map.]

This file feeds knowledge/adversarial/{VT-X}.md.
After writing: copy the questions into the appropriate VT-X.md file.
That is the compounding mechanism. It is not optional.
