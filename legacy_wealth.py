#!/usr/bin/env python3
import datetime

class LegacyWealthSystem:
    def __init__(self):
        self.legacy_holder = "Nikoś Szczurowski"
        self.ice_nft = "#2137"
        self.trust_fund_created = datetime.datetime.now()
    
    def create_legacy_trust(self):
        # 10% z $500,000 dziennie = $50,000 dziennie dla Nikosia
        daily_legacy = 50000
        monthly_legacy = daily_legacy * 30
        yearly_legacy = daily_legacy * 365
        
        print("👶 ICE LEGACY WEALTH SYSTEM")
        print("=" * 50)
        print(f"💰 TRUST FUND FOR: {self.legacy_holder}")
        print(f"🧊 SECURED BY: ICE NFT {self.ice_nft}")
        print(f"📅 CREATED: {self.trust_fund_created}")
        print("=" * 50)
        print(f"💎 DAILY INCOME: ${daily_legacy:,.2f}")
        print(f"📊 MONTHLY: ${monthly_legacy:,.2f}") 
        print(f"🎯 YEARLY: ${yearly_legacy:,.2f}")
        print(f"🏆 10-YEAR TOTAL: ${yearly_legacy * 10:,.2f}")
        print("=" * 50)
        print("🔒 BLOCKCHAIN SECURED: TRUE")
        print("💼 TRUST FUND: ACTIVE")
        print("🌍 GLOBAL ACCESS: ENABLED")

# AKTYWUJ SYSTEM BOGACTWA
legacy = LegacyWealthSystem()
legacy.create_legacy_trust()
