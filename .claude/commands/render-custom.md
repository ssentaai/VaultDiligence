---
name: render-custom
description: Render the investigation evidence into a user-supplied template
  format (DDQ, board pack, governance proposal, reporting template).
  Runs after standard D1-D5 outputs are complete.
  Uses the same evidence object. Does not re-investigate.
---

# /render-custom — Custom Template Output

## Purpose

The allocator has an existing format their IC, board, or governance
process expects. Produce VaultDiligence evidence mapped to that format.

This is an additional render only. It does not change what was investigated,
how evidence is classified, or what the standard outputs contain.

## Input

packs/{vault-slug}/custom-template/input.{ext}
  The user-supplied template. Accepted formats:
  - PDF (questionnaire or form)
  - DOCX (reporting template)
  - XLSX (structured DDQ)
  - MD (markdown template)
  - Plain text (field list)

packs/{vault-slug}/agent-outputs/evidence-register.json
  The completed evidence object from the investigation.

## Process

Step 1: Read the custom template.
  Identify every required field or question.
  Map each to the closest field in the evidence register.
  Where a direct mapping exists: use the confirmed value and state.
  Where no mapping exists: note as "Not covered by VaultDiligence investigation"
  or classify as G2/G3 if it is a gap we identified.

Step 2: Build the mapping table.
  | Template Field | Evidence Field | Value | State | Source |
  For every field in the template. No blanks.

Step 3: Render the output.
  Produce a completed version of the template using evidence register values.
  Preserve the template's structure, section headings, and field labels.
  Add VaultDiligence evidence metadata (state, source URI, retrieved_at)
  as footnotes or an appendix — do not embed them in the main fields
  unless the template has a source column.

Step 4: Flag gaps explicitly.
  Any template field that cannot be answered from the evidence register:
  - State clearly: "Not confirmed in VaultDiligence investigation"
  - Classify: G2 (exists but restricted) or G3 (does not exist)
  - Add to the gap register if not already present
  Do not leave blank. Do not invent values.

Step 5: Save output.
  packs/{vault-slug}/custom-template/output.{ext}
  packs/{vault-slug}/custom-template/mapping-table.md

## Named Templates

The following named templates can be referenced directly:

  DAO-RFP-DDQ-v1 — Standard DAO treasury RFP questionnaire.
    Used when subscriber is responding to a DAO treasury allocation process.
    Located: the source research
    Maps: evidence register fields → standard RFP section structure.
    Invoke: /render-custom --template DAO-RFP-DDQ-v1

## What This Is Not

Not a re-investigation. If the template asks for something not in the
evidence register and not classifiable as a known gap: note it as
"Outside VaultDiligence investigation scope" and recommend the user
add it to a future investigation brief.

Not a replacement for the standard outputs. D1-D5 are always produced.
This is additive.

Not an endorsement of the template's framing. If the template asks for
a risk score or rating: respond with "VaultDiligence does not produce scores
or ratings. The evidence relevant to this question is: [evidence field]."

## Output Location

packs/{vault-slug}/custom-template/
  input.{ext}           — user-supplied template (original)
  output.{ext}          — completed template with evidence values
  mapping-table.md      — field-by-field mapping with evidence states
