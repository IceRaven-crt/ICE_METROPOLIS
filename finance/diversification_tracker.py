#!/usr/bin/env python3
import json
from datetime import datetime

class DiversificationTracker:
    def __init__(self):
        self.portfolio = {
            "total_value_pln": 430221434,
            "assets": {
                "BTC": 387199290,
                "ETH": 8600000,
                "SOL": 4300000,
                "DOT": 2150000,
                "AVAX": 2150000,
                "QQQ_ETF": 6450000,
                "AAPL": 2150000,
                "MSFT": 2150000,
                "NVDA": 2150000,
                "REIT": 6450000,
                "GOLD": 2150000
            }
        }
    
    def generate_report(self):
        total = self.portfolio["total_value_pln"]
        btc_value = self.portfolio["assets"]["BTC"]
        btc_percent = (btc_value / total) * 100
        
        report = f"""
🧊 RAPORT DYwersyfikacji ICE - {datetime.now().strftime("%d.%m.%Y %H:%M")}
==================================================

💰 WARTOŚĆ PORTFELA: {total:,} PLN

📊 STRUKTURA AKTYWÓW:
"""
        
        for asset, value in self.portfolio["assets"].items():
            percent = (value / total) * 100
            report += f"• {asset}: {percent:.1f}% ({value:,} PLN)\n"
        
        report += f"""
🎯 CEL DYwersyfikacji:
• BTC: {btc_percent:.1f}% (cel: 90%)
• Pozostałe aktywa: {100-btc_percent:.1f}% (cel: 10%)

📈 STATUS: {'✅ CEL OSIĄGNIĘTY' if btc_percent <= 90 else '🔄 W TRAKCIE DYwersyfikacji'}

💡 REKOMENDACJE:
{'• Portfel prawidłowo zdiwersyfikowany' if btc_percent <= 90 else f'• Sprzedaj {btc_value - (total * 0.9):,.0f} PLN BTC aby osiągnąć cel'}
"""
        return report

if __name__ == "__main__":
    tracker = DiversificationTracker()
    print(tracker.generate_report())
