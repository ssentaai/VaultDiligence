# Verdict Block Specification

**Status:** v51 spec, applies to D2 (executive summary) and D3 (full pack).
**Origin:** 2026-05-06 review of Pharos's pmUSD seven-tweet thread + verdict.
**Companion docs:** spec/d2-output-spec.md, spec/d5-and-defi-teardown-spec.md.

## Why this spec exists

VaultDiligence's existing D2 and D3 outputs are freeform prose. An institutional reader scanning multiple reports cannot easily compare findings or extract a structural verdict. The Pharos pmUSD thread demonstrated a different shape: numbered findings with specific structural claims, followed by a verdict that states the structural reality without grading or scoring.

This spec defines that shape for VaultDiligence reports. It composes with Fix 71 (D3 reading order) and Fix 72 (D2 header block) — those specs cover what goes above the verdict block; this spec covers the verdict block itself.

## Where the verdict block goes

In **D2** (executive summary): below the canonical header block (Fix 72), above any narrative discussion. The verdict block is the short-form summary an allocator reads when they only have 60 seconds.

In **D3** (full pack): below the field-by-field evidence section, above the provenance appendix. The verdict block in D3 is more detailed than D2's because the reader has read the underlying evidence.

In **D1** (initial allocability screen): NOT included. D1's job is to gate the full-dd, not to deliver findings. A D1 has a "next-step recommendation" (full-dd / waitlist / decline-coverage), not a verdict.

## Verdict block structure

Every verdict block has three sections, in order:

```
## Findings

1. [Finding statement — one sentence stating the structural reality]
   [One paragraph supporting the claim with cited fields]

2. [Finding statement]
   [Supporting paragraph]

...

## Open Questions

[Numbered list of structural questions the diligence could not resolve.
Each question references the specific evidence state (G2/G3/I) in the
underlying register that the question maps to.]

## Verdict

[2-4 sentence narrative stating the structural reality without grading.
NOT a recommendation. NOT a score. NOT a PASS/FAIL.
Frames the trade-off the allocator must evaluate.]
```

## Findings — rules

A finding is a structural claim about the vault that the evidence supports. Findings must:

1. **Be structural, not numerical.** "Yield is 7.2%" is not a finding. "Yield is concentrated 94% in cbBTC/USDC" is a finding.

2. **Be supported by at least one cited field at evidence state E or E(P).** The supporting paragraph must cite the field IDs that produce the finding. If the finding rests on G2/G3 evidence, it goes in Open Questions instead.

3. **Be falsifiable.** The reader should be able to check the finding against the underlying evidence and confirm or refute. "The protocol seems risky" is not falsifiable. "The protocol's redemption requires three contract burns followed by a vNFT claim" is.

4. **Avoid scoring language.** No "fails," "passes," "weak," "strong," "concerning," "adequate." State the structural reality. The reader concludes risk.

5. **Be ordered by severity-of-structure, not narrative flow.** The most load-bearing structural finding goes first. A finding about admin-key control of the entire collateral layer ranks above a finding about yield breakdown.

Number of findings: typically 3-8. Fewer than 3 suggests the diligence was thin or the vault is genuinely unremarkable. More than 8 suggests the findings need consolidation or the diligence is venting rather than reporting.

## Findings — formatting per finding

Each finding follows this exact pattern:

```
N. [One-sentence structural claim, no fluff, present tense.]

   [One paragraph (3-6 sentences) supporting the claim. Must:
   - Cite at least one F-XXX-NNN field ID
   - State the underlying mechanism, not just the surface fact
   - Distinguish what is on-chain from what is off-chain
   - Avoid editorial framing ("worryingly," "surprisingly," etc.)]
```

Worked example, modeled on Pharos pmUSD finding 4:

```
4. Redemption requires three sequential burns and produces a legal claim,
   not currency.

   Per F-LIQ-040 (redemption mechanism) and F-COL-006 (collateral chain),
   exiting pmUSD requires (a) burning pmUSD to release IONau, (b) burning
   IONau to claim a vNFT, and (c) holding a vNFT representing legal title
   to a Yukon mining claim. The vNFT is not redeemable for USD without
   secondary-market sale of the underlying mining claim. This is a
   structural property of the protocol, not a current operational
   constraint, and is documented at [source URL].
```

