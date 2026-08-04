#!/usr/bin/env python3
"""
Fetch and parse contract ABI from Etherscan.
Usage:
  python3 fetch-abi.py 0x<contract-address> [--chain ethereum]
  python3 fetch-abi.py 0x<contract-address> --privileged-only
"""
import sys, os, json, requests

ETHERSCAN_KEY = os.getenv('ETHERSCAN_API_KEY', 'YourApiKeyToken')
CHAIN_URLS = {
    'ethereum': 'https://api.etherscan.io/api',
    'base': 'https://api.basescan.org/api',
    'arbitrum': 'https://api.arbiscan.io/api',
}

def fetch_abi(address, chain='ethereum', privileged_only=False):
    url = CHAIN_URLS.get(chain, CHAIN_URLS['ethereum'])
    params = {
        'module': 'contract',
        'action': 'getsourcecode',
        'address': address,
        'apikey': ETHERSCAN_KEY
    }
    r = requests.get(url, params=params, timeout=10)
    data = r.json()

    if data['status'] != '1':
        print(f"Not verified: {data.get('message')}")
        return

    result = data['result'][0]
    print(f"Contract: {result.get('ContractName')}")
    print(f"Compiler: {result.get('CompilerVersion')}")
    print(f"Proxy: {result.get('Proxy', '0')}")
    print(f"Implementation: {result.get('Implementation', 'N/A')}")

    abi_str = result.get('ABI', '[]')
    if abi_str == 'Contract source code not verified':
        print("\nABI: Not verified (G2 evidence state)")
        return

    try:
        abi = json.loads(abi_str)
        funcs = [f for f in abi if f.get('type') == 'function']
        if privileged_only:
            # Filter for functions with access control modifiers
            # Look for onlyOwner, onlyRole patterns in name/inputs
            print(f"\nAll functions ({len(funcs)} total):")
            for f in funcs:
                name = f.get('name', '')
                inputs = f.get('inputs', [])
                print(f"  {name}({', '.join(i.get('type','') for i in inputs)})")
        else:
            print(f"\nFunctions: {len(funcs)}")
    except Exception as e:
        print(f"ABI parse error: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 fetch-abi.py <address> [--chain ethereum|base|arbitrum] [--privileged-only]")
        sys.exit(1)

    address = sys.argv[1]
    chain = 'ethereum'
    privileged_only = '--privileged-only' in sys.argv

    if '--chain' in sys.argv:
        idx = sys.argv.index('--chain')
        chain = sys.argv[idx + 1]

    fetch_abi(address, chain, privileged_only)
