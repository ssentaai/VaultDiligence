---
name: source-add
description: |
  Evaluate a candidate external data source and decide whether to register
  it in knowledge/external-sources/, reject it with a documented reason,
  or pend it for further research. Walks the operator through tier
  classification, coverage assessment, failure-mode analysis, and the
  registration mechanics. Never adds a source to the registry without
  passing the schema validator and updating the cross-references.
triggers:
  - new data source
  - new source
  - register source
  - add to source registry
  - source not in registry
  - new feed
  - new oracle
  - new dashboard
  - issuer dashboard
  - reserve adapter
  - subgraph
  - what tier is this source
  - is this FORMAL
  - is this EXPERT
constraints:
  - Never register a source as ON-CHAIN that is not a direct RPC read
    or verified contract method. Aggregators are FORMAL, not ON-CHAIN.
  - Never register a source as FORMAL without a published methodology
    OR an attributable maintainer producing records of record.
    Twitter, Substack, Discord, unsigned blogs are INFORMAL by default.
  - Never register a source without specifying covers_field_ids.
    A source that does not support evidence on any field does not
    earn its place in the registry.
  - Never claim ON-CHAIN tier on a source that an aggregator wraps.
    DefiLlama is FORMAL even though it aggregates ON-CHAIN data.
    Etherscan API is FORMAL; a direct Alchemy RPC read is ON-CHAIN.
  - Never skip the schema validator. A source that fails
    scripts/validate-sources.py does not get committed.
  - Never skip the cross-reference work. Settings.json allow-list,
    field annotations, and disambiguation spec must be updated in the
    same commit as the new entry, not deferred.
---

# Source-Add Skill

When you encounter a data source not yet in `knowledge/external-sources/`, this skill is the protocol for deciding what to do with it. The answer is one of:

1. **Register** — write a full entry, update cross-references, validate, commit.
2. **Reject** — write a one-line entry in `_rejected.md` explaining why this source does not earn registration, so the question is closed.
3. **Pend** — write a stub in `_pending.md` with the unresolved questions, so the operator can return to it.

The default is **reject or pend**, not register. Most candidate sources do not earn registry inclusion. Adding noise to the registry harms the agents that read from it.

## When to invoke this skill

The skill triggers when:

- An agent is about to cite a source not in `knowledge/external-sources/_index.md`
- The operator hands the agent a URL or API endpoint and asks "should we use this"
- A pack run discovers a new issuer dashboard, reserve adapter, oracle feed, or aggregator
- A field-registry cross-walk (Fix 67) surfaces a field with no covering source

The skill does NOT trigger for:

- Citing an INFORMAL source within a single pack (those don't get individual entries; they cite the generic `informal-substack` / `informal-twitter` / `informal-discord` registry entries)
- Querying a source already in the registry (just read the entry and proceed)
- Generic web research that doesn't involve citing a source as evidence (browsing for context vs. citing for evidence are different jobs)

## Step 1 — Identify the source

Before tier classification, get the basic facts. The agent answers each of these or marks them as unresolved:

| Question | Where to look |
|---|---|
| What is the source's canonical name? | The provider's site, not your inference |
| Who maintains it? Named individual, named firm, anonymous? | About page, footer, GitHub maintainer list |
| What is the canonical URL base? | The endpoint root, not a specific resource |
| Is documentation published? Where? | Look for `/docs/`, `/methodology/`, README, OpenAPI spec |
| What does it actually return? Data, opinions, both? | A few sample requests answer this |
| Is the data reproducible — can you query the same input later and get the same answer (modulo refresh)? | Test by querying twice |
| Authentication required? Rate-limited? | API docs |
| What's the update cadence? | Docs or empirical observation |

If any of "name / maintainer / canonical URL / what it returns" is unresolved, **do not proceed to Step 2**. Return to research. A source you can't identify cannot be registered.

## Step 2 — Classify the tier

The source-tier classification is the most consequential decision. Follow these rules in order; the first rule that applies decides the tier.

### Rule 1 — ON-CHAIN

A source is ON-CHAIN if and only if **all** of the following are true:

- The data is computed deterministically from blockchain state
- Access is via direct RPC, public client read, or a verified contract method
- The reader's compute is the source of truth, not a remote service

**Examples that ARE ON-CHAIN:**
- Direct Alchemy RPC: `eth_call` to a verified contract's `totalSupply()`
- Curve pool's `get_dy()` read
- A protocol's redemption rate function (e.g. `cUSD.getBurnAmount()`)
- The Graph subgraph reads ARE NOT ON-CHAIN — they are FORMAL, because The Graph runs computation off-chain on indexed events. ON-CHAIN means *you* run the read against chain state.

**Examples that ARE NOT ON-CHAIN:**
- Etherscan API responses → FORMAL (Etherscan can be wrong; on-chain reads cannot)
- DefiLlama TVL queries → FORMAL (aggregation involves methodology choices)
- Pyth, Chainlink, RedStone oracle feeds → FORMAL (oracles publish methodology and operator sets; reading the feed is reading a published feed, not reading on-chain state directly)

A source that an aggregator wraps is FORMAL, not ON-CHAIN, even if the underlying data ultimately came from chain state. The aggregation is the methodology.

### Rule 2 — FORMAL

A source is FORMAL if it satisfies **at least two** of the following:

- Publishes versioned methodology documentation (e.g. Pharos's per-system version numbers)
- Has an attributable maintainer (named firm, named regulator, or named individual with a stable identity)
- Produces records of record (regulatory filings, signed audit reports, regulator-affiliated registries)
- Open source with a stable maintainer community

If only one of these is true, fall through to EXPERT or INFORMAL.

**Examples:**
- DefiLlama → FORMAL (open methodology, named maintainers, open source)
- Pharos Watch → FORMAL (versioned methodology, named maintainer, open source, no commercial conflict)
- GLEIF → FORMAL (regulator-affiliated, records of record)
- SEC EDGAR → FORMAL (regulator, records of record)
- OpenZeppelin published audit report → FORMAL (named firm, signed report, records of record)
- Issuer dashboard publishing live reserves with documented methodology (Tether, Circle, a synthetic-dollar issuer, etc.) → FORMAL
- Etherscan API → FORMAL (named firm, well-documented endpoints, but data ultimately requires on-chain corroboration for the claims that matter)

### Rule 3 — EXPERT

A source is EXPERT if it is a named individual or firm with domain reputation, **and** it produces opinion or analysis rather than records of record.

**Examples:**
- Gauntlet's risk parameter recommendations
- Chaos Labs published analyses
- Steakhouse's curator posts on Morpho's forum (when authored by named curators)
- Bluechip ratings
- A named DeFi researcher's analysis on Substack, IF the researcher has domain reputation. Anonymous Substack stays INFORMAL.

EXPERT sources can support state=E only when the field they support is itself opinion-shaped (e.g. risk parameter recommendations). For factual claims, EXPERT downgrades to E(P).

### Rule 4 — INFORMAL

Everything else. Forum posts, anonymous Twitter, Discord, unsigned blogs, podcast transcripts, screenshots without attribution.

INFORMAL sources cannot support state=E for any field. They downgrade to E(P) at best.

A handy disambiguation: **if you're not sure whether a source is FORMAL or INFORMAL, it is INFORMAL.** The bias is toward not promoting; promotion of an INFORMAL source to FORMAL is a real diligence error.

## Step 3 — Assess coverage

What fields can this source support evidence for?

Start from the field-registry side, not the source side. For each field this source might cover:

1. Read the field definition in `knowledge/data-model/fields/<F-XXX-NNN>.md`
2. Ask: "Does this source's output answer the field's question?"
3. Ask: "At what state ceiling? (E / E(P) / G2 / G3)"

A source typically covers a small number of fields well, not many fields adequately. List them honestly:

```
covers_field_ids:
  - F-FIN-018           # primary; live data, FORMAL tier, E ceiling
  - F-COL-014           # secondary; cited but only as corroboration
```

If you can't list at least one field, **do not register**. A source that doesn't help any field doesn't belong in the registry.

## Step 4 — Identify failure modes and fallbacks

Every registered source must answer: **what happens when this source is down?**

- Is there another registered source that covers the same fields? List them as `fallback_sources`.
- Is there NO fallback? Document this explicitly. The covered fields become at-risk fields when this source goes down — a real diligence concern that the registry should make visible.

Single-source fields are not disqualifying, but they need to be visible. The Fix 70 source registry's `--check-coverage` mode (when it exists) reports them.

Failure modes to think about:

- API down (rate limit, 5xx, no response)
- Source-side methodology change (Pharos has changelog; not all sources do)
- Source-side data quality regression (silent regression)
- Maintainer abandonment (e.g. a sunset issuer dashboard)
- Authentication change (API key requirement added)

## Step 5 — Make the decision

Three options:

### Decision A — Register

Pre-conditions:
- Step 1 fully resolved
- Tier classification clear and defensible per the rules in Step 2
- At least one covered field identified
- Fallback (or explicit no-fallback note) documented

Action:
1. Copy `spec/external-sources-schema.md`'s template to `knowledge/external-sources/<slug>.md`
2. Fill in YAML frontmatter completely
3. Write body sections per schema (What this source provides / Source tier rationale / When to use it / When NOT to use it / Authentication and rate limits / Cross-references / Notes)
4. If accessed via curl, add the URL pattern to `.claude/settings.json` permissions allow-list
5. For each covered field in `knowledge/data-model/fields/<F-XXX>.md`, add this source to that field's source list (annotation work — the field definitions need a sources section if they don't have one)
6. Run `python3 scripts/validate-sources.py` (when Fix 70 is built)
7. Run `python3 scripts/validate-sources.py --rebuild-index` to update `_index.md`
8. Commit with message format: `sources: register <slug> as <tier>`

### Decision B — Reject

When: source fails to meet tier-classification rules, or covers no fields, or duplicates an existing entry without adding distinct value.

Action:
1. Append a one-line entry to `knowledge/external-sources/_rejected.md`:

   ```
   - <slug-or-url> | <date> | rejected: <one-sentence reason>
   ```

2. Commit. The rejection log is the institutional memory: it stops the same source from being re-evaluated repeatedly.

Common reject reasons:
- "INFORMAL only, covers no field that needs INFORMAL ceiling evidence"
- "Aggregator-of-aggregators, lower authority than DefiLlama which we already use"
- "Maintainer abandoned, last update 2 years ago"
- "Methodology not published, source-tier unverifiable"
- "Same coverage as existing source X, no fallback value"

### Decision C — Pend

When: research is incomplete (Step 1 unresolved questions remain), or the source is interesting but you cannot yet decide tier or coverage.

Action:
1. Append an entry to `knowledge/external-sources/_pending.md`:

   ```
   ## <slug-candidate>
   URL: <url>
   First-seen: <date>
   Open questions:
   - <unresolved question 1>
   - <unresolved question 2>
   Decision deadline: <date or "no deadline">
   ```

2. Commit. The pending log is short by design — items here either get registered, rejected, or removed when stale (>90 days without progress).

## Step 6 — After registration

The registry entry is not the end. After a new FORMAL or ON-CHAIN source is registered:

1. Check if the new source enables any field that was previously G2 or G3 due to lack of source coverage. If so, those fields should be revisited in active packs.
2. Check if the new source is a fallback for any other registered source that previously had no fallback. Update those entries' `fallback_sources`.
3. Check if Fix 67's cross-walk (when complete) flagged this field area as a gap. Update the cross-walk doc to reflect the now-covered field.

These three checks take a few minutes and prevent the registry from becoming stale relative to the field registry.

## Common patterns

### "It's a new issuer's reserve dashboard"

Most likely FORMAL, IF the dashboard publishes documented methodology and is operated by the named issuer or a known service provider on the issuer's behalf. Examples in the registry: issuer-reserve-feed, circle-reserve-attestation, tether-transparency.

If the dashboard is operated by an anonymous third party or has no methodology documentation, downgrade to EXPERT or INFORMAL.

### "It's a new oracle feed"

FORMAL if it has documented methodology and a named operator set (Pyth, Chainlink, RedStone all qualify). The feed itself is the source; the on-chain price reads from that feed are still FORMAL (the oracle's methodology is the source of truth, not the chain state).

### "It's a new aggregator competing with DefiLlama"

Probably reject unless it covers fields DefiLlama does not. The registry already has DefiLlama; adding a redundant aggregator harms the disambiguation rules without adding coverage.

### "It's a Substack newsletter from a named DeFi researcher"

EXPERT if the researcher has domain reputation. INFORMAL if anonymous or new. Either way, this source's evidence ceiling is E(P), not E. Most analysis work doesn't need a registry entry — cite the generic `informal-substack` or `expert-named-individual` category.

### "It's a Twitter thread that claims to have the right number"

INFORMAL. Cite the generic `informal-twitter` category. Don't register individual Twitter accounts.

### "It's a regulator filing or registry"

FORMAL with high confidence. Examples: SEC EDGAR, GLEIF, OpenCorporates. Records of record by definition.

### "It's a smart contract function that returns data"

ON-CHAIN if it's a verified contract and the function is called via direct RPC. Examples: protocol redemption functions, getter views on verified contracts. Register the contract+function pair, not just the contract.

## Cross-references

- `spec/external-sources-schema.md` — the registry schema this skill registers entries against
- `spec/evidence-disambiguation.md` — the source-tier ordering this skill enforces
- `.claude/settings.json` — the permissions allow-list that registered sources update
- `knowledge/data-model/fields/` — the field definitions that registered sources cite back to
- `knowledge/external-sources/_index.md` — the auto-generated index regenerated after each registration
- `knowledge/external-sources/_rejected.md` — the institutional memory of rejected candidates
- `knowledge/external-sources/_pending.md` — the queue of sources awaiting research
- `scripts/validate-sources.py` (created in Fix 70) — schema enforcement
- `.claude/skills/tool-recovery/SKILL.md` — failure-mode policy that the `fallback_sources` field feeds

## What this skill is NOT

- Not a source-discovery tool. The skill processes candidates the operator or agent has already encountered. Discovery is upstream.
- Not a recommendation engine. The skill does not rank registered sources beyond tier classification. The disambiguation rules in `spec/evidence-disambiguation.md` handle ordering.
- Not for INFORMAL sources cited in single packs. INFORMAL sources cite generic registry categories. Don't add a registry entry for every Twitter post.
- Not a real-time monitoring system. The registry catalogs source identity; freshness is per-evidence at query time.
- Not blocked on Fix 70. This skill can be used today against the schema in `spec/external-sources-schema.md` even before the validator script exists. The schema is authoritative; the validator is convenience.