## Open Questions — rules

Open Questions are claims the evidence could not support to E. They are:

1. **Always tied to specific evidence states.** Each open question must reference the field(s) at G2/G3/I that produce the gap.

2. **Phrased as questions, not claims.** "Is the gold actually extractable at current cost?" not "The gold may not be extractable."

3. **Action-oriented when possible.** State what evidence would resolve the question. "An audit by a Big-4 firm assessing extraction economics would resolve this" is more useful than "this is unclear."

Number: 0-5. If a pack has zero open questions, the diligence either reached unusual completeness or is hiding gaps. Operator should examine before publishing.

## Verdict — rules

The verdict is a 2-4 sentence narrative that:

1. **States what the on-chain mechanics actually do**, separate from what the protocol claims.
2. **Identifies the structural trade-off** the allocator must evaluate.
3. **Does not recommend.** No "do not invest," "consider carefully," "appropriate for sophisticated allocators only."
4. **Does not score.** No grades, ratings, percentile placements, peer comparisons.

Worked example, modeled on Pharos pmUSD verdict:

> The on-chain mechanics are functional. The fork has precedent in production
> systems. The collateralization ratio against gold-claim valuation is high.
>
> The collateral, however, is unextracted gold controlled by a micro-cap
> issuer, verified by a small accounting firm, and redeemable only via legal
> claim to a mining concession. The structural trade-off is between the
> on-chain transparency of the issuance system and the off-chain opacity of
> the underlying physical asset.

This verdict states facts. It does not say "we recommend against this." It does not say "PASS" or "FAIL." It frames the structural reality such that a competent allocator can decide.

## What the verdict block is NOT

- **Not a score.** No A+/B/C/D/F grades. No 0-100 composites. No tier classifications.
- **Not a recommendation.** No "buy," "avoid," "consider," "appropriate for X."
- **Not a hedge.** No "this is risky but might be appropriate." Either state the structural reality or remove the sentence.
- **Not a hedge against legal risk.** VaultDiligence produces evidence; the allocator decides. Do not embed disclaimers in the verdict block — that's the report's terms-of-use, separate.
- **Not a chronological narrative.** "First we discovered X, then we noticed Y." The structure is severity-ordered findings + verdict, not investigation chronology.
- **Not a marketing summary.** Findings are not selling points. Verdicts are not pitch language.

## Tone calibration — anti-pattern examples

**WRONG:** "Worryingly, the collateral is held by a centralized custodian."
**RIGHT:** "The collateral is held by a single named custodian (F-CUS-003)."

**WRONG:** "The vault appears to have a strong yield profile."
**RIGHT:** "Yield is sourced 87% from organic protocol revenue (F-FIN-010, F-FIN-016)."

**WRONG:** "This vault is appropriate for allocators with appropriate risk appetite."
**RIGHT:** [No such sentence. The verdict block does not advise. Remove.]

**WRONG:** "Pass — meets all diligence criteria."
**RIGHT:** [No such sentence. VaultDiligence does not score. Remove.]

**WRONG:** "While the audit is from a smaller firm, the protocol's track record is reassuring."
**RIGHT:** "Audit was performed by Mac Accounting Group (F-SEC-012); not a Big-4 firm. Audit confirms collateral existence; does not confirm extractability economics."

## Cross-references

- `spec/d2-output-spec.md` — D2 envelope structure
- Fix 71 (D3 reading order) — what comes before the verdict block
- Fix 72 (D2 header block) — the structured header above the verdict
- The core rule — never score, rate, recommend, or produce a verdict
- Pharos pmUSD thread (May 2026) — model output style
- Merlin Egalite "Noncustodiality is not a philosophical question" — model for how control-risk findings should be framed

## How to migrate existing packs

Existing packs (none, pre-D1) do not need migration. The first D1 produced under v51 ships with a verdict block; older packs (none yet) would be tagged as pre-spec and exempted from the verdict-block requirement in `pack_status` (Fix 73, deferred).
