#!/usr/bin/env python3
"""
VaultDiligence T1 API Validation
Confirms each T1 source returns expected data structure
before running any vault investigation.

Reference vault: Steakhouse Prime USDC on Morpho (Ethereum)
Address: 0xYOUR_VAULT_ADDRESS_HERE
Chain: 1 (Ethereum)

Run this before the first investigation session.
Fix every FAIL before running /d1.

Usage:
  python3 scripts/validate-apis.py
  python3 scripts/validate-apis.py --vault 0x... --chain 1
"""

import requests
import json
import sys
import time
from datetime import datetime, timezone

# Reference vault for validation
DEFAULT_VAULT = '0xYOUR_VAULT_ADDRESS_HERE'
DEFAULT_CHAIN = 1

PASS = 'PASS'
FAIL = 'FAIL'
WARN = 'WARN'  # returns data but structure differs from expected

results = []

def test(name, url, check_fn, notes=''):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            results.append({'api': name, 'status': FAIL, 'reason': f'HTTP {r.status_code}', 'url': url, 'notes': notes})
            return None
        data = r.json()
        ok, reason = check_fn(data)
        status = PASS if ok else FAIL
        results.append({'api': name, 'status': status, 'reason': reason, 'url': url, 'notes': notes})
        return data
    except requests.exceptions.Timeout:
        results.append({'api': name, 'status': FAIL, 'reason': 'Timeout (10s)', 'url': url, 'notes': notes})
        return None
    except Exception as e:
        results.append({'api': name, 'status': FAIL, 'reason': str(e), 'url': url, 'notes': notes})
        return None

