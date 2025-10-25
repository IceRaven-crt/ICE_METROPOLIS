#!/bin/bash
echo "🤖 FINALNA KONFIGURACJA TELEGRAM BOTA"
echo "======================================"

BOT_TOKEN="8363880640:AAEzGosrXpd15yUe2fh1yDIoda2dtwRwqMA"
BOT_USERNAME="@ICE_System_2025_Bot"

echo "✅ Bot utworzony: $BOT_USERNAME"
echo "📝 Wyślij teraz WIADOMOŚĆ do bota na Telegramie"
echo "⏳ Czekam 30 sekund..."
sleep 30

echo "🔍 Szukam Twojej wiadomości..."
for i in {1..6}; do
    echo "🔄 Sprawdzam... ($i/6)"
    RESPONSE=$(curl -s "https://api.telegram.org/bot$BOT_TOKEN/getUpdates")
    
    CHAT_INFO=$(echo "$RESPONSE" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    if data['ok'] and data['result']:
        latest = data['result'][-1]
        chat_id = latest['message']['chat']['id']
        first_name = latest['message']['chat'].get('first_name', 'ICE User')
        username = latest['message']['chat'].get('username', 'No username')
        print(f'{chat_id}:{first_name}:{username}')
    else:
        print('NO_MESSAGES')
except Exception as e:
    print(f'ERROR:{e}')
")
    
    if [[ "$CHAT_INFO" != "NO_MESSAGES" ]] && [[ "$CHAT_INFO" != ERROR* ]]; then
        break
    fi
    sleep 5
done

if [[ "$CHAT_INFO" == "NO_MESSAGES" ]] || [[ "$CHAT_INFO" == ERROR* ]]; then
    echo "❌ Nie znaleziono wiadomości."
    echo "💡 WYŚLIJ WIADOMOŚĆ do $BOT_USERNAME i uruchom ponownie: ./final_telegram_setup.sh"
    exit 1
fi

# Przetwórz dane
CHAT_ID=$(echo "$CHAT_INFO" | cut -d: -f1)
FIRST_NAME=$(echo "$CHAT_INFO" | cut -d: -f2)
USERNAME=$(echo "$CHAT_INFO" | cut -d: -f3)

echo "🎯 ZNALEZIONO: $FIRST_NAME (@$USERNAME)"
echo "💾 Chat ID: $CHAT_ID"

# Zapisz konfigurację
cat > ~/.ice_telegram_config << CONFIG
export TELEGRAM_BOT_TOKEN="$BOT_TOKEN"
export TELEGRAM_CHAT_ID="$CHAT_ID"
export TELEGRAM_BOT_USERNAME="$BOT_USERNAME"
CONFIG

source ~/.ice_telegram_config

echo "✅ KONFIGURACJA ZAPISANA W ~/.ice_telegram_config"

# Wyślij wiadomość powitalną
echo "📨 Wysyłam powitanie..."
curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
    -d chat_id="$TELEGRAM_CHAT_ID" \
    -d text="🧊 <b>ICE SYSTEM - BOT AKTYWNY!</b> 🚀

✅ Konfiguracja zakończona pomyślnie!
📊 Od teraz będziesz otrzymywać automatyczne raporty sukcesu
💰 Śledź wzrost swojego ICE Metropolis
⏰ Raporty: 08:00 i 20:00 codziennie

<b>Status: SYSTEM OPERATIONAL</b> 🎯" \
    -d parse_mode="HTML"

echo ""
echo "🎉 KONFIGURACJA ZAKOŃCZONA SUKCESEM!"
echo "🤖 Bot: $TELEGRAM_BOT_USERNAME"
echo "👤 Użytkownik: $FIRST_NAME (@$USERNAME)"
echo "💬 Chat ID: $TELEGRAM_CHAT_ID"
