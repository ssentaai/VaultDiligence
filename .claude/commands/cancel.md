---
name: cancel
description: Halt an in-progress investigation cleanly. Marks the pack
  as INCOMPLETE. Preserves all completed work and scratchpad logs.
  No side-effect chain continues after this command runs.
---

# /cancel — Clean Investigation Halt

## When to Use

Investigation produced unexpected results and needs to be restarted.
Step limit exceeded and investigation is incomplete.
Wrong vault address was used.
Agent is behaving unexpectedly and needs to be stopped.

## What Happens

1. Stop all pending tool calls immediately.

2. Write to packs/{vault-slug}/progress.md:
   ```
   STATUS: INCOMPLETE — CANCELLED
   Cancelled at: [timestamp]
   Reason: [state the reason if known, or "manual cancel"]
   Last completed step: [last checkmark from todo.md]
   Steps not completed: [remaining unchecked items]
   ```

3. Write CANCELLED to the structured-output stub if it exists.
   Set status: "INCOMPLETE".

4. Rename active scratchpad file:
   packs/{vault-slug}/.scratchpad/{date}_{hash}.jsonl
   → packs/{vault-slug}/.scratchpad/{date}_{hash}_CANCELLED.jsonl

5. Append one row to log.md:
   | [date] | {vault-slug} | CANCEL | Investigation cancelled. [last step]. | Restart with /d1 or /full-dd |

6. Output:
   "Investigation cancelled.
   Pack status: INCOMPLETE.
   Completed work preserved in packs/{vault-slug}/progress.md
   Scratchpad preserved in packs/{vault-slug}/.scratchpad/
   To restart: /d1 or /full-dd with force_fresh=true"

## What Does NOT Happen

Files are not deleted.
Scratchpad logs are not destroyed.
Partially confirmed fields are not removed.
The vault folder is preserved for inspection and restart.

## Restarting After Cancel

Run /d1 or /full-dd again.
The agent reads progress.md and resumes from the last confirmed step.
Fields already confirmed E do not need to be re-queried.