def run_validation(vault=DEFAULT_VAULT, chain=DEFAULT_CHAIN):
    print(f'\nVaultDiligence T1 API Validation')
    print(f'Reference vault: {vault}')
    print(f'Chain: {chain}')
    print(f'Timestamp: {datetime.now(timezone.utc).isoformat()}\n')

    # 1. DefiLlama — TVL
    test(
        'DefiLlama TVL',
        'https://api.llama.fi/protocol/morpho',
        lambda d: ('tvl' in d or 'currentChainTvls' in d, 'tvl field present') if isinstance(d, dict) else (False, 'unexpected response type'),
        notes='F-FIN-001. Expect: dict with tvl or currentChainTvls'
    )

    # 2. DefiLlama yields
    test(
        'DefiLlama Yields',
        'https://yields.llama.fi/pools',
        lambda d: (isinstance(d.get('data'), list) and len(d['data']) > 0, f"{len(d.get('data', []))} pools returned"),
        notes='F-FIN-002. Expect: data array of pools'
    )

    # 3. Vaults.fyi
    test(
        'Vaults.fyi',
        f'https://api.vaults.fyi/v1/vaults/1/{vault}',
        lambda d: ('apy' in d or 'netApy' in d or 'totalAssets' in d, 'vault data present'),
        notes='F-FIN-002 APY share-price basis. If 404: vault not indexed yet.'
    )

    # 4. Morpho API
    test(
        'Morpho API',
        f'https://blue-api.morpho.org/graphql',
        lambda d: (True, 'GraphQL endpoint reachable'),
        notes='F-FIN-030. Note: Morpho uses GraphQL, not REST. Confirm in session.'
    )

    # 5. Etherscan
    test(
        'Etherscan Contract Source',
        f'https://api.etherscan.io/api?module=contract&action=getsourcecode&address={vault}&apikey=YourApiKeyToken',
        lambda d: (d.get('status') in ['1', '0'], f"status={d.get('status')} message={d.get('message')}"),
        notes='F-CTR-001. status=1 = verified. status=0 = unverified. Both are valid responses.'
    )

    # 6. 1inch quote
    test(
        '1inch Slippage Simulation',
        f'https://api.1inch.dev/swap/v6.0/1/quote?src=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&dst=0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2&amount=1000000000',
        lambda d: ('dstAmount' in d or 'toAmount' in d or 'error' in d, 'quote endpoint reachable'),
        notes='F-FIN-040 exit liquidity. Requires API key in production. Free tier may return 401.'
    )

    # 7. GLEIF
    test(
        'GLEIF Entity Search',
        'https://api.gleif.org/api/v1/fuzzycompletions?term=Steakhouse&field=entity.legalName',
        lambda d: (isinstance(d.get('data'), list), f"{len(d.get('data', []))} results"),
        notes='F-ENT-004 legal entity. Expect: data array of LEI records.'
    )

    # 8. OFAC
    test(
        'OFAC Sanctions',
        'https://sanctionslistservice.ofac.treas.gov/api/search?type=address&value=0x0000000000000000000000000000000000000000',
        lambda d: ('hits' in d or 'results' in d or isinstance(d, list), 'sanctions endpoint reachable'),
        notes='F-ENT-005 sanctions screening. Expect: search results structure.'
    )

    # 9. FRED Risk-Free Rate
    test(
        'FRED 3M T-Bill',
        'https://api.stlouisfed.org/fred/series/observations?series_id=DGS3MO&api_key=abcdefghijklmnopqrstuvwxyz012345&file_type=json&limit=1&sort_order=desc',
        lambda d: ('observations' in d or 'error_message' in d, 'FRED endpoint reachable'),
        notes='F-FIN-019 risk-free rate. Requires free FRED API key. observations[0].value = current rate.'
    )

    # 10. Solodit
    test(
        'Solodit Audit Registry',
        'https://solodit.xyz/api/projects?q=morpho',
        lambda d: (isinstance(d, (list, dict)), 'solodit endpoint reachable'),
        notes='F-SEC-006 audit history. If blocked: use web search for solodit.xyz/protocols/morpho'
    )

    # 11. GitHub
    test(
        'GitHub API',
        'https://api.github.com/repos/morpho-org/morpho-blue/stats/commit_activity',
        lambda d: (isinstance(d, list) or d == {}, f'{len(d) if isinstance(d, list) else 0} weeks of activity'),
        notes='F-ENT-060 team activity. Rate limited at 60/hr unauthenticated.'
    )

    # 12. Snapshot
    test(
        'Snapshot Governance',
        'https://hub.snapshot.org/graphql',
        lambda d: (True, 'GraphQL endpoint reachable'),
        notes='F-GOV-005. GraphQL only. Confirm query structure in session.'
    )

    # Print results
    print(f'{"API":<30} {"STATUS":<6} {"REASON":<50} NOTES')
    print('─' * 120)
    for r in results:
        status_icon = '✓' if r['status'] == PASS else '✗' if r['status'] == FAIL else '!'
        print(f"{status_icon} {r['api']:<28} {r['status']:<6} {r['reason'][:48]:<50} {r['notes'][:40]}")

    passes = sum(1 for r in results if r['status'] == PASS)
    fails = sum(1 for r in results if r['status'] == FAIL)
    total = len(results)

    print(f'\nResult: {passes}/{total} PASS | {fails} FAIL')

    if fails > 0:
        print('\nFAILED APIs — fix before running /d1:')
        for r in results:
            if r['status'] == FAIL:
                print(f'  {r["api"]}: {r["reason"]}')
                print(f'    URL: {r["url"]}')
                print(f'    Notes: {r["notes"]}')
        print('\nCommon fixes:')
        print('  API key missing: add to .env file')
        print('  Rate limited: wait 60s and retry')
        print('  Endpoint changed: check docs and update scripts/validate-apis.py')
        sys.exit(1)
    else:
        print('\nAll T1 APIs reachable. Safe to run /d1.')
        print('Note: 1inch and FRED require API keys for production use.')
        sys.exit(0)

if __name__ == '__main__':
    vault = DEFAULT_VAULT
    chain = DEFAULT_CHAIN

    args = sys.argv[1:]
    for i, arg in enumerate(args):
        if arg == '--vault' and i + 1 < len(args):
            vault = args[i + 1]
        if arg == '--chain' and i + 1 < len(args):
            chain = int(args[i + 1])

    run_validation(vault, chain)
