#!/usr/bin/env python3
import datetime

class MilestoneCelebrations:
    def __init__(self):
        self.milestones = {
            1000000: "First $1 Million",
            5000000: "$5 Million Club", 
            10000000: "$10 Million Achieved",
            50000000: "$50 Million Milestone",
            100000000: "$100 Million - Centimillionaire",
            328500000: "Age 18 - Adult Wealth Access",
            500000000: "Half Billion Dollar Club",
            1000000000: "BILLIONAIRE STATUS"
        }
    
    def check_milestones(self, current_wealth):
        print("🎉 WEALTH MILESTONE CELEBRATIONS!")
        print("=" * 50)
        
        achieved = []
        upcoming = []
        
        for amount, description in self.milestones.items():
            if current_wealth >= amount:
                achieved.append((amount, description))
            else:
                upcoming.append((amount, description))
        
        if achieved:
            print("🏆 ACHIEVED MILESTONES:")
            for amount, desc in achieved:
                print(f"   ✅ {desc}: ${amount:,.2f}")
        
        if upcoming:
            print(f"\n🎯 UPCOMING MILESTONES:")
            for amount, desc in upcoming:
                needed = amount - current_wealth
                days_needed = needed / 50000  # przy $50k dziennie
                print(f"   🔜 {desc}")
                print(f"      Need: ${needed:,.2f} (~{days_needed:.1f} days)")
    
    def create_celebration_plan(self, current_wealth):
        print(f"\n🎊 CELEBRATION PLAN FOR ${current_wealth:,.2f}:")
        print("=" * 50)
        
        if current_wealth >= 1000000000:
            celebrations = [
                "Private Island Acquisition",
                "Space Tourism Experience",
                "Luxury Yacht World Tour",
                "Personal Jet for Global Education",
                "Foundation Launch Gala",
                "Family Museum of Legacy",
                "Tech Innovation Campus",
                "Global Philanthropy Tour"
            ]
        elif current_wealth >= 100000000:
            celebrations = [
                "World Travel Education Tour",
                "Private Tutor Dream Team",
                "Luxury Family Retreats",
                "Elite Sports Training",
                "Music & Arts Masterclasses",
                "Technology Lab Setup",
                "Language Immersion Programs",
                "Cultural Heritage Exploration"
            ]
        else:
            celebrations = [
                "Educational Theme Parks",
                "Science Museum Memberships",
                "Private Zoo & Aquarium Visits",
                "Interactive Learning Centers",
                "Sports Training Camps",
                "Art & Creativity Workshops",
                "Nature Exploration Expeditions",
                "Technology Building Blocks"
            ]
        
        for celebration in celebrations:
            print(f"   🎁 {celebration}")

# SPRAWDŹ KAMIEŃ MILOWE
milestones = MilestoneCelebrations()
current_wealth = 18250000  # Przykładowa wartość
milestones.check_milestones(current_wealth)
milestones.create_celebration_plan(current_wealth)
