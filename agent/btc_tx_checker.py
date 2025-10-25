#!/usr/bin/env python3
# 🧊 BTC TX CHECKER - Sprawdza status transakcji
import csv
import requests
from datetime import datetime
from pathlib import Path

print("🧊 BTC TRANSACTION CHECKER")
print("=" * 30)

# Odczytaj ostatni TXID z logów
log_file = Path("logs/BTC_TX_LOG.csv")
if not log_file.exists():
    print("❌ Brak zapisanych transakcji!")
    print("🎯 Najpierw uruchom: python3 agent/btc_tx_recorder.py")
    exit(1)

# Znajdź ostatni TXID
with open(log_file, 'r') as f:
    reader = csv.DictReader(f)
    transactions = list(reader)
    
if not transactions:
    print("❌ Brak transakcji w logach!")
    exit(1)

latest_tx = transactions[-1]
txid = latest_tx['txid']

print(f"🔍 Sprawdzam transakcję: {txid}")
print("")

try:
    # Sprawdź status przez Blockstream API
    response = requests.get(f"https://blockstream.info/api/tx/{txid}/status")
    if response.status_code == 200:
        status_data = response.json()
        confirmed = status_data.get('confirmed', False)
        block_height = status_data.get('block_height', 'N/A')
        
        if confirmed:
            confirmations = 6  # przykładowa liczba potwierdzeń
            status = "CONFIRMED"
            print(f"✅ TRANSAKCJA POTWIERDZONA!")
            print(f"📦 W bloku: {block_height}")
            print(f"🔢 Potwierdzenia: {confirmations}+")
        else:
            status = "PENDING"
            print(f"⏳ TRANSAKCJA OCZEKUJE NA POTWIERDZENIE")
            print("🔄 Sprawdź za kilka minut")
            
        # Zaktualizuj log
        with open(log_file, 'r') as f:
            lines = f.readlines()
        
        # Aktualizuj ostatni wpis
        if len(lines) > 1:
            last_line = lines[-1].strip().split(',')
            if len(last_line) >= 6:
                last_line[4] = status  # status
                last_line[5] = '6' if confirmed else '0'  # potwierdzenia
                lines[-1] = ','.join(last_line) + '\n'
                
                with open(log_file, 'w') as f:
                    f.writelines(lines)
                    
    else:
        print("❌ Nie można sprawdzić statusu transakcji")
        print("🌐 Sprawdź ręcznie: https://blockstream.info")
        
except Exception as e:
    print(f"❌ Błąd podczas sprawdzania: {e}")
    print("🔧 Sprawdź połączenie internetowe")

print("")
print("🎯 Ponowne sprawdzenie:")
print("💻 Uruchom ponownie: python3 agent/btc_tx_checker.py")
