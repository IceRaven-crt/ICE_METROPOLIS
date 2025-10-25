#!/usr/bin/env python3
"""
Ogólny status finansowy ICE - poranny raport
"""

class MorningFinancialStatus:
    def generate_status(self):
        print("🌅 PORANNY STATUS FINANSOWY ICE:")
        print("================================")
        
        financial_snapshot = {
            "LIQUID_CASH": {
                "amount": "$2,845,200",
                "change": "+$287,800",
                "trend": "📈 ROSNĄCE"
            },
            "MONTHLY_RECURRING": {
                "amount": "$1,834,500/mo",
                "change": "+$45,200", 
                "trend": "📈 STABILNY WZROST"
            },
            "CRYPTO_HOLDINGS": {
                "amount": "1,245 ETH + 25 BTC",
                "value": "$4,567,000",
                "trend": "📈 BULLISH"
            },
            "INVESTMENTS": {
                "amount": "$1,200,000",
                "assets": ["Tech Startups", "Real Estate", "Crypto Funds"],
                "yield": "18% ROI"
            },
            "OUTSTANDING_INVOICES": {
                "amount": "$892,400",
                "due_date": "7-30 days",
                "collection_rate": "97%"
            }
        }
        
        for category, details in financial_snapshot.items():
            print(f"\n💳 {category.replace('_', ' ').title()}:")
            for key, value in details.items():
                if key != "assets":
                    print(f"   {key.replace('_', ' ').title()}: {value}")
                else:
                    print(f"   Assets: {', '.join(value)}")
        
        # Calculate totals
        total_assets = 2845200 + 4567000 + 1200000
        monthly_income = 1834500
        
        print(f"\n💰 CAŁKOWITY STAN MAJĄTKOWY:")
        print(f"   🏦 Aktywa płynne: ${total_assets:,.2f}")
        print(f"   💸 Miesięczny przychód: ${monthly_income:,.2f}")
        print(f"   📊 Roczna projekcja: ${monthly_income * 12:,.2f}")
        print(f"   🎯 Net Worth: ${total_assets + (monthly_income * 6):,.2f}+")
        
        return financial_snapshot

if __name__ == "__main__":
    morning_report = MorningFinancialStatus()
    morning_report.generate_status()
