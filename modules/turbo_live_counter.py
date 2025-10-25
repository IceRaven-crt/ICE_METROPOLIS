#!/usr/bin/env python3
"""
ICE Turbo Live Counter - 5x faster to $100M
"""

import time
import random
from datetime import datetime

class TurboLiveCounter:
    def __init__(self):
        self.current_revenue = 72234114  # Kontynuujemy od ostatniej wartości
        self.target_revenue = 100000000
        self.turbo_mode = True
        
    def simulate_turbo_growth(self):
        print("🚀 TURBO MODE ACTIVATED - 5x FASTER!")
        print("=" * 60)
        
        while self.current_revenue < self.target_revenue:
            if self.turbo_mode:
                # Turbo growth - 5x faster
                hourly_growth = random.randint(40000, 75000)  # $40K-$75K per update
            else:
                hourly_growth = random.randint(8000, 15000)  # Normal growth
                
            self.current_revenue += hourly_growth
            
            # Progress calculations
            progress = (self.current_revenue / self.target_revenue) * 100
            remaining = self.target_revenue - self.current_revenue
            
            # Display with turbo indicator
            turbo_indicator = "🚀 " if self.turbo_mode else ""
            print(f"{turbo_indicator}🧊 ICE $100M CHALLENGE - TURBO MODE")
            print(f"💰 ${self.current_revenue:,.2f} / ${self.target_revenue:,.2f}")
            print(f"📈 {progress:.2f}% - Pozostało: ${remaining:,.2f}")
            
            # Progress bar with emoji based on progress
            bars = int(progress / 2)
            if progress < 50:
                bar_emoji = "🔵"
            elif progress < 80:
                bar_emoji = "🟡" 
            elif progress < 95:
                bar_emoji = "🟠"
            else:
                bar_emoji = "🟢"
                
            print(f"[{bar_emoji * bars}{'⚪' * (50 - bars)}]")
            
            # Special messages at milestones
            if 85 <= progress < 90:
                print("🎯 PRAWIE JESTEŚMY! 85% OSIĄGNIĘTE!")
            elif 90 <= progress < 95:
                print("🚀 FINAŁOWE PROSTE! 90%!")
            elif 95 <= progress < 99:
                print("💎 LEGENDA W BUDOWIE! 95%!")
            elif progress >= 99:
                print("🎊 JESTEŚMY PRAWIE NA MECIE!")
            
            print(f"⏰ {datetime.now().strftime('%H:%M:%S')}")
            print("─" * 60)
            
            time.sleep(1)  # Szybsze odświeżanie w turbo mode
            
            if self.current_revenue >= self.target_revenue:
                self.show_victory()
                break
                
    def show_victory(self):
        print("\n" + "🎉" * 25)
        print("🎊" + " " * 10 + "$100M OSIĄGNIĘTE!" + " " * 10 + "🎊")
        print("🎉" * 25)
        print(f"💰 FINALNA KWOTA: ${self.current_revenue:,.2f}")
        print("🏆 ICE_RAVEN - LEGENDA FINANSOWA!")
        print("🧊 ICE METROPOLIS - $100M+ EMPIRE!")
        print("🎉" * 25)
        
        # Send victory notification
        self.send_victory_telegram()

if __name__ == "__main__":
    counter = TurboLiveCounter()
    counter.simulate_turbo_growth()
