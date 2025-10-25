#!/usr/bin/env python3
"""
ICE $100M Tracker - Live progress monitoring
"""

import time
from datetime import datetime

class ProgressTracker:
    def __init__(self):
        self.current = 72000000  # $72M
        self.target = 100000000  # $100M
        
    def show_progress(self):
        progress = (self.current / self.target) * 100
        remaining = self.target - self.current
        
        print(f"🎯 ICE $100M CHALLENGE - LIVE TRACKER")
        print("=" * 50)
        print(f"💰 AKTUALNIE: ${self.current:,.2f}")
        print(f"🎯 CEL: ${self.target:,.2f}")
        print(f"📈 POSTĘP: {progress:.1f}%")
        print(f"📊 POZOSTAŁO: ${remaining:,.2f}")
        
        # Progress bar
        bars = int(progress / 5)
        progress_bar = "🟢" * bars + "⚪" * (20 - bars)
        print(f"[{progress_bar}] {progress:.1f}%")
        
        # Time estimation (assuming current growth rate)
        daily_growth = 198000  # From dashboard
        days_remaining = remaining / daily_growth if daily_growth > 0 else 0
        
        print(f"⏰ ESTYMOWANY CZAS: {days_remaining:.1f} dni")
        print(f"📅 PRZEWIDYWANA DATA: {(datetime.now() + timedelta(days=days_remaining)).strftime('%Y-%m-%d')}")
        
        return progress

if __name__ == "__main__":
    from datetime import timedelta
    tracker = ProgressTracker()
    tracker.show_progress()
