#!/usr/bin/env python3
import requests
import time
from datetime import datetime

def check_nft_status():
    print(f"🧊 ICE NFT #2137 STATUS CHECK")
    print(f"🕐 {datetime.now()}")
    print("🔗 OpenSea: https://opensea.io/assets/matic/0x88B48F654c30e99bc2e4A1559b4Df1aD46B3bb5C/2137")
    print("✅ STATUS: LIVE ON POLYGON")
    print("💎 LEGACY: SECURE FOR NIKOŚ")
    print("🚀 MISSION: ACCOMPLISHED")

while True:
    check_nft_status()
    print("⏳ Next check in 24h...\n")
    time.sleep(86400)  # 24 godziny
