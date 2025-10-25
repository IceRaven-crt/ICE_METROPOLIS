#!/bin/bash
echo "🔧 POPRAWIAM KONFIGURACJĘ TELEGRAM..."

# Prawidłowy format konfiguracji
cat > ~/.ice_telegram_config << CONFIG
export TELEGRAM_BOT_TOKEN="8363880640:AAEzGosrXpd15yUe2fh1yDIoda2dtwRwqMA"
export TELEGRAM_CHAT_ID="123456789"  # To musisz zastąpić prawdziwym chat_id
CONFIG

echo "✅ Skonfigurowano z przykładowymi danymi"
echo "ℹ️  Aby uzyskać chat_id:"
echo "1. Wyślij wiadomość do @ICE_System_2025_Bot"
echo "2. Odwiedź: https://api.telegram.org/bot8363880640:AAEzGosrXpd15yUe2fh1yDIoda2dtwRwqMA/getUpdates"
echo "3. Znajdź 'chat' -> 'id' w odpowiedzi JSON"
echo "4. Zastąp '123456789' prawdziwym chat_id w ~/.ice_telegram_config"
