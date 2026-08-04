# D2 Executive Summary — Output Specification

## Purpose

IC-ready 2-page summary for CIO, CFO, or investment committee chair.
Standard risk taxonomy throughout. Dollar figures at implied position size.
No scores. No ratings. No verdicts. Evidence and gaps only.

---

## Sequence (mandatory — do not reorder)

### Section 1: Investment Case
Three fields. The filter. If the yield premium does not justify the risk
complexity, the IC stops here and the remaining sections are not needed.

| Field | Field ID | Format | Source |
|-------|----------|--------|--------|
| What it is | F-ENT-001 | One sentence. Declarative. No marketing. | Gitbook / prospectus |
| TradFi direct equivalent | F-MKT-003 | Named instrument. e.g. "CLO ETF", "T-bill MMF", "Prime brokerage repo" | Analyst judgment |
| Net yield premium vs TradFi equivalent | F-MKT-004 | bps. Negative = underperforms TradFi. | FRED + operator disclosure |

---

### Section 2: Exit Liquidity Box
Always here. Always sourced. Never estimated. If any number is G2 or G3,
state the gap and the action before proceeding.

| Field | Field ID | Format | Source |
|-------|----------|--------|--------|
| Max position at 1% slippage | F-FIN-040 | $M | 1inch Pathfinder API at exact token/chain/amount |
| Redemption timeline — standard | F-FIN-043 | T+N. Every step named. Every counterparty named. | Cross-interview mapping |
| Redemption timeline — stress | F-FIN-044 | T+N worst case. Named conditions extending timeline. | Operator disclosure + protocol docs |
| Largest single redemption processed | F-FIN-045 | $M | Operator disclosure — G2 if unconfirmed |
| Implied max allocation ($500M portfolio, standard liquidity limits) | derived | $M | Derived from F-FIN-040. State method. Not a recommendation. |

---

### Section 3: The IC Question
One paragraph. The specific decision this allocator faces.
What is confirmed, what remains open, what the committee must resolve.
Drafted from the evidence. Not a recommendation. The question, not the answer.

---

### Section 4: Risk Summary
Six categories. Standard market taxonomy. No family codes. No scores.
For each category:
- What was confirmed (sourced facts, URL cited)
- What is not yet confirmed (open gaps with evidence state and action)
- Worst-case structural consequence at implied position size ($, not %)

| Category | Pillars |
|----------|---------|
| Legal and Custody Risk | P1, P2 |
| Credit and Collateral Risk | P4, P5, P6 |
| Market and Oracle Risk | P3 |
| Liquidity and Exit Risk | P9 |
| Operational and Governance Risk | P8, P10 |
| Smart Contract Risk | P7 |

Format per category:
```
## Legal and Custody Risk — [PASS / WATCH / CONCERN / FAIL / ASK]

Confirmed: [fact + source URL + date]
Not confirmed: [gap description — evidence state G2/G3 — action]
Worst case at [$Xm implied position]: [dollar figure + named scenario]
Triggered conditions: [RF number + one-line observation if any]

[If WATCH]: Monitor: [what to watch] — escalates to CONCERN if [threshold].
[If CONCERN]: Action: [specific gap] — [responsible party] — [document required].
[If FAIL]: Unresolvable with current evidence: [what is missing and why it matters].
[If ASK]: Ask: [named individual], [organisation] — [exact question or document].
```

Status label definitions: the core output rules section.
The label is the navigation signal. The evidence below it is the substance.
Never use a label without the full evidence block.

---

### Section 5: Counterparty Map
Every named entity in the vault structure. One row per entity.
Source: Agent 3 counterparty register output.

| Entity | Role | Jurisdiction | Regulator / Licence | Liability if they fail | Evidence |
|--------|------|-------------|--------------------|-----------------------|----------|

---

### Section 6: Pre-Allocation Conditions
Three to five items maximum. Hard requirements before capital deploys.
Pulled from D4 gap register — pre-allocation priority only.

| Gap ID | What is needed | Who provides it | Why pre-allocation |
|--------|---------------|-----------------|-------------------|

---

### Section 7: Evidence Base
One row. Gives the IC a confidence metric on diligence completeness.

| Criteria with confirmed sources (E) | Partial (E(P)) | Gaps requiring operator docs (G2) | Gaps requiring creation (G3) | Triggered conditions |
|--------------------------------------|----------------|-----------------------------------|------------------------------|---------------------|

Reference: Full evidence record in D3. Action list in D4.

---

