#!/usr/bin/env python3
import json
import hashlib
from datetime import datetime

print("🌐 SYMULACJA UPLOADU IPFS")

# Wczytaj metadane
with open('ice_nft_metadata.json', 'r') as f:
    metadata = json.load(f)

# Generuj CID (symulacja)
metadata_str = json.dumps(metadata, sort_keys=True)
cid = hashlib.sha256(metadata_str.encode()).hexdigest()[:46]
cid = "Qm" + cid[2:]  # Format IPFS CID

print(f"✅ Metadane NFT:")
print(f"   CID: {cid}")
print(f"   Nazwa: {metadata['name']}")
print(f"   Blockchain: {metadata['attributes'][4]['value']}")
print(f"   Legacy: {metadata['attributes'][6]['value']}")

# Zapisz CID
with open('nft_cid.txt', 'w') as f:
    f.write(cid)

print("🎯 Gotowe do mintingu na Polygon!")
