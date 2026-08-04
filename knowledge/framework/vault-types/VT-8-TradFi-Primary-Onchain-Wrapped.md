# VT-8 — TradFi-Primary / Onchain-Wrapped

VT-8 — TradFi-Primary / Onchain-Wrapped | A vault where the primary yield-bearing instrument is a publicly traded TradFi security (listed equity, listed preferred stock, listed bond, ETF, money market fund) held at a TradFi prime broker or custodian, with an onchain ERC-4626 or equivalent wrapper providing DeFi composability. The onchain layer is a distribution and access mechanism. The TradFi layer is where the primary risk resides. 

Primary risk layer (assess first): issuer corporate risk, listed instrument price and dividend risk, TradFi prime brokerage custody, settlement chain, tax character. 
Secondary risk layer (assess second): onchain oracle, PoR provider, ERC-4626 contract, access control, blacklist/pause. 

EXAMPLE: a preferred-equity-backed vault. Primary layer: a listed preferred instrument (the issuer's perpetual preferred equity on Nasdaq), held at the prime broker via the execution broker. Secondary layer: a preferred-equity-backed token ERC-4626 on Ethereum, Chainlink oracle, Accountable PoR. 

DO NOT ASSESS VT-8 AS VT-3. VT-3 assumes primary risk is private credit or offchain fund. VT-8 primary risk is a publicly traded instrument with daily liquidity, a corporate issuer with SEC filing obligations, and a TradFi settlement chain. The assessment criteria and pillar weightings are materially different.