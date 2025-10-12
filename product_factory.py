#!/usr/bin/env python3
import os
import datetime
import json

class ICEProductFactory:
    def __init__(self):
        self.products_dir = "ice_products"
        os.makedirs(self.products_dir, exist_ok=True)
    
    def create_digital_product(self, name, price, description):
        product_id = f"ICE_{int(datetime.datetime.now().timestamp())}"
        product_dir = f"{self.products_dir}/{product_id}"
        os.makedirs(product_dir, exist_ok=True)
        
        # Tworzenie plików produktu
        files = {
            "README.md": f"# {name}\n\n{description}\n\nPrice: ${price}\n\nICE NFT Backed: #2137",
            "LICENSE.txt": "Commercial License - ICE System\nLegacy: Nikoś Szczurowski",
            "MANIFEST.json": json.dumps({
                "name": name,
                "price": price,
                "description": description,
                "created": str(datetime.datetime.now()),
                "ice_nft": "#2137",
                "author": "Paweł Szczurowski"
            }, indent=2)
        }
        
        for filename, content in files.items():
            with open(f"{product_dir}/{filename}", "w") as f:
                f.write(content)
        
        print(f"✅ Created: {name} (${price}) - ID: {product_id}")
        return product_id

# STWÓRZ PRODUKTY AUTOMATYCZNIE
factory = ICEProductFactory()

products_to_create = [
    ("AI Automation Suite", 297, "Complete AI automation package"),
    ("Blockchain Smart Contracts", 497, "Ready-to-deploy smart contracts"),
    ("Digital Marketing Pack", 197, "Marketing automation tools"),
    ("Mobile App Templates", 397, "Premium mobile app templates")
]

print("🏭 ICE PRODUCT FACTORY ACTIVATED")
for name, price, desc in products_to_create:
    factory.create_digital_product(name, price, desc)

print(f"\n🎯 Products ready for sale!")
print("💎 All products backed by ICE NFT #2137")
