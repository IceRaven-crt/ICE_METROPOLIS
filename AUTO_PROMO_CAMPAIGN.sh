#!/bin/bash
echo "📡 URuchamiam automatyczną kampanię promocyjną..."

# Generuję gotowe materiały promocyjne
cat > PROMO_MATERIALS/LAUNCH_ANNOUNCEMENT.md << 'ANNOUNCE'
# 🚀 OFFICIAL LAUNCH: ICE METROPOLIS + GENESIS BLOCK 002

## 🌐 LIVE SYSTEM: 
https://68ec129ea66cd52eff4e577a--ice-metropolis-1760301724.netlify.app

## 🏷️ GENESIS BLOCK 002 FEATURES:
- Full Web3 Integration
- Crypto Payments Ready
- NFT Collection
- Digital Legacy System
- Professional Dashboard

## 👤 AUTHOR:
Paweł Szczurowski / ICE_RAVEN

## 👶 LEGACY HEIR:
Nikoś

## 🎯 MISSION:
Building digital inheritance and Web3 solutions for future generations.

## 🔗 QUICK ACCESS:
- Live Site: [NETLIFY_URL]
- Genesis Block: [GENESIS_URL]
- NFT Collection: [OPENSEA_URL]

#ICE_METROPOLIS #Web3 #NFT #Crypto #DigitalLegacy
ANNOUNCE

# Tworzę skrypt auto-posting
cat > SOCIAL_AUTO_POST.py << 'SOCIAL'
import datetime

print("🧊 SOCIAL MEDIA AUTO-POSTING SCRIPT")
print("=====================================")

posts = [
    {
        'platform': 'Twitter',
        'content': '''🚀 LAUNCHED: ICE METROPOLIS - Full Web3 System Online!

🌐 Live: https://68ec129ea66cd52eff4e577a--ice-metropolis-1760301724.netlify.app
🏷️ Genesis Block 002 NFT - Limited 1/1
👶 Digital legacy for my son Nikoś

#ICE_METROPOLIS #Web3 #NFT #Crypto''',
        'hashtags': '#Web3 #NFT #Crypto #DigitalLegacy'
    },
    {
        'platform': 'Telegram',
        'content': '''🧊 OFFICIAL ANNOUNCEMENT:

ICE METROPOLIS system is now LIVE!

Features:
• Web3 Dashboard with wallet integration
• Crypto payments (Bitcomat ready)
• NFT Collection - Genesis Block 002
• Digital inheritance system

Live: https://68ec129ea66cd52eff4e577a--ice-metropolis-1760301724.netlify.app

Author: Paweł Szczurowski / ICE_RAVEN
Heir: Nikoś 👶''',
        'hashtags': ''
    }
]

for post in posts:
    print(f"\n📮 {post['platform']} POST:")
    print("---")
    print(post['content'])
    print(f"{post['hashtags']}")
    print("---")

print(f"\n✅ Ready to post on {len(posts)} platforms")
print("💡 Copy & paste these to your social media!")
SOCIAL

python3 SOCIAL_AUTO_POST.py

echo "✅ MODUŁ 2 AKTYWNY - materiały promocyjne gotowe!"
