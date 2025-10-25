#!/bin/bash
echo "🤖 AUTOMATYCZNE POBIERANIE CHAT_ID"
echo "📝 Wyślij teraz wiadomość do: @ICE_System_2025_Bot"
echo "⏳ Czekam 60 sekund..."

for i in {1..12}; do
    echo "⏰ Sprawdzam wiadomości... ($i/12)"
    RESPONSE=$(curl -s "https://api.telegram.org/bot8363880640:AAEzGosrXpd15yUe2fh1yDIoda2dtwRwqMA/getUpdates")
    
    if echo "$RESPONSE" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    if data['ok'] and data['result']:
        latest = data['result'][-1]
        chat_id = latest['message']['chat']['id']
        first_name = latest['message']['chat'].get('first_name', 'User')
        print(f'SUCCESS:{chat_id}:{first_name}')
        sys.exit(0)
    else:
        print('WAITING')
        sys.exit(1)
except:
    print('ERROR')
    sys.exit(2)
"; then
        break
    fi
    sleep 5
done

# Przetwórz wynik
RESULT=$(echo "$RESPONSE" | python3 -c "
import json, sys
data = json.load(sys.stdin)
if data['ok'] and data['result']:
    latest = data['result'][-1]
    chat_id = latest['message']['chat']['id']
    first_name = latest['message']['chat'].get('first_name', 'User')
    print(f'{chat_id}:{first_name}')
")

if [ -n "$RESULT" ]; then
    CHAT_ID=$(echo $RESULT | cut -d: -f1)
    NAME=$(echo $RESULT | cut -d: -f2)
    
    echo "🎯 ZNALEZIONO: $NAME (Chat ID: $CHAT_ID)"
    
    # Zapisz konfigurację
    cat > ~/.ice_telegram_config << CONFIG
export TELEGRAM_BOT_TOKEN="8363880640:AAEzGosrXpd15yUe2fh1yDIoda2dtwRwqMA"
export TELEGRAM_CHAT_ID="$CHAT_ID"
CONFIG
    
    source ~/.ice_telegram_config
    echo "✅ KONFIGURACJA ZAPISANA!"
    
    # Wyślij potwierdzenie
    curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
        -d chat_id="$TELEGRAM_CHAT_ID" \
        -d text="🎉 ICE System - Konfiguracja udana! Otrzymasz teraz automatyczne raporty sukcesu! 🧊🚀" \
        -d parse_mode="HTML"
        
    echo "📨 Wysłano potwierdzenie na Telegram!"
else
    echo "❌ Nie znaleziono wiadomości. Spróbuj ponownie."
fi
