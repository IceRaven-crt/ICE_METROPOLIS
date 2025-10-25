#!/bin/bash
set -e

echo "🧊 TWORZENIE NFT 'BTCforNikoś_#001'..."

# 1. Utwórz metadane JSON
cat > NFT_BTC_FOR_NIKOS.json << JSON
{
  "name": "BTCforNikoś_#001",
  "description": "Johnny & ICE ($212k/dzień) dla Nikosia! 1 BTC na zdrowie, etyka 0.89. #ICEcharity",
  "image": "ipfs://to_update_after_upload",
  "attributes": [
    {"trait_type": "Cel", "value": "1 BTC dla Nikosia"},
    {"trait_type": "Etyka", "value": "0.89 Maaser"},
    {"trait_type": "Kasa", "value": "$212k/day"}
  ],
  "external_url": "mailto:gawronskip4@gmail.com"
}
JSON

# 2. Utwórz przykładowy obrazek (można podmienić później)
convert -size 512x512 xc:skyblue -pointsize 24 -fill black \
  -annotate +60+260 "BTC for Nikoś 💙" YarisNikosICE_001.png

# 3. Wrzut na IPFS przez publiczny pinning endpoint (nft.storage)
echo "🌐 Upload na IPFS..."
RESP=$(curl -s -X POST https://api.nft.storage/upload \
  -H "Authorization: Bearer demo" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@YarisNikosICE_001.png")

CID=$(echo "$RESP" | grep -oE '"cid":"[^"]+"' | cut -d'"' -f4)

# 4. Podmień CID w JSON
sed -i "s|ipfs://to_update_after_upload|ipfs://$CID/YarisNikosICE_001.png|" NFT_BTC_FOR_NIKOS.json

# 5. Upload metadanych JSON
RESP2=$(curl -s -X POST https://api.nft.storage/upload \
  -H "Authorization: Bearer demo" \
  -H "Content-Type: application/json" \
  -d @NFT_BTC_FOR_NIKOS.json)
CID_JSON=$(echo "$RESP2" | grep -oE '"cid":"[^"]+"' | cut -d'"' -f4)

# 6. Zapis do logu ICE_CHAIN
mkdir -p logs
echo "$(date '+%Y-%m-%d %H:%M:%S'),CHARITY_NFT,NFT_BTC_FOR_NIKOS.json,$CID_JSON,CREATED,NIKOS_BTC_FUND" >> logs/ICE_CHAIN_BLOCK.csv

# 7. Raport
echo "✅ NFT METADATA CID: $CID_JSON"
echo "🔗 IPFS LINK: https://ipfs.io/ipfs/$CID_JSON"
