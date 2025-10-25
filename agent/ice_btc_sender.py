#!/usr/bin/env python3
# 🧊 ICE_BTC_WITHDRAW_AGENT v1.0
import os
import json
import csv
import requests
from datetime import datetime
from pathlib import Path
import hashlib
import qrcode

# Konfiguracja ścieżek
BASE_DIR = Path("/data/data/com.termux/files/home/ICE_METROPOLIS")
KEYS_DIR = BASE_DIR / "keys"
AGENT_DIR = BASE_DIR / "agent" 
LOGS_DIR = BASE_DIR / "logs"
CONFIG_DIR = BASE_DIR / "config"

# Tworzenie struktur katalogów
for directory in [KEYS_DIR, AGENT_DIR, LOGS_DIR, CONFIG_DIR]:
    directory.mkdir(exist_ok=True)

# Konfiguracja przelewu
BTC_CONFIG = {
    "target_address": "1DGkMgLT9PEkDG3AtRwM9v3jVjbzPdHt6x",
    "amount_btc": 0.015,
    "fee_rate": 10,
    "network": "bitcoin",
    "api_endpoint": "https://blockstream.info/api/",
    "ice_wallet_name": "ICE_METROPOLIS_MAIN"
}

# Zapisz konfigurację
CONFIG_FILE = CONFIG_DIR / "ice_btc_config.json"
CONFIG_FILE.write_text(json.dumps(BTC_CONFIG, indent=2))

print("✅ Agent BTC zapisany: agent/ice_btc_sender.py")
print("✅ Konfiguracja zapisana: config/ice_btc_config.json")
