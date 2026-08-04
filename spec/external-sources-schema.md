# External Sources Registry Schema

## Purpose

A canonical registry of every external data source VaultDiligence agents can cite as evidence. Used by:
- A1 (on-chain evidence) and A2 (document/counterparty) when choosing which source to query for a given field
- A3 (synthesis) when assessing source-tier authority during disambiguation
- A6 (verification) when checking whether a cited source matches an authoritative source for the claim
- Plan-mode preambles when seeding `findings-live.md` triggers based on which sources are reachable for a given vault type
- The disambiguation rules in `spec/evidence-disambiguation.md` (which already reference ON-CHAIN > FORMAL > EXPERT > INFORMAL but do not enumerate the actual sources)

## What problem it solves

Before this registry, the implicit list of sources VaultDiligence used lived in three places:
1. The `permissions.allow` list in `.claude/settings.json` (covered ~11 endpoints, focused on bash curl)
2. Agent prompts (which mention specific sources inline without a canonical reference)
3. The `tool-recovery` skill (which documents failure shapes but not source identity)

That fragmentation meant: agents would sometimes cite a source the operator hadn't realized was in scope, source-tier classifications were inconsistent across packs, and adding a new source required hunting through three files.

The registry centralizes this. One file per source. Every agent reads from it. New sources get added in one place.

## Location

`knowledge/external-sources/_index.md` — registry listing, one row per source
`knowledge/external-sources/<slug>.md` — one structured entry per source

Slug format: `<provider>-<purpose>` for clarity, e.g. `etherscan-evm-explorer`, `defillama-tvl`, `pharos-stablecoin-grades`. Keep slugs lowercase, hyphenated, and stable across schema versions.

## Entry schema

YAML frontmatter + structured body. All required fields must be present; missing fields fail validation.

### Frontmatter (required)

```yaml
---
schema_version: 1
id: defillama-tvl
name: DefiLlama TVL API
provider: DefiLlama
url_base: https://api.llama.fi
docs_url: https://api-docs.defillama.com/
source_tier: FORMAL                    # ON-CHAIN | FORMAL | EXPERT | INFORMAL
purpose:                                # what this source is for, in one phrase
  - tvl
  - protocol-metadata
  - yield-aggregation
auth: none                              # none | api-key | rate-limited-anonymous | oauth | other | unknown
access_mode: fetch                      # fetch | pointer-gated | pointer-paid
freshness_typical: hourly               # realtime | sub-minute | minute | hourly | daily | weekly | static
freshness_max_trusted: 4h               # max age before evidence based on this source becomes E(P)
covers_chains:                          # which chains the source covers; ALL if chain-agnostic
  - ALL
covers_field_ids:                       # which VaultDiligence field IDs this source can support evidence for
  - F-FIN-001
  - F-FIN-002
  - F-FIN-010
fallback_sources:                       # other source slugs that cover the same fields if this one is down
  - etherscan-evm-explorer
  - direct-rpc-read
status: active                          # active | deprecated | candidate | blocked
added_in: v45                           # VaultDiligence version this source was added/registered
notes_url:                              # optional pointer to a longer notes doc
---
```

### access_mode (required, enum-checked; defaults to `fetch` if absent)

Distinguishes "VaultDiligence verifies this" from "available here — analyst's action". This is
orthogonal to `auth` (which is the credential *type*); `access_mode` is *who does the retrieving*.

- `fetch` — VaultDiligence retrieves it directly (free API / anonymous web / direct RPC).
- `pointer-gated` — exists and is free to read in-browser, but blocks programmatic/anonymous
  fetch (the analyst opens it). Includes sources needing a declared User-Agent, a free key,
  or that are JS-rendered / rate-limited.
- `pointer-paid` — behind a paid subscription; the analyst obtains it under their own access
  or via the DDQ (e.g. NRSRO credit ratings).

Enum-checked when present. Absent is treated as `fetch` (default) so pre-existing entries do
not break. The renderer uses this to label a source "verified by us" vs "available, your action".

### Body (required sections)

```markdown
## What this source provides

Two to four sentences. Mechanical description of the data shape — what
endpoints, what fields, what update cadence. No interpretation.

## Source tier rationale

One paragraph explaining WHY this source has the assigned tier. The
classification is not arbitrary — it should follow from the source's
operational structure. ON-CHAIN means the data is computed deterministically
from blockchain state. FORMAL means the source publishes versioned
methodology, has an attributable maintainer, and produces records of
record. EXPERT means a named individual or firm with domain reputation.
INFORMAL is everything else — forum posts, Twitter, Substack, unsigned blogs.

A source that *aggregates* on-chain data (e.g. DefiLlama, Etherscan APIs)
is generally FORMAL, not ON-CHAIN, because the aggregation introduces
methodology choices. ON-CHAIN tier is reserved for direct RPC reads and
verified contract data.

## When to use it

The fields it's authoritative for, the freshness window inside which it
should be preferred, and any vault types where it should be the default.

## When NOT to use it

The fields it should NOT be cited for (even if it surfaces them
incidentally), known data quality issues, and vault types where it's
unreliable. Document the failure modes the agents should recognize.

## Authentication and rate limits

How to access. If an API key is required, document where the operator
sets it (env var, settings.json key, etc.). If anonymous use is
rate-limited, document the limit and what happens when it's hit (per
the tool-recovery skill).

## Cross-references

Other source registry entries that interact with this one (fallbacks,
overlapping coverage, alternative tiers). Links to spec docs that
reference this source.

## Notes

Free-form. Source-confidence caveats, known data quality issues,
historical incidents involving this source's reliability, anything
that doesn't fit above.
```

