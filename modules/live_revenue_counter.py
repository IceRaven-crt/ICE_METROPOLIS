#!/usr/bin/env python3
"""
ICE Live Revenue Counter - Real-time progress to $100M
"""

import time
import random
from datetime import datetime

class LiveRevenueCounter:
    def __init__(self):
        self.current_revenue = 72000000  # Start from $72M
        self.target_revenue = 100000000  # $100M target
        self.last_update = datetime.now()
        
    def simulate_growth(self):
        while self.current_revenue < self.target_revenue:
            # Simulate revenue growth
            hourly_growth = random.randint(8000, 15000)  # $8K-$15K per hour
            self.current_revenue += hourly_growth
            
            # Calculate progress
            progress = (self.current_revenue / self.target_revenue) * 100
            remaining = self.target_revenue - self.current_revenue
            
            # Display progress
            print(f"🧊 ICE $100M CHALLENGE - LIVE")
            print(f"💰 ${self.current_revenue:,.2f} / ${self.target_revenue:,.2f}")
            print(f"📈 {progress:.2f}% - Pozostało: ${remaining:,.2f}")
            
            # Progress bar
            bars = int(progress / 2)
            print(f"[{'🟢' * bars}{'⚪' * (50 - bars)}]")
            
            print(f"⏰ {datetime.now().strftime('%H:%M:%S')}")
            print("─" * 60)
            
            time.sleep(2)  # Update every 2 seconds
            
            if self.current_revenue >= self.target_revenue:
                print("🎉 🎉 🎉 $100M OSIĄGNIĘTE! 🎉 🎉 🎉")
                break

if __name__ == "__main__":
    counter = LiveRevenueCounter()
    counter.simulate_growth()
