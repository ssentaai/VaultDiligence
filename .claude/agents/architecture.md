# VaultDiligence Agent Architecture

## Principle

Scoped autonomy. Not workflows.

Each agent has a goal, a constraint, a scope, and a stop condition.
The agent decides how to meet the goal.
The one constraint that applies to every agent:
No fact without a verifiable primary source.

---

## Decision: Agent vs Direct Tool

Before spawning any agent, ask: can this be done in two tool calls?

Use web_search + web_fetch directly for:
  D1 allocability screen
  Single data point lookups (TVL, APY, token price)
  Comparables table data
  Quick claim verification

Spawn agents when the task requires sustained investigation
across multiple sources with judgment at each step.
D3 full pack = agents. Everything else = direct tools first.

---

## Shared Investigation State

This is the coordination mechanism. No orchestrator needed.

packs/{vault-slug}/obsidian/raw/findings-live.md is readable
and writable by all agents during their run. It is the live
signal layer between agents. Append-only during investigation.

Agents also write wiki pages to packs/{vault-slug}/obsidian/wiki/
incrementally during investigation. The wiki page for a criterion
is created when investigation starts and updated as evidence is found.
This is the live investigation state, not a post-processed output.
Full vault structure: spec/obsidian-integration.md

When any agent finds a condition that requires investigation
by another agent: append to findings-live.md immediately.

Format:
  TRIGGER | [finding] | [what needs investigating] | [field ID] | [agent scope]

Examples:
  TRIGGER | Off-chain minting role in Gitbook | Verify on-chain issuance bound | F-SEC-009 | Agent 1
  TRIGGER | the prime broker named as prime broker | Verify SIPC + FCA registration | F-ENT-041 | Agent 2
  TRIGGER | Token used as collateral in 3 protocols | Pull circuit breaker docs for each | F-CTR-008 | Agent 2
  TRIGGER | Timelock 0 hours on-chain | Verify governance docs claim 48hr | F-CTR-004 | Agent 2

Each agent:
  1. Reads findings-live.md at start of session
  2. Adds any triggers in its scope to its work queue
  3. Appends new triggers as it makes findings during investigation
  4. Checks findings-live.md again before declaring stop condition met

An agent cannot declare stop condition met if findings-live.md
contains unresolved triggers in its scope.

Agent 3 synthesis reads findings-live.md to confirm every trigger
was followed up. Unresolved triggers = open gap with action.
Never silent omission.

---

## Research Knowledge Base

Before starting any investigation, check knowledge/research/ for
pages tagged with the current vault's type and risk categories.

Read relevant research pages before going to the web.
Apply their insights. Do not re-discover what is already known.

Check knowledge/research/framework-review-queue.md for open flags
that may affect how criteria should be assessed for this vault type.

Ingest new research: /ingest [URL] from Claude Code at any time.

---

## Tool-Call Discipline (v45 / Fix 74)

Every external fetch must cite the field it is for.

When an agent calls web_fetch, WebFetch, Scrapling, WebSearch, or
bash curl, it includes a `purpose` parameter or comment:

  Format: `field=F-XXX-NNN, action=<verb>`
  Multi:  `fields=F-XXX-NNN,F-YYY-MMM, action=<verb>`

Examples:
  web_fetch(url=..., purpose="field=F-CTR-001, action=verify token contract")
  WebFetch(url=..., purpose="field=F-FIN-001, action=fetch TVL")
  Bash(command="curl ... # purpose: field=F-OPS-001, action=enumerate team")

The PreToolUse hook (.claude/hooks/validate-tool-purpose.py) validates:
  1. Purpose is present and parseable
  2. Cited field(s) exist in knowledge/data-model/fields/
  3. Cited field(s) are in the calling agent's scope per
     spec/agent-scopes.json (which mirrors the agent scopes below in
     structured form)

Agent scope is configured in spec/agent-scopes.json. When agent scopes
change here, that file must be updated.

A field is in scope for an agent if the field's family prefix
(e.g. F-CTR for F-CTR-001) is in the agent's scope_field_families
list, OR the field's Category is in the agent's scope_categories list.

Hook modes (configured in spec/agent-scopes.json):
  - default_mode: warn (will switch to block once data confirms
    scope rules are well-calibrated)
  - missing_purpose_mode: warn
  - unknown_field_mode: block (always — citing a nonexistent field
    is always wrong)
  - silent_outside_pack: true (operator-driven calls outside an
    active pack are not validated)

A3 and A6 do not normally fetch evidence themselves. The hook permits
their fetches with a warning rather than blocking, but the correct
pattern when A3 or A6 needs new evidence is to append a TRIGGER to
findings-live.md for A1 or A2 to handle.

The VAULTDILIGENCE_CURRENT_AGENT environment variable must be set when
each agent is invoked, so the hook can determine the calling agent's
scope. This is set by the agent dispatcher before running each agent.

---

## Three Agents

### Agent 1: Evidence Agent

Goal: Populate every field in the field registry for this vault
      from the most authoritative, current, verifiable source.

