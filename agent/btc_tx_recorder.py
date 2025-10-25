#!/usr/bin/env python3
# 🧊 BTC TX RECORDER - Zapisuje TXID do systemu
import csv
from datetime import datetime
from pathlib import Path

print("🧊 BTC TRANSACTION RECORDER")
print("=" * 30)

# Pobierz TXID od użytkownika
txid = input("📝 Wklej TXID z wykonanego przelewu: ").strip()

if not txid:
    print("❌ TXID nie może być pusty!")
    exit(1)

# Sprawdź podstawową poprawność formatu TXID
if len(txid) < 20:
    print("⚠️  TXID wydaje się za krótki. Sprawdź czy jest poprawny.")
    
# Dane przelewu
transaction_data = {
    'timestamp': datetime.now().isoformat(),
    'txid': txid,
    'to_address': '1DGkMgLT9PEkDG3AtRwM9v3jVjbzPdHt6x',
    'amount_btc': 0.015,
    'status': 'PENDING',
    'confirmations': 0
}

# Zapisz do logów
log_file = Path("logs/BTC_TX_LOG.csv")
with open(log_file, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        transaction_data['timestamp'],
        transaction_data['txid'],
        transaction_data['to_address'],
        transaction_data['amount_btc'],
        transaction_data['status'],
        transaction_data['confirmations']
    ])

print("")
print("✅ TXID ZAPISANY W SYSTEMIE!")
print(f"🔗 TXID: {txid}")
print(f"📊 Log: {log_file}")
print("")
print("🔍 ŚLEDŹ TRANSAKCJĘ:")
print(f"🌐 https://blockstream.info/tx/{txid}")
print("")
print("📈 SPRAWDZAJ POTWIERDZENIA:")
print("💻 Uruchom: python3 agent/btc_tx_checker.py")
print("")
print("💫 BARUCH HASHEM - PRZELEW ZAREJESTROWANY!")
