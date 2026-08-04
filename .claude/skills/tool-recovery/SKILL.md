---
name: tool-recovery
description: |
  How to handle tool failures (timeouts, rate limits, JS-rendered pages,
  empty responses) without inventing data. Centralises retry, backoff,
  and fallback logic so every agent handles failures the same way.
triggers:
  - web_fetch timeout
  - web_fetch empty
  - JS-rendered
  - rate limited
  - 429
  - 503
  - tool failed
  - tool error
  - Scrapling fallback
  - retry
constraints:
  - Never invent a value to fill a gap. A failed tool produces G2 or G3, never E.
  - Never silently retry. Every retry is logged in scratchpad with reason.
  - Hard-fail after the policy's retry budget is exhausted. Do not loop forever.
---

# Tool Recovery Policy

When a tool call fails, the right response is rarely "try again immediately." It is one of: retry with backoff, fall back to a different tool, or hard-fail and write G2/G3 with a specific gap action. Without a policy, every agent improvises and the failure modes diverge across packs.

This skill defines the policy. Agents follow it exactly. Anything that does not fit the policy is a `findings-live.md` trigger to the human, not silent improvisation.

## Failure taxonomy

There are five failure shapes. Each has a fixed response.

### 1. Timeout (no response within tool's timeout)

Examples: web_fetch hangs, an MCP returns nothing, an API doesn't respond.

Response:
1. Retry once with the same tool, same arguments.
2. If still timing out, try the documented fallback for that source class:
   - `web_fetch` → `Scrapling` for JS-rendered pages
   - DefiLlama API → DefiLlama static snapshot in `knowledge/snapshots/`
   - Etherscan → equivalent block explorer for the chain (Arbiscan, Polygonscan, etc.)
3. If fallback also fails: write the field as G2 with gap action "source unreachable, retry on T+1 or escalate to operator."

### 2. Empty response (200 OK but body is empty or skeletal)

Examples: web_fetch returns empty markdown, Scrapling returns the cookie banner only, an API returns `[]` for a query that should have content.

This is the most dangerous failure mode because it looks like success. The default behaviour of trusting a 200 OK is wrong here.

Response:
1. Detect: if the response is shorter than 200 chars, treat it as empty.
2. Try the documented fallback (same as Timeout step 2).
3. If fallback also returns empty: write the field as G2 with gap action "source returns no content for this query, may be JS-rendered or behind auth."

Never write G3 ("absent") on the basis of an empty response. Empty ≠ absent. Absent means you know it doesn't exist; empty means the tool didn't show it to you.

### 3. Rate-limited (429, 503, "rate limit exceeded" body)

Examples: Etherscan free tier hit, GLEIF API throttled, OpenCorporates daily limit reached.

Response:
1. First 429: wait 30s, retry once.
2. Second 429: wait 120s, retry once.
3. Third 429: stop calling that tool for the rest of the agent run. Write the field as G2 with gap action "rate-limited, retry in next session."
4. Log the rate-limit hit to the agent's scratchpad with timestamp so the dream cycle can surface tooling-pattern problems.

Do not switch to a different API key to bypass rate limits. The point of the policy is to surface tooling-cost patterns, not hide them.

### 4. Schema mismatch (response structure doesn't match expectation)

Examples: API response missing an expected field, JSON shape changed, contract returns a tuple where a single value was expected.

Response:
1. Do not retry. Schema mismatches are not transient.
2. Do not partially parse. A response that violates the expected schema may have other surprises.
3. Write the field as G2 with gap action "<API_NAME> response schema does not match expected format; verify the API contract."
4. Append a `findings-live.md` trigger to the human (or A3 if mid-pack): "Schema mismatch on <tool> for field <field_id> — verify the contract."

### 5. Persistent tool error (5xx, network failure, tool unavailable)

Examples: Scrapling crashes, an MCP server is offline, a CDN returns 502.

Response:
1. Retry once after 60s.
2. If still failing, mark the tool as unavailable for the rest of the agent run.
3. Write affected fields as G2 with gap action "tool <name> unavailable this session, retry in next session."
4. Append a `findings-live.md` trigger if more than 3 fields were affected.

## Retry budget

Across all failure types, an agent has a hard cap of **15 retries per session**. Beyond that, the agent stops attempting recovery and writes remaining fields as G2 with the appropriate gap action.

This cap exists because the worst failure mode is an agent that retries forever. The cap forces the agent to surface persistent problems to the human instead of burning tokens.

## What never happens

- Never invent a value because a tool failed. A failed tool produces G2 or G3, never E.
- Never silently retry. Every retry is logged in the agent's scratchpad with the failure reason. The dream cycle reads these logs to detect tooling pain patterns.
- Never switch fallback chains without documenting the substitution. If `web_fetch` fails and you fall back to `Scrapling`, the resulting evidence object's `reasoning` field must say so.
- Never assume a 200 OK means success. Empty content with 200 is a failure.

## Scratchpad logging

Every retry attempt and every fallback substitution must produce a scratchpad entry:

```json
{
  "timestamp": "2026-05-12T10:14:00Z",
  "skill": "tool-recovery",
  "action": "Scrapling fallback after web_fetch empty",
  "tool_used": "Scrapling",
  "tool_substituted_for": "web_fetch",
  "reason": "web_fetch returned 142 bytes for vault Gitbook URL",
  "outcome": "success" | "failure",
  "field_id": "F-CTR-008"
}
```

The dream cycle uses these entries to surface patterns: if `web_fetch → Scrapling` substitution happens 5+ times for Gitbook URLs across 3 packs, the staging queue surfaces a candidate lesson "Gitbook URLs need Scrapling, not web_fetch."

## Cross-references

- `spec/evidence-object-schema.md` — what gap action means; G2 vs G3 distinction
- `spec/findings-live-schema.md` — how to write a trigger when tool failure affects another agent
- `.claude/skills/_index.md` — register this skill for trigger matching