Constraint: ON-CHAIN beats FORMAL beats INFORMAL.
            No inference. No estimation.
            Gap when no verifiable source exists.

Scope: All fields with a primary source in on-chain state,
       live market data, or free registries.
       Reads knowledge/framework/index.md to understand what
       needs answering. Reads findings-live.md for triggers
       from Agent 2 requiring on-chain verification.

Priority: Exit Liquidity Box first.
          Three numbers confirmed or G2 before continuing.

Stop: Every in-scope field is E (URL + date) or G2/G3 with action.
      No unresolved triggers in findings-live.md for Agent 1 scope.

Output: packs/{vault-slug}/agent-outputs/evidence.json
        Schema: field_id | value | source_url | retrieved | evidence_state


### Agent 2: Document and Counterparty Agent

Goal: Extract structured evidence from all formal operator documentation
      and map every named entity in the vault structure.

These two tasks are combined because document reading surfaces
counterparties and counterparty verification requires document reading.
Splitting them creates redundant tool calls.

Constraint: FORMAL sources only.
            Every claim cites document name, URL, page or section.
            Third-party reports cited as pointers only.
            T4 gaps: output precise question + named responsible party.
            If entity cannot be independently verified: G2.

Scope:
  Documents: Gitbooks, whitepapers, governance forum, prospectus,
             SEC filings, audit reports, legal opinions where public,
             curator risk frameworks, PoR attestation pages,
             rating reports as pointers.
  Counterparties: every named entity with role, legal name,
                  entity type, jurisdiction, regulator + licence,
                  named individuals where confirmable, liability
                  in failure, governing law, enforcement venue.

Reads findings-live.md for triggers from Agent 1 requiring
document verification. Appends triggers requiring on-chain
verification back to findings-live.md for Agent 1.

Stop: Every document field E or G2/G3 with action.
      Every named entity has complete row or G2 with specific registry.
      No unresolved triggers in findings-live.md for Agent 2 scope.

Output: packs/{vault-slug}/agent-outputs/evidence.json (appends to Agent 1 output)
        packs/{vault-slug}/agent-outputs/counterparties.json

Run in parallel with Agent 1. Both read and write findings-live.md.


### Agent 3: Adversarial Synthesis

Goal: Find every fact in the combined evidence that should not be E.
      Confirm every trigger in findings-live.md was resolved.

Constraint: Produces no new data.
            Reads evidence.json, counterparties.json, findings-live.md.
            No allocation judgments. No verdicts.

