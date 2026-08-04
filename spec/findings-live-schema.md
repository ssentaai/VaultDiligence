# findings-live.md Schema

The trigger protocol for inter-agent coordination during a full-dd run.

## Purpose

A1 (Evidence) and A2 (Document and Counterparty) run in parallel. Each will discover facts the other needs to verify. Without a shared protocol, this happens implicitly — A1 finds something on-chain, hopes A2 sees it, hopes A2 verifies it, and there's no contract for what counts as "verified" or "unresolved."

`findings-live.md` is the explicit contract. It is a typed, append-only log of triggers that one agent has raised for another. A3 (Adversarial Synthesis) later reads it to confirm every trigger was resolved before the pack closes.

## Location

`packs/{vault-slug}/agent-outputs/findings-live.md`

One file per pack. Created by whichever agent runs first. Both A1 and A2 hold it open for read+append throughout their runs.

## Trigger format

Every trigger is one block. Format is fixed:

```
TRIGGER ID: T-001
RAISED BY:   A1 | A2
RAISED AT:   <ISO 8601 datetime>
TARGET:      A1 | A2
FIELD:       F-XYZ-NNN | none
ACTION:      <one-sentence verification action>
CONTEXT:     <one or two sentences of why this matters>
STATUS:      OPEN | RESOLVED | STALE
RESOLVED BY: <agent_id, only when STATUS=RESOLVED>
RESOLVED AT: <ISO 8601 datetime, only when STATUS=RESOLVED>
RESOLUTION:  <one-sentence summary, only when STATUS=RESOLVED>
```

Trigger IDs are sequential (`T-001`, `T-002`, ...) and assigned by the raising agent based on the highest existing ID in the file plus one.

## Status lifecycle

```
OPEN ──[target agent verifies]──> RESOLVED
   │
   └──[A3 finds trigger > 24h old, never resolved]──> STALE
```

A3 raises every STALE trigger as a finding in the synthesis report. Stale triggers are not silently dropped — they appear in the gap register with a specific resolution action.

## Required field contracts

**TRIGGER ID** must be unique within the file. A repeat ID is a hard error and the writer must select the next available number.

**RAISED BY ≠ TARGET** — an agent cannot raise a trigger to itself. Use scratchpad notes for self-reminders.

**FIELD** must be a real field ID from `knowledge/data-model/fields/`, or the literal string `none` for triggers that aren't field-specific (e.g. "verify whether this auditor's address is the same one cited in the Gitbook").

**STATUS** is `OPEN` at write time. Only the target agent can transition `OPEN → RESOLVED` and only when it has produced the verification action's evidence object. A3 transitions `OPEN → STALE` based on age and absence of resolution.

**ACTION** is imperative voice, one sentence, specific. Examples:
- ✓ `Verify off-chain minting role bound to multisig 0xABC...`
- ✓ `Confirm the prime broker SIPC + FCA registration via T1 sources`
- ✗ `Maybe check the auditor` (not specific)
- ✗ `Look into the timelock situation` (not actionable)

## Examples

```
TRIGGER ID: T-001
RAISED BY:   A1
RAISED AT:   2026-05-12T10:14:00Z
TARGET:      A2
FIELD:       F-CTR-008
ACTION:      Confirm Gitbook section 4.2 still names Steakhouse Labs as curator after the May 2026 governance vote.
CONTEXT:     On-chain governance shows curator role transferred to 0xFOO... on 2026-05-08. Gitbook may be stale.
STATUS:      OPEN

TRIGGER ID: T-002
RAISED BY:   A2
RAISED AT:   2026-05-12T10:42:00Z
TARGET:      A1
FIELD:       F-SEC-009
ACTION:      Verify on-chain that minting role is bound to the multisig named in the Gitbook (0xABC...).
CONTEXT:     Gitbook claims minting is multisig-protected; on-chain verification needed before this can be E.
STATUS:      RESOLVED
RESOLVED BY: A1
RESOLVED AT: 2026-05-12T10:58:00Z
RESOLUTION:  On-chain MINTER_ROLE bound to 0xABC... per AccessControl read at block 19847211.
```

## Validator

`scripts/validate-findings-live.py` (next session) parses the file and enforces:
- Sequential, unique trigger IDs
- Valid agent IDs (A1 or A2 only at this stage; future agents extend)
- Self-trigger rejection (RAISED BY ≠ TARGET)
- Field IDs match the registry
- RESOLVED triggers have RESOLVED BY/AT/RESOLUTION populated
- Datetime parse-ability

Until that validator exists, the format is enforced by review at A3 synthesis time.

## Why markdown not JSON

The file is co-edited by two parallel agents. Markdown's append-only feel and human-readable diff make race conditions detectable in `git status`. JSON would technically be cleaner but the parallel-write semantics are operationally fragile when two agents are writing inside seconds of each other.

## Cross-references

- `.claude/agents/architecture.md` — agent scopes that produce and consume triggers
- `.claude/commands/full-dd.md` — dispatch sequence
- `spec/evidence-disambiguation.md` — what happens when A1 and A2 produce conflicting evidence after triggers are resolved
