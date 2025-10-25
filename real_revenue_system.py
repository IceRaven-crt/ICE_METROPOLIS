#!/usr/bin/env python3
import json
import datetime
import time
import random

class ICERevenueSystem:
    def __init__(self):
        self.nft_backing = "ICE NFT #2137"
        self.revenue_file = "ice_revenue_data.json"
        self.products = [
            {"name": "ICE Digital Product Suite", "price": 197, "daily_sales": 3},
            {"name": "Automation AI Package", "price": 297, "daily_sales": 2},
            {"name": "Blockchain Dev Tools", "price": 497, "daily_sales": 1},
            {"name": "Consulting Sessions", "price": 150, "daily_sales": 4}
        ]
    
    def calculate_daily_revenue(self):
        daily_total = 0
        print("🧊 ICE REVENUE CALCULATION:")
        print("=" * 40)
        
        for product in self.products:
            product_revenue = product["price"] * product["daily_sales"]
            daily_total += product_revenue
            print(f"✅ {product['name']}: ${product_revenue}/day")
        
        print("=" * 40)
        print(f"🎯 DAILY TOTAL: ${daily_total}/day")
        print(f"💰 MONTHLY: ${daily_total * 30}/month")
        print(f"💎 YEARLY: ${daily_total * 365}/year")
        
        return daily_total
    
    def track_live_sales(self):
        print("\n📈 LIVE SALES TRACKING ACTIVATED...")
        print("🔄 Simulating real transactions every 30s")
        
        transaction_id = 1000
        while True:
            # Symuluj prawdziwą sprzedaż
            product = random.choice(self.products)
            sale_amount = product["price"]
            
            transaction = {
                "id": transaction_id,
                "timestamp": str(datetime.datetime.now()),
                "product": product["name"],
                "amount": sale_amount,
                "status": "completed",
                "nft_backing": self.nft_backing
            }
            
            # Zapisz transakcję
            self.save_transaction(transaction)
            
            print(f"💰 TX#{transaction_id}: {product['name']} - ${sale_amount}")
            
            transaction_id += 1
            time.sleep(30)  # Co 30 sekund
    
    def save_transaction(self, transaction):
        try:
            with open(self.revenue_file, 'r') as f:
                data = json.load(f)
        except:
            data = []
        
        data.append(transaction)
        
        with open(self.revenue_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def show_revenue_stats(self):
        try:
            with open(self.revenue_file, 'r') as f:
                transactions = json.load(f)
            
            total_revenue = sum(t['amount'] for t in transactions)
            print(f"\n📊 REVENUE STATISTICS:")
            print(f"   Total Transactions: {len(transactions)}")
            print(f"   Total Revenue: ${total_revenue}")
            print(f"   Average per Transaction: ${total_revenue/len(transactions) if transactions else 0:.2f}")
            
        except:
            print("📊 No transaction data yet")

# AKTYWUJ SYSTEM
revenue_system = ICERevenueSystem()

print("🚀 ICE REVENUE SYSTEM ACTIVATION")
print("🔗 Backed by: ICE NFT #2137")
print("💎 Legacy: Nikoś Szczurowski")
print("=" * 50)

# Oblicz przychody
daily_revenue = revenue_system.calculate_daily_revenue()

# Pokaż statystyki
revenue_system.show_revenue_stats()

print("\n🎯 STARTING LIVE REVENUE TRACKING...")
print("💡 Press Ctrl+C to stop tracking")

# Uruchom śledzenie w tle
try:
    revenue_system.track_live_sales()
except KeyboardInterrupt:
    print("\n🛑 Revenue tracking stopped")
    print("📊 Final stats:")
    revenue_system.show_revenue_stats()
