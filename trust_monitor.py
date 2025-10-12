#!/usr/bin/env python3
import datetime
import time
import random

class TrustMonitor:
    def __init__(self):
        self.beneficiary = "Nikoś Szczurowski"
        self.founder = "Paweł Szczurowski"
        self.start_time = datetime.datetime.now()
        self.total_accumulated = 0
        
    def live_wealth_tracker(self):
        print("💰 LIVE TRUST FUND GROWTH TRACKER")
        print("=" * 60)
        print(f"👶 Beneficiary: {self.beneficiary}")
        print(f"👑 Founder: {self.founder}")
        print(f"🕐 Started: {self.start_time}")
        print("=" * 60)
        
        daily_income = 50000
        seconds_per_day = 10  # przyspieszone dla demonstracji
        
        try:
            while True:
                current_time = datetime.datetime.now()
                elapsed = (current_time - self.start_time).total_seconds()
                days_elapsed = elapsed / seconds_per_day
                
                accumulated = daily_income * days_elapsed
                self.total_accumulated = accumulated
                
                # Wyczyść ekran (dla lepszego efektu)
                print("\033[H\033[J")  # clear screen
                
                print("💰 LIVE TRUST FUND GROWTH TRACKER")
                print("=" * 60)
                print(f"👶 Beneficiary: {self.beneficiary}")
                print(f"👑 Founder: {self.founder}")
                print(f"🕐 Tracking since: {self.start_time}")
                print("=" * 60)
                
                print(f"📈 ACCUMULATED WEALTH: ${accumulated:,.2f}")
                print(f"⏱️  Elapsed time: {elapsed:.1f}s (simulated: {days_elapsed:.1f} days)")
                
                # Pokazuj alokacje w czasie rzeczywistym
                allocations = {
                    "Education Fund": accumulated * 0.20,
                    "Investment Portfolio": accumulated * 0.30,
                    "Real Estate": accumulated * 0.25,
                    "Crypto Assets": accumulated * 0.15,
                    "Liquid Cash": accumulated * 0.10
                }
                
                print(f"\n📊 CURRENT ALLOCATIONS:")
                for category, amount in allocations.items():
                    print(f"   {category}: ${amount:,.2f}")
                
                # Projekcja na najbliższe lata
                print(f"\n🔮 PROJECTIONS:")
                for years in [1, 5, 10, 18]:
                    future_amount = accumulated + (daily_income * 365 * years)
                    if years == 18:
                        print(f"   🎓 Age 18: ${future_amount:,.2f}")
                    else:
                        print(f"   +{years} years: ${future_amount:,.2f}")
                
                time.sleep(1)  # Update co sekundę
                
        except KeyboardInterrupt:
            print(f"\n🛑 Tracking stopped")
            print(f"💎 FINAL ACCUMULATED: ${self.total_accumulated:,.2f}")
            return self.total_accumulated

# URUCHOM MONITOROWANIE W CZASIE RZECZYWISTYM
monitor = TrustMonitor()
final_amount = monitor.live_wealth_tracker()
