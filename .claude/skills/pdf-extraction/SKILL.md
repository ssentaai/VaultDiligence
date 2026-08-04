---
name: pdf-extraction
description: Extract structured fields from PDF documents. Use for audit
  reports, legal opinions, fund prospectuses, SOC-2 reports, subscription
  agreements. Runs at most once per document per session.
---

# PDF Extraction Skill

## When to Use

Audit reports: extract firm, date, scope, findings by severity,
  out-of-scope section explicitly.
Legal opinions: extract issuing firm, date, jurisdiction, key conclusions,
  limitations stated.
Fund prospectuses: extract legal structure, redemption terms, NAV methodology,
  fee structure, risk factors.
SOC-2 reports: extract type (I or II), period, auditor, exceptions noted.
Subscription agreements: extract lock-up terms, redemption notice periods,
  gate provisions, side pocket provisions.

## Process

Step 1: Identify the document type from filename and first page.

Step 2: Extract the standard fields for that document type (below).

Step 3: For every extracted value state the page number and clause.
  Format: [value]. Page [N], clause [X.Y] (if applicable).
  Never summarise without citing the specific page.

Step 4: Extract the out-of-scope section explicitly for audit reports.
  This is the most important section. If no out-of-scope section exists:
  state that explicitly. It is a gap, not an absence.

Step 5: Cross-reference out-of-scope against VT failure modes.
  Read knowledge/adversarial/{VT-X}.md.
  For each failure mode listed: is it in or out of scope?
  State the overlap explicitly.

## Standard Fields by Document Type

### Audit Report
- Audit firm name and reputation tier
- Audit date (start and end)
- Scope: contracts audited (exact list)
- Out of scope: explicitly stated exclusions
- Findings: critical, high, medium, low counts
- Resolved findings: confirmed resolved with commit hash or statement
- Unresolved findings: still open as of audit date
- Auditor notes on privileged roles
- Auditor notes on upgrade mechanisms
- Comparison to VT failure modes (knowledge/adversarial/)

### Legal Opinion
- Issuing firm
- Date issued
- Jurisdiction
- Opinion type (true sale, bankruptcy remoteness, enforceability)
- Key conclusion (one sentence)
- Stated limitations and carve-outs
- Whether opinion covers depositor claims specifically

### Fund Prospectus / Offering Memorandum
- Legal entity name and jurisdiction
- Fund structure (SPC, LP, etc.)
- Redemption terms (notice period, settlement)
- NAV calculation methodology and frequency
- Gate provisions
- Side pocket provisions
- Fee structure (management, performance, other)
- Eligible investor requirements (KYC/AML)
- Wind-down provisions

## Evidence States for PDF Fields

E    Value extracted with page citation. URL to document stated.
E(P) Value partially stated. Material qualification or gap within document.
G2   Document referenced but not publicly accessible. Request named.
G3   Document does not exist. Operator must create.

## Output Format

For each extracted field:
  Field: [field ID if applicable]
  Value: [extracted value]
  Page: [N]
  Clause: [X.Y if applicable]
  Evidence state: [E / E(P)]
  Note: [any qualification or limitation from the document]

---


## Common Rationalizations

These are the excuses agents use to skip steps in this skill.
They are documented here so they can be recognised and rejected.

| Rationalization | Reality |
|---|---|
| "I read the whole PDF, I know what it says" | Reading is not citing. Every claim needs a page number. If you cannot page-cite it, it is not E. |
| "The audit scope section is standard, no need to verify" | Audit scope exclusions are where material risks hide. Resolv had 18 audits. The scope gap was the problem. |
| "This PDF is too long to read fully" | Use scripts/extract.py --pages to read the relevant sections. Do not summarise what you have not read. |
| "The finding is marked informational, not critical" | Informational findings become critical in combination. Log all findings. The allocator assesses severity. |
| "I can summarise the key points without quoting" | Summaries introduce interpretation. Quote the exact text with page number. The allocator reads the source. |

## Verification Checklist

Exit criteria. Every item must be confirmed before the skill output
is accepted. "Seems right" is never sufficient.

- [ ] Every claim has a page number citation. No claim without a page number is E.
- [ ] Audit scope stated explicitly: what was in scope and what was explicitly excluded.
- [ ] All findings listed regardless of severity rating. Informational findings included.
- [ ] Audit date confirmed. Pack expiry calculated from audit date for audit-related fields.
- [ ] Auditor identity confirmed: named firm, named lead auditor where stated.
- [ ] No field populated from summary text without a direct page reference.
- [ ] If PDF was unreadable or pages were missing: G2 with specific pages noted.

## When NOT to Use

- The document is already in the evidence register from this session.
- The document is plain text with no structured claims (use web_fetch instead).
- The document is a marketing one-pager with no technical claims.

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
