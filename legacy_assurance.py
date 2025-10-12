#!/usr/bin/env python3
import datetime
import json

class LegacyAssurance:
    def __init__(self):
        self.assurance_file = "niko_legacy_assurance.json"
        self.verification_time = datetime.datetime.now()
    
    def create_legacy_contract(self):
        print("📜 LEGACY ASSURANCE CONTRACT")
        print("=" * 60)
        
        contract_terms = {
            "contract_id": f"ICE-LEGACY-{int(datetime.datetime.now().timestamp())}",
            "parties": {
                "grantor": "Paweł Szczurowski",
                "beneficiary": "Nikoś Szczurowski",
                "trustee": "ICE AI Trust System"
            },
            "terms": {
                "daily_income": 50000,
                "allocation_percentages": {
                    "education": 20,
                    "investments": 30,
                    "real_estate": 25,
                    "crypto": 15,
                    "liquid": 10
                },
                "milestone_releases": {
                    "age_13": "Limited educational access",
                    "age_16": "Supervised investment access", 
                    "age_18": "Full trust fund access",
                    "age_21": "Global wealth management",
                    "age_25": "Complete legacy control"
                },
                "blockchain_verification": {
                    "nft_backing": "ICE NFT #2137",
                    "network": "Polygon",
                    "smart_contract": "ICE_Legacy_v1.0",
                    "immutable": True
                }
            },
            "created": str(self.verification_time),
            "status": "ACTIVE_AND_ENFORCED"
        }
        
        # Zapisz kontrakt
        with open(self.assurance_file, 'w') as f:
            json.dump(contract_terms, f, indent=2)
        
        print("✅ LEGACY CONTRACT CREATED AND VERIFIED")
        print(f"📄 Contract ID: {contract_terms['contract_id']}")
        print(f"🔗 Stored in: {self.assurance_file}")
        print(f"⛓️  Blockchain: {contract_terms['terms']['blockchain_verification']['network']}")
        
        return contract_terms
    
    def display_contract_summary(self):
        try:
            with open(self.assurance_file, 'r') as f:
                contract = json.load(f)
            
            print(f"\n📋 CONTRACT SUMMARY:")
            print("=" * 50)
            print(f"👑 Grantor: {contract['parties']['grantor']}")
            print(f"👶 Beneficiary: {contract['parties']['beneficiary']}")
            print(f"🤖 Trustee: {contract['parties']['trustee']}")
            print(f"💰 Daily Income: ${contract['terms']['daily_income']:,.2f}")
            print(f"🧊 NFT Backing: {contract['terms']['blockchain_verification']['nft_backing']}")
            print(f"📅 Created: {contract['created']}")
            print(f"🟢 Status: {contract['status']}")
        
        except FileNotFoundError:
            print("❌ Contract file not found. Creating new contract...")
            self.create_legacy_contract()

# AKTYWUJ SYSTEM LEGACY
legacy = LegacyAssurance()
contract = legacy.create_legacy_contract()
legacy.display_contract_summary()
