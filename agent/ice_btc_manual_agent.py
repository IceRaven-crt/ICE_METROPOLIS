#!/usr/bin/env python3
# 🧊 ICE_BTC_MANUAL_AGENT - PRZELEW BEZ BIBLIOTEK
import json
import csv
from datetime import datetime
from pathlib import Path

print("🧊 ICE_BTC_MANUAL_AGENT v1.0")
print("=" * 50)
print("🎯 SYSTEM RĘCZNEGO PRZELEWU BTC")
print("")

# Konfiguracja przelewu
CONFIG = {
    "target_address": "1DGkMgLT9PEkDG3AtRwM9v3jVjbzPdHt6x", 
    "amount_btc": 0.015,
    "purpose": "ICE_METROPOLIS_OPERATIONS"
}

print("📋 DANE PRZELEWU:")
print(f"📍 Adres odbiorcy: {CONFIG['target_address']}")
print(f"💰 Kwota: {CONFIG['amount_btc']} BTC")
print(f"🎯 Cel: {CONFIG['purpose']}")
print("")

# Instrukcja krok po kroku
instructions = """
🚀 INSTRUKCJA WYKONANIA PRZELEWU:

KROK 1: 🏦 OTWÓRZ SWÓJ PORTFEL BTC
   • Electrum (PC/Mobile)
   • Ledger/Trezor (hardware)
   • BlueWallet, Exodus (mobile)
   • Binance, Coinbase (giełda)

KROK 2: 💸 WYKONAJ PRZELEW
   • Wklej adres: 1DGkMgLT9PEkDG3AtRwM9v3jVjbzPdHt6x
   • Wpisz kwotę: 0.015 BTC
   • Wybierz opłatę: STANDARD
   • Potwierdź transakcję

KROK 3: 📝 ZAPISZ TXID W SYSTEMIE
   • Skopiuj TXID z portfela
   • Uruchom: python3 agent/btc_tx_recorder.py
   • Wklej TXID gdy zostaniesz poproszony

KROK 4: 🔍 ŚLEDŹ TRANSAKCJĘ
   • Wejdź na: https://blockstream.info
   • Wklej TXID w wyszukiwarkę
   • Sprawdzaj potwierdzenia
"""

print(instructions)

# Przygotowanie systemu plików
Path("logs").mkdir(exist_ok=True)
Path("config").mkdir(exist_ok=True)

# Plik logów transakcji
log_file = Path("logs/BTC_TX_LOG.csv")
if not log_file.exists():
    with open(log_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'txid', 'to_address', 'amount_btc', 'status', 'confirmations'])

# Konfiguracja systemu
config_data = {
    "created": datetime.now().isoformat(),
    "target_address": CONFIG["target_address"],
    "amount_btc": CONFIG["amount_btc"],
    "purpose": CONFIG["purpose"],
    "status": "AWAITING_MANUAL_TRANSFER",
    "instructions": "Use any BTC wallet to send 0.015 BTC to the target address"
}

config_file = Path("config/btc_manual_transfer.json")
config_file.write_text(json.dumps(config_data, indent=2))

print("✅ SYSTEM PRZYGOTOWANY!")
print(f"📁 Konfiguracja: {config_file}")
print(f"📊 Logi: {log_file}")
print("")
print("🎯 TERAZ WYKONAJ PRZELEW W SWOIM PORTFELU BTC!")
print("💫 BARUCH HASHEM - SYSTEM GOTOWY!")
