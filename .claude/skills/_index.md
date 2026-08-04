# Skills Registry

Read this file for skill discovery. Load full SKILL.md only when trigger matches.
This file stays short. The full skill files load progressively.

---

## pdf-extraction
Extracts structured fields from PDF documents.
Triggers: audit report, legal opinion, fund prospectus, SOC-2, subscription agreement, PDF
Constraints: page-cite every claim, never summarise without citing page number

## contract-reading
Reads smart contract ABI to enumerate privileged roles and upgrade mechanisms.
Triggers: contract, ABI, privileged roles, timelock, oracle address, Etherscan, upgrade mechanism
Constraints: G2 if unverified, never decompile unverified bytecode

## redemption-waterfall-mapping
Maps every counterparty in a redemption stack with individual T+N.
Triggers: redemption, waterfall, T+N, exit, queue, counterparty stack, VT-3, VT-3a, VT-7, VT-8
Constraints: every counterparty must be named, G2 if any step timeline is unstated

## comparables-table
Builds factual side-by-side comparables table with TradFi anchor.
Triggers: comparables, comparable vaults, peers, alternatives, side-by-side, TradFi equivalent
Constraints: no judgment column, no advantage assessment, every cell sourced and dated

## tool-recovery
How to handle tool failures (timeout, empty response, rate-limit, schema mismatch, persistent error) without inventing data.
Triggers: web_fetch timeout, web_fetch empty, JS-rendered, rate limited, 429, 503, tool failed, Scrapling fallback, retry

## ingest-source
Seven-phase methodology for ingesting external source material (research, methodology documents, market commentary, incident post-mortems) and deciding ship/defer/reject. Bias toward defer. Ingestion-rate gate at 5 unvalidated ingestions.
Triggers: ingest source, new methodology document, new research paper, new article, new framework, market commentary, incident post-mortem, industry standards, check against framework, what can we learn from this, does this change vaultdiligence, rating methodology, operator-side commentary
Constraints: registry audit mandatory before estimating effort, four-dimension impact assessment mandatory, ingestion-rate gate enforced, immediate-ship requires all six criteria met
Constraints: never invent a value to fill a gap (G2/G3 only, never E), never silently retry (every retry logged), 15-retry budget per session

## source-add
Workflow for evaluating a candidate external data source — tier classification, coverage assessment, failure-mode analysis — and deciding whether to register, reject, or pend. Default is reject or pend, not register.
Triggers: new data source, new source, register source, add to source registry, source not in registry, new feed, new oracle, new dashboard, issuer dashboard, reserve adapter, subgraph, what tier is this source, is this FORMAL, is this EXPERT
Constraints: never register ON-CHAIN for a source that aggregates rather than reads chain state directly, never register FORMAL without published methodology or attributable maintainer, never skip schema validation, never skip cross-reference work