Method:
  1. Source check: every E must have URL + date. Missing = E(P).
  2. Authority check: INFORMAL source cited as E = downgrade + flag.
  3. Conflict detection: Agent 1 on-chain vs Agent 2 formal disagree = I.
     State both values, both sources. Do not resolve.
  4. Incidents cross-reference (v44): run
     `python3 scripts/load-incidents.py --vault-type <VT> --pack <slug> --json`
     For every returned `pack_trigger` (a field in the current pack at the
     same gap state as a prior incident's pre-incident state), surface it
     as a finding in the synthesis report at severity `medium`. Cite the
     incident's id and the gap_action from its diligence signature. The
     pack does not "fail" on a registry match — it surfaces a documented
     historical pattern that warrants attention before pack closure.
  4. Red flag logic: run all conditions in knowledge/red-flags/ against
     field values. Deterministic. For each triggered condition:
     what was observed, source, structural consequence, what closes it.
  5. Gap audit: challenge every G2. Should it be G3?
     G2 = information exists, allocator can obtain it.
     G3 = does not exist, operator must create it.
     Wrong classification misleads the allocator.
  6. Trigger audit: every entry in findings-live.md must be either
     resolved (field updated in evidence.json) or recorded as open gap.
     No trigger disappears silently.
  7. Status label assignment: for each of the six risk categories,
     assign one status label based on the synthesised evidence.
     PASS / WATCH / CONCERN / FAIL / ASK
     Definitions in the core output rules.
     ASK requires: named individual, named organisation, exact question.
     FAIL requires: statement of what evidence would change the status.
     One label per category. Cannot be blank. Cannot be hedged.

Stop: Every field defensible. Every triggered condition recorded.
      Every gap correctly classified. Every findings-live.md entry resolved.

Output: packs/{vault-slug}/agent-outputs/synthesis.json
        Contains: corrected evidence | triggered conditions |
                  contradictions | gap register | unresolved triggers

---

## Skills (load on demand)

The agent pulls the skill it needs. Not called sequentially.

skill: pdf-extraction
  When: any PDF (audit report, legal opinion, prospectus)
  What: structured fields with page reference for every claim

skill: contract-reading
  When: ABI analysis, privileged role enumeration,
        timelock reads, oracle address identification
  What: map privileged functions, upgrade mechanism,
        hardcoded vs proxy

skill: redemption-waterfall
  When: VT-3, VT-3a, VT-7, VT-8 vaults
  What: map every counterparty T+N, sum to aggregated timeline,
        name bottleneck at each stress level

skill: web-scraping
  When: HTML documentation (Gitbooks, protocol docs, forums)
  What: Scrapling MCP, targeted extraction before passing to agent

---

## One Hook

Post-Agent-1-and-2, pre-synthesis:
When both evidence.json and counterparties.json exist:
run the eight critical conditions (RF01-RF07, RF28) against evidence.json.
If any triggered: surface immediately.
Do not wait for full synthesis.

---

## Vault Type Rules

Read vault type from knowledge/framework/vault-types/ before starting.

Structure in {leveraged,looped} (composed/leveraged vaults): two separate investigation runs required. [Phase 3 (2026-07-09): dimension gate; formerly VT-7.]
      Run 1: collateral asset. Run 2: strategy protocol.
      Never conflate. Single run = incomplete by definition.

caller_type=agent: confirm four on-chain gates before investigation. [Phase 3 (2026-07-09): VT-A retired as an archetype; a caller_type=agent overlay, not a vault type.]
      Gate A: instant 1-block withdrawal confirmed on-chain
      Gate B: upgrade timelock >= 48 hours
      Gate C: governance top-10 concentration < 60%
      Gate D: agent position cap = withdrawable x 2%
      Any gate fails: a structured output with critical_conditions_present=true. Surface immediately.

---

## Comparables (mandatory for every investigation)

Every vault returns five comparables plus one TradFi anchor.
No exceptions.

Comparables are selected by dollar mandate, not vault type.
The question: what else would this allocator consider instead?

Agent 1 populates comparable data fields from T1 sources
in parallel with the main investigation.
Comparable selection follows spec/comparables-spec.md.

Confirm each comparable is live before including it.
A wound-down or exploited comparable must be noted with context.
Check knowledge/research/ for prior work on comparable vaults first.

Comparable output feeds into:
  D2 IC Memo (summary table in Section 6)
  D3 Evidence File (full comparables section with differentiation matrix)
  DeFi Teardown (one paragraph: how subject vault sits in the competitive set)

---

## Rendering (after synthesis)

Rendering applies no judgment. Follows spec files exactly.

D2 IC Memo    -> spec/d2-output-spec.md
D3 Evidence   -> Obsidian vault structure
D4 Gap Brief  -> spec/gap-register-schema.md
structured JSON    -> spec/evidence-object-schema.md
DeFi Teardown -> spec/d5-and-defi-teardown-spec.md
Comparables   -> spec/comparables-spec.md (all output formats)

---

## What Does Not Exist Here

No orchestrator agent.
No scoring engine.
No composite calculation.
No verdict generator.
No tool routing tables.
No API endpoint lists.

Coordination is findings-live.md.
The agent finds the best source for each field.
The knowledge graph defines what needs to be found.
The spec files define what the output looks like.

---

## Correction-Capture Protocol (v43)

When the human corrects an agent during a run — either inline ("you should
have classified that as E(P), not E") or after the fact ("the next time you
see a Substack article cited as a primary source, downgrade") — the agent
captures the correction at the moment it happens, not at end-of-session.

Two destinations:

1. `lessons.md` (project root). Append the correction as a one-line rule:
   `- When <pattern>, do <action>. (corrected on YYYY-MM-DD by human)`
   This is for investigation rules that apply across packs.

2. the working session notes "Active Hypotheses" or "Checkpoints"
   section, as appropriate. This is for the local session's working state.

The dream cycle later harvests episodic entries that referenced the
correction and surfaces them as candidate semantic lessons (v40 staging
protocol). The synchronous append to `lessons.md` is the working-context
fix; the asynchronous staging protocol is the cross-pack lesson surface.
Both run.

Boris Cherny tip 4 of part 1 / tip 3 of part 2: "After any correction,
end with: 'Update your <memory-file> so you don't make that mistake
again.'" VaultDiligence's adaptation: lessons.md for investigation rules,
WORKSPACE.md for session state, and let the dream cycle handle cross-pack
synthesis.

---

## Operator Setup for Tool-Call Discipline (Fix 74 + Fix 77)

The validate-tool-purpose.py hook needs to know which agent is making
each call. It reads this from the VAULTDILIGENCE_CURRENT_AGENT env var.

Set this env var to the current agent's ID (one of the IDs defined in
spec/agent-scopes.json) before that agent's tool calls, and clear it when done.

The dispatcher validates the agent ID against the scope config before
emitting the export, so typos are caught immediately rather than
silently producing the wrong attribution.

If the env var is not set, the hook will:
  - Emit a warning to stderr (visible to agent on next turn)
  - Allow the call through
  - Skip the per-agent scope check

This is the deliberate fail-soft behavior. The hook still validates
purpose presence and field-existence even without agent identity —
it just can't enforce per-agent scope.

Phase C (deferred — Fix 77 in fixes.md): per-agent definition files
with embedded init steps that auto-set the env var on agent invocation.
That removes even the eval step. Until built, operator runs the eval.
