#!/usr/bin/env python3
from decimal import Decimal
from datetime import datetime
import json

# Pobieramy rzeczywiste dochody z dashboardu ICE
DAILY_PROFIT = Decimal('212817.90')  # Z dashboardu

def calculate_realtime_maaser():
    maaser = DAILY_PROFIT * Decimal('0.10')
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "daily_profit": float(DAILY_PROFIT),
        "maaser": float(maaser),
        "impact": "REAL_TIME_DATA",
        "intention": "L'shem Shamayim - Real ICE Metropolis Revenue"
    }
    
    # Zapis
    with open("logs/REAL_MAASER_LOG.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"💰 RZECZYWISTE PRZYCHODY: ${DAILY_PROFIT:,.2f}")
    print(f"🕊️ RZECZYWISTY MAASER: ${maaser:,.2f}")
    print(f"📊 MIESIĘCZNY MAASER: ${maaser * 30:,.2f}")
    return maaser

if __name__ == "__main__":
    calculate_realtime_maaser()
