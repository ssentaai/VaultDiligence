# F-SEC-017

**Field ID**: F-SEC-017
**Category**: Security
**Sub-Category**: Infrastructure
**Field Name**: Frontend / API / RPC Endpoint Hardening
**What to Collect / Question to Answer**: What protections are in place for the operator's user-facing frontends, APIs, and RPC endpoints — specifically a web application firewall (WAF), CDN fronting, and request rate limiting?
**Data Type**: Text (control checklist)
**Vault Types**: ALL
**Collection Tier**: T3
**Pillar(s)**: P7
**Primary Source**: Operator infrastructure security documentation / DDQ response
**Fallback Source**: Inspection of response headers and CDN/WAF fingerprints on the public frontend and API endpoints, plus operator confirmation of rate-limiting configuration
**Evidence Pathway**: Inspection-validatable: inspect HTTP response headers and edge fingerprints on the public frontend and API/RPC endpoints to detect a CDN/WAF, then obtain operator confirmation of rate-limiting thresholds and coverage.
**Institutional Standard**: User-facing frontends, APIs, and RPC endpoints sit behind a web application firewall and a CDN, with request rate limiting applied, so the hosted mint/redeem and data surface resists takeover, injection, and denial-of-service without depending on the contract layer for protection.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the operator's frontend/API/RPC protection posture: confirm WAF presence and vendor, CDN provider, and rate-limiting configuration and coverage. Where any control is absent or unconfirmed, classify as a gap (G2) and name the operator's infrastructure owner as the entity that must produce evidence.
**Source / Precedent**: Steakhouse Financial stablecoin-issuer DDQ v1.0, §2.19: 'What protections are in place for frontends, APIs, and RPC endpoints? WAF? CDN? Rate limiting?' Same web2 attack-surface family as the Curve and BadgerDAO frontend hijacks, which compromised the hosted UI rather than the contracts.
**Criterion ID(s)**: 7.16
