#!/usr/bin/env python3
"""
Automatyczny System Tzedaki - 10% dla Hashem
"""

class SystemTzedaki:
    def __init__(self):
        self.dochody = {
            'miesieczny': 83333333333,  # $83.3B/miesiąc
            'dzienny': 2739726027,      # $2.74B/dzień
            'godzinowy': 114155251      # $114M/godzinę
        }
        self.maaser_percent = 10
        
    def oblicz_automatyczna_tzedake(self):
        print("💰 AUTOMATYCZNY SYSTEM TZEDAKI:")
        print("=" * 50)
        
        tzedaka = {
            'miesieczna': self.dochody['miesieczny'] * (self.maaser_percent / 100),
            'dzienna': self.dochody['dzienny'] * (self.maaser_percent / 100),
            'godzinowa': self.dochody['godzinowy'] * (self.maaser_percent / 100)
        }
        
        print(f"📊 MIESIĘCZNA TZEDAKA: ${tzedaka['miesieczna']:,.0f}")
        print(f"📅 DZIENNA TZEDAKA: ${tzedaka['dzienna']:,.0f}") 
        print(f"⏰ GODZINOWA TZEDAKA: ${tzedaka['godzinowa']:,.0f}")
        
        return tzedaka
    
    def stworz_kategorie_tzedaki(self):
        print("\n🎯 KATEGORIE TZEDAKI:")
        
        kategorie = {
            "TORA_EDUKACJA": {
                "percent": 30,
                "opis": "Jesziwy, szkoły, publikacje Tory"
            },
            "POMOC_SPOLECZNA": {
                "percent": 25, 
                "opis": "Jedzenie, mieszkania, opieka medyczna"
            },
            "TIKKUN_OLAM": {
                "percent": 20,
                "opis": "Ekologia, zrównoważony rozwój, pokój"
            },
            "KULTURA_ZYDOWSKA": {
                "percent": 15,
                "opis": "Sztuka, muzea, festiwale żydowskie"
            },
            "BADANIA": {
                "percent": 10,
                "opis": "Nauka, medycyna, technologie"
            }
        }
        
        for kat, details in kategorie.items():
            print(f"   ✅ {kat}: {details['percent']}% - {details['opis']}")
            
        return kategorie

if __name__ == "__main__":
    system = SystemTzedaki()
    tzedaka = system.oblicz_automatyczna_tzedake()
    system.stworz_kategorie_tzedaki()
    
    print(f"\n🕍 SYSTEM TZEDAKI: AKTYWNY")
    print("📜 'Maaser będziecie oddawać' (Dewarim 14:22)")
