# Gap Register Schema

## Purpose

Every open gap in a VaultDiligence investigation has a structured record.
This schema governs both the JSON representation (for agent processing)
and the Obsidian note frontmatter (for persistence and answer capture).
The schema is the contract between the investigation agent, the answer
ingestion layer, and the document generation layer.

---

## JSON Schema

```json
{
  "gap_id": "string — G-{vault_slug}-{sequence_number} e.g. G-example-vault-004",
  "vault_slug": "string — e.g. example-vault",
  "field_id": "string — e.g. F-LEG-011",
  "criterion_id": "string — e.g. 1.3",
  "pillar": "string — e.g. P1",
  "risk_category": "enum — Legal and Custody Risk | Credit and Collateral Risk | Market and Oracle Risk | Liquidity and Exit Risk | Operational and Governance Risk | Smart Contract Risk",
  "question": "string — precise question. One question per gap. If multiple questions are needed: create multiple gaps.",
  "evidence_state": "enum — G2 | G3",
  "gap_type": "enum — On-Chain Verification | Market Data | Document Review | Legal Opinion (Vault) | Legal Opinion (Allocator) | Human Interview | Discrepancy | Curator Track Record | Governance Documentation | Stack Documentation | Insurance | Performance Data",
  "responsible_party": {
    "entity": "string — named entity e.g. Fund Manager Ltd",
    "contact_name": "string — named individual e.g. Fund Manager CEO",
    "contact_email": "string — e.g. ceo@entity.com",
    "role": "string — e.g. CEO / Legal Counsel / Fund Administrator"
  },
  "closure_pathway": "enum — direct_request | allocator_counsel",
  "response_type": "enum — document_upload | text_confirmation | url | on_chain_query",
  "specific_action": "string — precise instruction: what document, what API call, what question to ask, what URL to check",
  "priority": "enum — pre-allocation | within-30-days | ongoing",
  "triggered_conditions": ["string — list of RF IDs this gap affects e.g. RF09"],
  "red_flag_if_unresolved": "string — what structural condition persists if gap is not closed",
  "status": "enum — open | answered | closed | not-applicable",
  "opened_date": "string — ISO 8601 e.g. 2026-04-14",
  "answer": "string | null",
  "answer_source": "string | null — URL or file path",
  "answer_date": "string | null — ISO 8601",
  "closed_by": "string | null — email of person who provided the answer",
  "evidence_state_after_closure": "enum | null — E | E(P) | N/A"
}
```

---

## Obsidian Note Frontmatter Template

Every gap becomes a markdown note in `gap-queue/{priority}/` in the Obsidian vault.
The frontmatter is machine-readable. The note body is human-readable.

```markdown
---
# Worked example from a preferred-equity-backed vault investigation
gap_id: G-{vault-slug}-{NNN}
vault: {vault-slug}
field_id: F-LEG-011
criterion_id: "1.3"
pillar: P1
risk_category: Legal and Custody Risk
evidence_state: G2
gap_type: Legal Opinion (Vault)
priority: pre-allocation
triggered_conditions: [RF09]
responsible_entity: {entity name}
responsible_contact: {contact name}
responsible_email: {contact email}
response_type: document_upload
status: open
opened: 2026-04-14
answer: null
answer_source: null
answer_date: null
closed_by: null
evidence_state_after: null
---

## Question

Has Tier-1 legal counsel produced a written opinion confirming that the
a preferred-equity-backed token token holder's principal claim is court-enforceable in a court of
competent jurisdiction, independent of smart contract operation?

## Why This Matters

Without a written legal opinion, the claim exists only in the smart contract.
If the contract fails or is exploited, there is no independent legal mechanism
for the depositor to recover their principal. This is criterion 1.3
Claim Enforceability. RF09 is triggered until resolved.

## Specific Action

Request from the issuer contact ([contact email redacted]): written legal opinion from
Tier-1 counsel (Fenwick & West, Perkins Coie, or equivalent) confirming:
(1) governing law for the preferred-equity-backed token token holder's claim,
(2) the claim is court-enforceable independent of smart contract operation,
(3) jurisdiction for dispute resolution.
Verbal confirmation from the team does not satisfy this requirement.

## Evidence Required to Close

Written legal opinion PDF. Counsel firm name, date, specific confirmation
of enforceability. Upload to this note or the Notion gap table.

## Structural Consequence if Unresolved

a preferred-equity-backed token holder's legal recourse if the protocol fails depends entirely on
smart contract execution. No court jurisdiction confirmed. Recovery in
insolvency or exploit scenario is uncertain.

## Links

- [[criteria/1.3-claim-enforceability]]
- [[vaults/example-vault/index]]
- [[red-flags/RF09]]
- [[issuers/example-issuer/profile]]
```

---

## Evidence State Enum

| State | Meaning | Agent action on receipt |
|-------|---------|------------------------|
| G2 | Information exists but not publicly accessible | Route to named responsible party via email or Notion |
| G3 | Information does not exist publicly | Route to issuer team — they must create and publish |

---

## Priority Definitions

| Priority | Definition | Action |
|----------|------------|--------|
| pre-allocation | Must be resolved before any capital can be deployed | Allocator informed. D2 Section 6 lists these explicitly. Pack is incomplete until resolved. |
| within-30-days | Should be resolved within 30 days of initial investigation | D4 action list. Allocator monitors. |
| ongoing | Continuous monitoring item | Vault Health Metrics. Not a blocker. |

---

## Gap Type to Resolution Skill Mapping

| Gap Type | Resolution Approach | Timeline |
|----------|--------------------|---------| 
| On-Chain Verification | Agent runs specific contract call or API query immediately | Immediate |
| Market Data | Query DefiLlama, DexScreener, 1inch, CoinGecko | Immediate |
| Document Review | Request from operator. Read primary source. Note page/clause. | 5-10 business days |
| Legal Opinion (Vault) | Request from vault operator's Tier-1 counsel | 2-4 weeks |
| Legal Opinion (Allocator) | Allocator engages own counsel. Not a VaultDiligence task. | 2-4 weeks |
| Human Interview | Schedule with named entity. Record verbatim. | 1-3 weeks |
| Discrepancy | Contact operator to confirm correct figure. Document both values. | 3-5 business days |
| Stack Documentation | Request from protocol teams. Map all dependency layers. | 2-3 weeks |

---

## Answer Ingestion Logic

When an answer is received (via email reply or Notion update):

1. Extract the specific claim that closes the gap.
2. Identify the source: URL or file path. Record date.
3. Update frontmatter: status → answered, answer, answer_source, answer_date, closed_by.
4. Evaluate whether the answer fully closes the gap or partially:
   - Fully closes: evidence_state_after → E. Status → closed.
   - Partially closes: evidence_state_after → E(P). Status → answered. Create child gap for remaining portion.
   - Does not close: status remains open. Note reason.
5. Rerun triggered condition logic for all RF IDs in triggered_conditions.
6. Rebuild D4 gap register from updated notes.
7. Rebuild D2 Section 6 pre-allocation conditions if a pre-allocation gap closes.
