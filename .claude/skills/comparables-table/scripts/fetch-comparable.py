#!/usr/bin/env python3
"""
Fetch comparable vault data from DefiLlama and Vaults.fyi.
Usage:
  python3 fetch-comparable.py --slug morpho --chain ethereum --address 0x...
"""
import sys, os, json, requests

def fetch_defillama(slug):
    r = requests.get(f'https://api.llama.fi/protocol/{slug}', timeout=10)
    if r.status_code != 200:
        return None
    d = r.json()
    return {
        'tvl': d.get('tvl', [{}])[-1].get('totalLiquidityUSD'),
        'name': d.get('name'),
        'chain': d.get('chain'),
    }

def fetch_vaultsfyi(chain, address):
    r = requests.get(
        f'https://api.vaults.fyi/v1/vaults/{chain}/{address}',
        timeout=10
    )
    if r.status_code != 200:
        return None
    d = r.json()
    return {
        'netApy': d.get('netApy') or d.get('apy'),
        'totalAssets': d.get('totalAssets'),
    }

if __name__ == '__main__':
    slug = None
    chain = 'ethereum'
    address = None

    args = sys.argv[1:]
    for i, arg in enumerate(args):
        if arg == '--slug' and i+1 < len(args): slug = args[i+1]
        if arg == '--chain' and i+1 < len(args): chain = args[i+1]
        if arg == '--address' and i+1 < len(args): address = args[i+1]

    if slug:
        data = fetch_defillama(slug)
        print(f"DefiLlama: {json.dumps(data, indent=2)}")

    if address:
        data = fetch_vaultsfyi(chain, address)
        print(f"Vaults.fyi: {json.dumps(data, indent=2)}")
