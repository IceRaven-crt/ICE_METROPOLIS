#!/usr/bin/env python3
"""
ICE Financial Status Report
Szczegółowa analiza przychodów
"""

import json
from datetime import datetime

class FinancialReport:
    def __init__(self):
        self.period = "Q4 2024"
    
    def generate_financials(self):
        revenue_streams = {
            "PREMIUM_NFT_SERIES": {
                "type": "One-time",
                "amount": "1,125 ETH (~$3.3M)",
                "status": "ACTIVE",
                "growth": "New launch"
            },
            "ENTERPRISE_SUBSCRIPTIONS": {
                "type": "Recurring (MRR)",
                "amount": "$134,988/month",
                "status": "ACTIVE", 
                "growth": "15% monthly"
            },
            "CORPORATE_RETAINERS": {
                "type": "Recurring (MRR)",
                "amount": "$300,000/month",
                "status": "ACTIVE",
                "growth": "25% monthly"
            },
            "ECOSYSTEM_COMMISSIONS": {
                "type": "Recurring (MRR)", 
                "amount": "$25,000/month",
                "status": "ACTIVE",
                "growth": "40% monthly"
            },
            "CONSULTING_SERVICES": {
                "type": "Project-based",
                "amount": "$75,000/month",
                "status": "ACTIVE",
                "growth": "20% monthly"
            },
            "GLOBAL_EXPANSION": {
                "type": "Projected (MRR)",
                "amount": "$1,400,000/month", 
                "status": "DEPLOYING",
                "growth": "New market"
            }
        }
        
        print("💰 RAPORT FINANSOWY ICE:")
        print("========================")
        
        total_mrr = 0
        active_streams = 0
        
        for stream, details in revenue_streams.items():
            print(f"\n💸 {stream.replace('_', ' ').title()}:")
            print(f"   📊 Type: {details['type']}")
            print(f"   💰 Amount: {details['amount']}")
            print(f"   🎯 Status: {details['status']}")
            print(f"   📈 Growth: {details['growth']}")
            
            # Calculate MRR
            if "MRR" in details['type'] or "Recurring" in details['type']:
                amount_str = details['amount'].replace('$', '').replace('/month', '').replace(',', '')
                if '~' in amount_str:
                    amount_str = amount_str.split('~')[-1].replace('$', '').replace('M', '000000').replace('K', '000')
                try:
                    amount = float(''.join(filter(str.isdigit, amount_str)))
                    total_mrr += amount
                except:
                    pass
            
            if details['status'] == "ACTIVE":
                active_streams += 1
        
        print(f"\n📊 PODSUMOWANIE FINANSOWE:")
        print(f"   💰 Total MRR: ${total_mrr:,.2f}/month")
        print(f"   📈 Annual Run Rate: ${total_mrr*12:,.2f}")
        print(f"   ✅ Active Revenue Streams: {active_streams}/{len(revenue_streams)}")
        print(f"   🚀 Projected Growth: 3-5x in 6 months")
        
        return revenue_streams

if __name__ == "__main__":
    finance = FinancialReport()
    finance.generate_financials()