### Section 8: Pack Validity (mandatory footer)
| Field | Field ID | Value |
|-------|----------|-------|
| Evidence date | F-PKG-002 | Date all T1 data collected |
| Pack expires | F-PKG-003 | Evidence date + decay period (standard: 30 days, VT-8: 30 days) |
| Immediate rerun triggers | F-PKG-004 | List conditions requiring immediate rerun |

VT-8 specific rerun triggers: issuer quarterly earnings, dividend rate change,
prime broker regulatory action, oracle configuration change, TVL change >20%.

---

## VT-8 Additions (TradFi-Primary / Onchain-Wrapped)

Add between Section 1 and Section 2:

### Yield Quality
| Field | Field ID | Format |
|-------|----------|--------|
| Net Realised Yield (single mandatory number) | F-FIN-071 | Gross APY minus all costs. State each deduction. |
| Yield Obligation Type | F-FIN-072 | Contractual / Discretionary. Source: issuer prospectus. |
| Return of Capital Classification | F-FIN-073 | Y/N and %. Source: SEC Form 8937. |
| Single Underlying Concentration | F-FIN-075 | % and named issuer. 100% requires explicit disclosure. |
| Secondary Yield Floor | F-FIN-076 | % if primary source fails. State 0% if none. |

### Tax Position (conditional — TradFi-backed vaults only)
| Field | Field ID | Format |
|-------|----------|--------|
| Underlying Instrument Tax Character | F-TAX-001 | ROC / ordinary income / qualified dividend / mixed. Source: Form 8937. |
| Prime Broker Identity and SIPC Status | F-CUS-001 | Named prime broker. SIPC confirmed Y/N. |

---

## Hard Rules

Use exactly the five status labels defined in the core rules. No other labels.
Never use AUTO-DISQUALIFIER or BLOCKING.
Triggered conditions are observations: state what was found, source,
structural consequence. Allocator decides what it means.
Worst-case figures must be in dollars at implied position size, not percentages.
IC Question is always Section 3, not the closing item.

---

## Loss Scenario Register (Fix 14)

Add as Section 4b immediately after Risk Summary (Section 4).

Six entries. One per risk category. Dollar figures at implied position size.
Not percentages. Not ranges. Named scenario with named mechanism.

### Format per entry

Category: [Legal and Custody / Credit and Collateral / Market and Oracle /
           Liquidity and Exit / Operational and Governance / Smart Contract]
Trigger event: [specific named event — e.g. "custodian insolvency"]
Depositor outcome at [$X implied position]: [$Y at risk / $Y recovered]
Recovery mechanism: [specific legal or operational process]
Time to recovery: [T+N or "indeterminate — no wind-down procedure confirmed"]
Evidence basis: [E if sourced / G2 if inferred from structure / G3 if unknown]

### Mandatory entries

Legal and Custody Risk:
  Trigger: custodian insolvency with no bankruptcy-remote structure confirmed.
  Populate from: F-LEG-003, F-LEG-004, F-CUS-001, F-CUS-002.
  If bankruptcy remoteness unconfirmed (G2): state full position at risk.

Credit and Collateral Risk:
  Trigger: largest single collateral asset falls 40% in 24 hours.
  Populate from: F-COL-001, F-COL-002, F-FIN-034, F-FIN-035.
  State: LTV at stress price, liquidation triggered Y/N, bad debt outcome.

Market and Oracle Risk:
  Trigger: oracle reports stale price for 4+ hours during market stress.
  Populate from: F-ORC-001, F-ORC-004, F-ORC-005.
  State: maximum mispricing possible, who can correct, time to correction.

Liquidity and Exit Risk:
  Trigger: 30% TVL redemption in 48 hours with one counterparty unavailable.
  Populate from: F-FIN-040, F-FIN-043, F-FIN-044, redemption waterfall skill.
  State: queue position, time to exit, price impact at implied position size.

Operational and Governance Risk:
  Trigger: key person unavailable + governance attack simultaneously.
  Populate from: F-OPS-001, F-OPS-002, F-ENT-060, F-ENT-061.
  State: protocol continues or halts, recovery time, who has emergency access.

Smart Contract Risk:
  Trigger: exploit draining X% of TVL.
  Populate from: F-SEC-006, F-SEC-007, F-RIS-001, F-RIS-002.
  State: insurance coverage vs TVL ratio, time to depositor recovery,
  whether the Resolv privileged minting check passed.

### Hard rule

If a loss scenario cannot be populated because the evidence is G2 or G3:
state explicitly: "Loss outcome indeterminate. Evidence required: [action]."
Do not estimate. Do not omit the row. Indeterminate is the finding.
