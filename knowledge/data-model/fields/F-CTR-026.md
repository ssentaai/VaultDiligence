# F-CTR-026

**Field ID**: F-CTR-026
**Category**: Smart Contract
**Sub-Category**: Testing & Assurance
**Field Name**: Test/Fuzz Coverage & Full-Stack Penetration Testing
**What to Collect / Question to Answer**: What unit, integration, and fuzz/invariant test coverage exists for the contracts, and has penetration testing been performed across the entire technology stack rather than the contracts alone?
**Data Type**: Structured: { line_coverage, branch_coverage, fuzz_invariant_suite: bool, pentest_performed: bool, pentest_scope, pentest_firm, pentest_date }
**Vault Types**: ALL
**Collection Tier**: T2
**Pillar(s)**: P7
**Primary Source**: Public test suite and coverage report in the source repository (coverage output, fuzz/invariant test files) plus the named penetration-test report stating scope and date
**Fallback Source**: Audit report's testing-and-coverage section and any operator-published assurance summary naming the pentest firm and stack scope
**Evidence Pathway**: Third-party-evidenced: read the repository's coverage report and fuzz/invariant suite, and obtain the named penetration-test report (firm and date) confirming the full stack — not only contracts — was in scope.
**Institutional Standard**: Contracts carry high line and branch coverage backed by a fuzz/invariant suite, and a named firm has penetration-tested the entire stack (contracts, off-chain services, frontend, infrastructure) with the report's scope and date stated.
**Status**: Gap with action
**If Not Found — Gap Action**: If coverage figures or a fuzz/invariant suite are absent, classify G2 and require the operator to publish the coverage report and test suite; if penetration testing is contracts-only or absent, state the gap and require a full-stack pentest naming firm, scope, and date.
**Source / Precedent**: Resolv, Mar 2026: 18 smart-contract audits passed yet the off-chain signing path was never penetration-tested, and that out-of-scope stack layer was the actual attack vector ($34M net loss).
**Criterion ID(s)**: 7.5, RF02
