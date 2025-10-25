#!/bin/bash
echo "📱 FINALNA KONFIGURACJA TELEGRAM"

# Poproś użytkownika o chat_id
read -p "🤖 Podaj Twój Chat ID z Telegram: " CHAT_ID

if [ -n "$CHAT_ID" ]; then
    # Zapisz konfigurację
    cat > ~/.ice_telegram_config << CONFIG
export TELEGRAM_BOT_TOKEN="8363880640:AAEzGosrXpd15yUe2fh1yDIoda2dtwRwqMA"
export TELEGRAM_CHAT_ID="$CHAT_ID"
CONFIG
    
    source ~/.ice_telegram_config
    echo "✅ Konfiguracja zapisana!"
    echo "🤖 Bot: @ICE_System_2025_Bot"
    echo "💬 Chat ID: $CHAT_ID"
    
    # Test wysyłki
    echo "🧪 Testuję wysyłkę wiadomości..."
    curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
        -d chat_id="$TELEGRAM_CHAT_ID" \
        -d text="🧊 ICE System Test - Konfiguracja udana! ✅" \
        -d parse_mode="HTML"
        
    echo "🎉 KONFIGURACJA ZAKOŃCZONA!"
else
    echo "❌ Nie podano Chat ID"
fi
