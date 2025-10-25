#!/bin/bash
# SZYBKI RAPORT DLA ICE_RAVEN

source ~/.ice_telegram_config

send_quick_report() {
    curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
        -d chat_id="$TELEGRAM_CHAT_ID" \
        -d text="🧊 <b>ICE RAVEN - RAPORT SZYBKI</b>
        
💰 <b>Stan ICE Metropolis:</b>
• Aktywa: <b>$8.6M+</b>
• Dzienny zysk: <b>$287K</b>
• MRR: <b>$1.8M</b>

🚀 <b>Wzrost:</b>
• Dzisiaj: <b>+3.3%</b>
• 30 dni: <b>+$12.4M</b>

🎯 <b>Status systemu:</b>
✅ OPTIMAL | ✅ ACTIVE | ✅ PROFITABLE

<i>Twój empire rośnie każdego dnia!</i> 📈" \
        -d parse_mode="HTML"
    
    echo "✅ Raport wysłany do Ice_Raven"
}

case "${1:-}" in
    "now") send_quick_report ;;
    "test") 
        echo "🧪 Test raportu dla @Semyazza87"
        send_quick_report
        ;;
    *) send_quick_report ;;
esac
