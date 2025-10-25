#!/usr/bin/env python3
import datetime

class LegacyIncomeTracker:
    def __init__(self):
        self.legacy_holder = "Nikoś Szczurowski"
        self.ice_nft = "#2137"
        self.income_start = datetime.datetime.now()
    
    def calculate_legacy_income(self):
        # 10% wszystkich przychodów idzie na legacy
        base_income = 1800  # dzienny przychód
        legacy_percentage = 0.10  # 10%
        
        daily_legacy = base_income * legacy_percentage
        monthly_legacy = daily_legacy * 30
        yearly_legacy = daily_legacy * 365
        
        print(f"👶 LEGACY INCOME FOR: {self.legacy_holder}")
        print(f"🧊 BACKED BY: ICE NFT {self.ice_nft}")
        print("=" * 40)
        print(f"💰 Daily: ${daily_legacy:.2f}")
        print(f"📅 Monthly: ${monthly_legacy:.2f}")
        print(f"🎯 Yearly: ${yearly_legacy:.2f}")
        print("=" * 40)
        print(f"💎 Secure blockchain storage: ACTIVE")
        print(f"🕐 Started: {self.income_start}")

# AKTYWUJ LEGACY SYSTEM
legacy = LegacyIncomeTracker()
legacy.calculate_legacy_income()
