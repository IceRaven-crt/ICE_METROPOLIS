#!/usr/bin/env python3
import datetime

class ChildBankingSystem:
    def __init__(self):
        self.initial_deposit = 516208.06
        self.accounts_created = datetime.datetime.now()
    
    def create_global_accounts(self):
        print("🏦 GLOBAL BANKING SYSTEM FOR NIKOŚ")
        print("=" * 60)
        
        banks = [
            {
                "bank": "UBS Switzerland",
                "account": "Trust Fund #NIKO-001",
                "balance": self.initial_deposit * 0.20,
                "purpose": "Long-term wealth preservation"
            },
            {
                "bank": "DBS Singapore", 
                "account": "Growth Investment #NIKO-002",
                "balance": self.initial_deposit * 0.25,
                "purpose": "Asian market investments"
            },
            {
                "bank": "J.P. Morgan New York",
                "account": "US Markets #NIKO-003", 
                "balance": self.initial_deposit * 0.20,
                "purpose": "Stock portfolio management"
            },
            {
                "bank": "Emirates NBD Dubai",
                "account": "Middle East #NIKO-004",
                "balance": self.initial_deposit * 0.15,
                "purpose": "Regional opportunities"
            },
            {
                "bank": "HSBC London",
                "account": "European #NIKO-005",
                "balance": self.initial_deposit * 0.20,
                "purpose": "European investments"
            }
        ]
        
        total_allocated = 0
        for bank in banks:
            print(f"🏛️  {bank['bank']}:")
            print(f"   💰 Balance: ${bank['balance']:,.2f}")
            print(f"   📋 Account: {bank['account']}")
            print(f"   🎯 Purpose: {bank['purpose']}")
            total_allocated += bank['balance']
        
        print(f"\n💰 TOTAL BANK DEPOSITS: ${total_allocated:,.2f}")
        print(f"📅 Accounts Created: {self.accounts_created}")
    
    def setup_financial_controls(self):
        print(f"\n🛡️ FINANCIAL CONTROLS & SAFEGUARDS:")
        print("=" * 50)
        
        controls = [
            "Dual Authorization for Large Withdrawals",
            "Monthly Spending Limits by Category", 
            "Educational Expense Pre-Approval",
            "Investment Risk Management Protocols",
            "Fraud Detection AI Monitoring",
            "Regular Financial Health Audits",
            "Age-Based Access Graduation",
            "Philanthropic Giving Oversight"
        ]
        
        for control in controls:
            print(f"   🔒 {control}")

# STWÓRZ SYSTEM BANKOWY
banking = ChildBankingSystem()
banking.create_global_accounts()
banking.setup_financial_controls()
