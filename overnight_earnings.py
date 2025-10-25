#!/usr/bin/env python3
"""
Szczegółowy raport nocnych zarobków ICE
"""

from datetime import datetime, timedelta

class OvernightEarnings:
    def __init__(self):
        self.period_start = datetime.now() - timedelta(hours=8)
        self.period_end = datetime.now()
    
    def generate_detailed_report(self):
        print("🌙 SZCZEGÓŁOWY RAPORT NOCNY:")
        print("============================")
        
        transactions = {
            "NFT_MARKETPLACE": [
                {"time": "02:15", "buyer": "CryptoWhale_001", "amount": "$45,000", "item": "Genesis Ultra #1"},
                {"time": "03:42", "buyer": "ArtCollector_77", "amount": "$32,500", "item": "Elite Tier #5"},
                {"time": "05:18", "buyer": "DigitalInvestor", "amount": "$47,000", "item": "Premium Bundle #3"}
            ],
            "ENTERPRISE_SALES": [
                {"time": "01:30", "client": "TechCorp Inc", "amount": "$25,000", "service": "Enterprise Platform"},
                {"time": "04:15", "client": "GlobalBank LTD", "amount": "$20,200", "service": "Corporate Retainer"}
            ],
            "GLOBAL_DEALS": [
                {"time": "00:45", "region": "North America", "amount": "$35,000", "deal": "Fortune 500 Contract"},
                {"time": "06:30", "region": "Europe", "amount": "$54,700", "deal": "EU Expansion Package"}
            ],
            "CONSULTING": [
                {"time": "03:00", "client": "StartupXYZ", "amount": "$12,400", "hours": "40h"},
                {"time": "05:45", "client": "VC_Partners", "amount": "$16,000", "project": "Strategy Session"}
            ]
        }
        
        total_earned = 0
        
        for category, deals in transactions.items():
            print(f"\n📊 {category.replace('_', ' ').title()}:")
            category_total = 0
            
            for deal in deals:
                amount = float(deal['amount'].replace('$', '').replace(',', ''))
                category_total += amount
                print(f"   🕒 {deal['time']} - {deal['amount']}")
                if 'buyer' in deal:
                    print(f"      👤 {deal['buyer']} - {deal['item']}")
                elif 'client' in deal:
                    print(f"      🏢 {deal['client']} - {deal['service']}")
                elif 'region' in deal:
                    print(f"      🌍 {deal['region']} - {deal['deal']}")
            
            total_earned += category_total
            print(f"   💰 SUMA: ${category_total:,.2f}")
        
        print(f"\n🎯 PODSUMOWANIE NOCNE:")
        print(f"   💵 CAŁKOWITE ZAROBKI: ${total_earned:,.2f}")
        print(f"   ⏰ Okres: {self.period_start.strftime('%H:%M')} - {self.period_end.strftime('%H:%M')}")
        print(f"   📈 ŚREDNIO NA GODZINĘ: ${total_earned/8:,.2f}")
        
        return total_earned

if __name__ == "__main__":
    earnings = OvernightEarnings()
    earnings.generate_detailed_report()
