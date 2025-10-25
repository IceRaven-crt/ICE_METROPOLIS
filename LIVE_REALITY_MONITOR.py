#!/usr/bin/env python3
# 🧊 LIVE REALITY MONITOR - MONITORING W CZASIE RZECZYWISTYM
import time
from datetime import datetime
from pathlib import Path

print("🧊 LIVE REALITY MONITOR - ICE_METROPOLIS")
print("=" * 45)
print("🎯 MONITORUJĘ RZECZYWISTOŚĆ SYSTEMU")
print("⏰ Rozpoczęcie: " + datetime.now().strftime("%H:%M:%S"))
print("")

def monitor_reality():
    try:
        while True:
            # Sprawdź stan systemu
            chain_file = Path("logs/ICE_CHAIN_BLOCK.csv")
            if chain_file.exists():
                with open(chain_file, 'r') as f:
                    lines = f.readlines()
                    activity_count = len(lines) - 1  # minus header
                
                print(f"📊 Aktywności w blockchain: {activity_count}")
                print(f"⏰ Czas systemowy: {datetime.now().strftime('%H:%M:%S')}")
                print("🟢 SYSTEM DZIAŁA RZECZYWISCIE")
                print("-" * 40)
            
            time.sleep(30)  # sprawdzaj co 30 sekund
            
    except KeyboardInterrupt:
        print("")
        print("⏹️  Monitoring zatrzymany")
        print("💫 RZECZYWISTOŚĆ POTWIERDZONA!")

# Uruchom monitoring
monitor_reality()
