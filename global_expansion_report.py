#!/usr/bin/env python3
"""
ICE Global Expansion Status
Raport postępów międzynarodowych
"""

class GlobalExpansionReport:
    def generate_expansion_status(self):
        regions = {
            "NORTH_AMERICA": {
                "status": "🟢 ACTIVE",
                "revenue": "$500K/month",
                "clients": "45+",
                "team_size": "15",
                "next_target": "Fortune 100 companies"
            },
            "EUROPE": {
                "status": "🟡 DEPLOYING", 
                "revenue": "$300K/month (projected)",
                "clients": "25+",
                "team_size": "8",
                "next_target": "EU institutions"
            },
            "ASIA_PACIFIC": {
                "status": "🟡 DEPLOYING",
                "revenue": "$400K/month (projected)",
                "clients": "35+", 
                "team_size": "12",
                "next_target": "Tech giants"
            },
            "MIDDLE_EAST": {
                "status": "🟠 PLANNING",
                "revenue": "$200K/month (projected)",
                "clients": "15+",
                "team_size": "5",
                "next_target": "Sovereign funds"
            }
        }
        
        print("🌍 STATUS EKSPANSJI GLOBALNEJ:")
        print("==============================")
        
        active_regions = 0
        total_revenue = 0
        
        for region, details in regions.items():
            print(f"\n📍 {region.replace('_', ' ').title()}:")
            print(f"   🎯 Status: {details['status']}")
            print(f"   💰 Revenue: {details['revenue']}")
            print(f"   👥 Clients: {details['clients']}")
            print(f"   🧑‍💼 Team: {details['team_size']} people")
            print(f"   🎯 Next Target: {details['next_target']}")
            
            if "ACTIVE" in details['status']:
                active_regions += 1
            
            # Extract revenue numbers
            rev_str = details['revenue'].replace('$', '').replace('K', '000').replace('M', '000000').split(' ')[0]
            try:
                rev_num = float(rev_str)
                total_revenue += rev_num
            except:
                pass
        
        print(f"\n📈 PODSUMOWANIE EKSPANSJI:")
        print(f"   🗺️  Active Regions: {active_regions}/{len(regions)}")
        print(f"   💰 Total Revenue: ${total_revenue:,.2f}/month")
        print(f"   🚀 Projection: $1.4M/month when fully deployed")
        
        return regions

if __name__ == "__main__":
    expansion = GlobalExpansionReport()
    expansion.generate_expansion_status()
