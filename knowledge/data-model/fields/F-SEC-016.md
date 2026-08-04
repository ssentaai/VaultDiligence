# F-SEC-016

**Field ID**: F-SEC-016
**Category**: Security
**Sub-Category**: Infrastructure
**Field Name**: DNS / Domain Security
**What to Collect / Question to Answer**: Are the operator's domain names protected by DNSSEC, registrar-level domain locking, and registrar account 2FA, and are DNS record changes actively monitored for unauthorised modification?
**Data Type**: Text (control checklist)
**Vault Types**: ALL
**Collection Tier**: T3
**Pillar(s)**: P7
**Primary Source**: Operator security documentation / infrastructure security questionnaire response
**Fallback Source**: Public DNS inspection of the operator domain (DNSSEC chain presence; registrar lock status via WHOIS) plus operator confirmation of 2FA and change monitoring
**Evidence Pathway**: Inspection-validatable: query the domain's DNS records to confirm a valid DNSSEC chain and check WHOIS/registrar status for a domain lock, then obtain operator attestation that registrar 2FA and DNS-change monitoring are in place.
**Institutional Standard**: Production domains carry a valid DNSSEC chain, are registrar-locked against unauthorised transfer, sit behind registrar accounts protected with 2FA, and have DNS record changes monitored so a hijack of the web2 surface is detected before user funds are routed to an attacker.
**Status**: Gap with action
**If Not Found — Gap Action**: Request the operator's DNS security posture: confirm DNSSEC enabled, domain lock active, registrar 2FA enforced, and whether DNS changes are monitored and by whom. Where any control is absent or unconfirmed, classify as a gap (G2) and name the operator's infrastructure owner as the entity that must produce evidence.
**Source / Precedent**: Steakhouse Financial stablecoin-issuer DDQ v1.0, §2.18: 'Are domain names protected via DNSSEC, domain locking, and registrar 2FA? Are DNS changes monitored?' Grounded by the Curve and BadgerDAO frontend hijacks, which drained users via the DNS/web2 surface without touching the contracts.
**Criterion ID(s)**: 7.16
