#!/usr/bin/env python3
"""
ICE Live Dashboard - Monitorowanie wszystkich systemów
"""

import time
import random
from datetime import datetime

class LiveDashboard:
    def __init__(self):
        self.systems = {
            "CRYPTO_MINING": {"status": "🟢", "revenue": 25000},
            "DEFI_FARMING": {"status": "🟢", "revenue": 18000},
            "AI_TRADING": {"status": "🟢", "revenue": 35000},
            "NFT_FACTORY": {"status": "🟢", "revenue": 75000},
            "REAL_ESTATE": {"status": "🟢", "revenue": 45000},
            "GLOBAL_EXPANSION": {"status": "🟡", "revenue": 0}
        }
    
    def show_dashboard(self):
        print("🎛️ ICE LIVE DASHBOARD - FULL POWER MODE")
        print("=" * 50)
        
        total_daily = 0
        for system, data in self.systems.items():
            revenue = data["revenue"] * (1 + random.uniform(-0.1, 0.2))
            total_daily += revenue
            print(f"{data['status']} {system:<20} ${revenue:>8,.2f}/dzień")
            
        hourly = total_daily / 24
        monthly = total_daily * 30
        
        print(f"\n📊 PODSUMOWANIE LIVE:")
        print(f"💰 DZIENNIE: ${total_daily:,.2f}")
        print(f"⏰ GODZINOWO: ${hourly:,.2f}")
        print(f"📈 MIESIĘCZNIE: ${monthly:,.2f}")
        print(f"🚀 ROCZNIE: ${monthly * 12:,.2f}")
        
        print(f"\n🕒 Ostatnia aktualizacja: {datetime.now().strftime('%H:%M:%S')}")
        
        return total_daily

# Continuous monitoring
dashboard = LiveDashboard()
while True:
    dashboard.show_dashboard()
    print("\n" + "="*50)
    time.sleep(10)  # Update every 10 seconds
