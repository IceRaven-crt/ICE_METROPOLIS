#!/usr/bin/env python3
# 🧊 ICE_BTC_AGENT - PEŁNA WERSJA
import json
import csv
from datetime import datetime
from pathlib import Path

print("🧊 ICE_BTC_WITHDRAW_AGENT v1.0 - AKTYWACJA")
print("=" * 50)

# Konfiguracja
CONFIG = {
    "target_address": "1DGkMgLT9PEkDG3AtRwM9v3jVjbzPdHt6x",
    "amount_btc": 0.015,
    "network": "bitcoin"
}

print("🎯 KONFIGURACJA PRZELEWU:")
print(f"📍 Adres: {CONFIG['target_address']}")
print(f"💰 Kwota: {CONFIG['amount_btc']} BTC")
print(f"🌐 Sieć: {CONFIG['network']}")
print("")

try:
    from bitcoinlib.wallets import Wallet
    
    print("✅ BITCOINLIB: ZAINSTALOWANY")
    print("🔄 TWORZENIE PORTFELA ICE_METROPOLIS...")
    
    # Tworzymy portfel
    wallet = Wallet.create(
        "ICE_METROPOLIS_BTC_WALLET", 
        network=CONFIG['network']
    )
    
    print("🎉 PORTFEL UTWORZONY!")
    print(f"📧 Adres: {wallet.get_key().address}")
    print(f"🔐 Mnemonic: {wallet.mnemonic}")
    print("")
    print("⚠️  ZAPISZ MNEMONIC W BEZPIECZNYM MIEJSCU!")
    print("")
    
    # Zapisz backup
    backup_file = Path("keys/ice_wallet_backup.txt")
    backup_file.write_text(f"""ICE_METROPOLIS BTC WALLET BACKUP
Created: {datetime.now()}
Network: {CONFIG['network']}

MNEMONIC: {wallet.mnemonic}

ADDRESS: {wallet.get_key().address}

PRZELEW KONFIGURACJA:
Target: {CONFIG['target_address']}
Amount: {CONFIG['amount_btc']} BTC
""")
    
    print(f"💾 Backup zapisany: {backup_file}")
    
    # Sprawdź balans
    balance = wallet.balance()
    print(f"💰 Balans: {balance} sats ({balance/100000000:.8f} BTC)")
    
    # Przygotuj transakcję
    print("")
    print("🔧 PRZYGOTOWANIE TRANSAKCJI...")
    print(f"📤 Z: {wallet.get_key().address}")
    print(f"📥 Do: {CONFIG['target_address']}") 
    print(f"💰 Kwota: {CONFIG['amount_btc']} BTC")
    
    # Zapisz log
    log_file = Path("logs/BTC_TX_READY.csv")
    if not log_file.exists():
        log_file.write_text("timestamp,from_address,to_address,amount_btc,status\n")
    
    with open(log_file, 'a') as f:
        f.write(f'{datetime.now()},{wallet.get_key().address},{CONFIG["target_address"]},{CONFIG["amount_btc"]},READY\n')
    
    print("")
    print("✅ SYSTEM GOTOWY DO PRZELEWU!")
    print("📋 Log transakcji zapisany")
    
except Exception as e:
    print(f"❌ Błąd: {e}")
    print("📦 Sprawdź instalację: pip install bitcoinlib")

print("")
print("🎯 NASTĘPNY KROK:")
print("🔧 Wpłać BTC na adres portfela")
print("⚡ Wykonaj przelew")
print("📊 Monitoruj transakcję")
print("")
print("💫 BARUCH HASHEM - AGENT BTC AKTYWNY!")