## What every entry MUST do

1. Have a non-empty `covers_field_ids` list. A source that doesn't support evidence on any field doesn't earn its place in the registry.
2. Specify `source_tier` exactly once from the controlled vocabulary {ON-CHAIN, FORMAL, EXPERT, INFORMAL}.
3. Specify `freshness_max_trusted` as a duration string. After that age, evidence citing this source must downgrade to E(P).
4. Specify at least one `fallback_sources` entry, OR explicitly state in the body that no fallback exists (in which case the field IDs covered are at risk of becoming uncovered if this source goes down — a real diligence concern that should be visible).

## What every entry MUST NOT do

1. Speculate about source intent or commercial positioning. The registry is operational, not editorial.
2. Recommend or rank sources beyond the source-tier classification. Tier is the only ranking; finer comparisons are out of scope.
3. Reproduce extensive content from the source's documentation. Cite, don't quote.

## How sources get classified into tiers

The source_tier classification is not negotiable per-pack. It's set in the registry and used consistently by every agent and every disambiguation pass. The rules:

- **ON-CHAIN** — data is computed deterministically from blockchain state via direct RPC, public client read, or verified contract method. Examples: an Alchemy `eth_call` to a verified contract's `totalSupply()`, a Curve pool's `get_dy()` read. NOT Etherscan's API responses (those are FORMAL — Etherscan can be wrong, on-chain reads cannot).

- **FORMAL** — source publishes versioned methodology, has an attributable maintainer, produces records of record. Examples: DefiLlama (open-source methodology, named maintainers), Pharos Watch (versioned scoring docs), GLEIF (regulator-affiliated entity registry), SEC EDGAR (regulatory filings), Pyth Network and Chainlink (versioned oracle feeds with documented operator sets).

- **EXPERT** — named individual or firm with domain reputation, even when the output is opinion. Examples: a Gauntlet risk parameter recommendation, a Steakhouse curator post on Morpho's forum, a published Bluechip rating.

- **INFORMAL** — everything else. Forum posts, Substack newsletters, unsigned blog posts, Twitter, Discord, podcast transcripts. INFORMAL sources cannot support state=E; they downgrade to E(P) at best.

A source can be *cited* at any tier, but the tier follows the source, not the citation context. If an agent cites a Substack article, that's INFORMAL whether the article is correct or not.

## How sources get added to the registry

Manually, by the human operator, when a real diligence need surfaces a source not yet registered. The dream cycle does not write to this directory. Agents do not write to this directory. Adding a source is a versioned change to VaultDiligence's framework.

When a new source is added:
1. Write the entry under `knowledge/external-sources/<slug>.md`.
2. If the source is accessed via curl, add the appropriate URL pattern to `.claude/settings.json` permissions.
3. Run `scripts/validate-sources.py` (to be built) to enforce schema and rebuild `_index.md`.
4. Cross-reference: update any field definition in `knowledge/data-model/fields/` that lists the new source as supporting evidence.
5. Document in CHANGELOG-vXX.md as part of the version that introduced it.

## Versioning

Entries written under v45's schema are tagged `schema_version: 1` in frontmatter. If the schema evolves, increment the version and document migration rules. Old entries are not silently re-interpreted.

## Index format

`knowledge/external-sources/_index.md` is one row per source, grouped by `source_tier` (ON-CHAIN first, then FORMAL, then EXPERT, then INFORMAL), then alphabetically within tier:

```markdown
# External Sources Registry

## ON-CHAIN

| Slug | Name | Purpose | Covers chains |
|------|------|---------|---------------|
| direct-rpc-read | Direct EVM RPC | on-chain state reads | EVM chains |

## FORMAL

| Slug | Name | Purpose | Covers chains |
|------|------|---------|---------------|
| defillama-tvl | DefiLlama TVL | TVL, protocol metadata | ALL |
| etherscan-evm-explorer | Etherscan family | block explorer | EVM chains |
| ...
```

The index is regenerated by `scripts/validate-sources.py --rebuild-index`, not edited by hand.

## Cross-references

- `spec/evidence-object-schema.md` — the evidence object format that cites these sources via `source_uri` and `source_type`
- `spec/evidence-disambiguation.md` — the v42 ON-CHAIN > FORMAL > EXPERT > INFORMAL ordering this registry enumerates concretely
- `.claude/settings.json` — the bash curl allow-list that must include any source accessed via curl
- `.claude/skills/tool-recovery/SKILL.md` — the failure-shape policy that uses `fallback_sources`
- `knowledge/incidents/` — historical incidents that involve specific sources (e.g. an oracle feed misbehaving) cross-reference back here
