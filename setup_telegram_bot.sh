#!/bin/bash
# Konfiguracja Telegram Bot dla ICE raportów

echo "🤖 KONFIGURACJA TELEGRAM BOT DLA ICE SYSTEM"

# Sprawdź czy plik konfiguracyjny już istnieje
if [ ! -f ~/.ice_telegram_config ]; then
    echo "📝 Konfiguruję Telegram Bot..."
    
    echo "ℹ️  Instrukcja konfiguracji:"
    echo "1. Stwórz bota przez @BotFather na Telegram"
    echo "2. Zdobądź token bota"
    echo "3. Wyślij wiadomość do bota"
    echo "4. Zdobądź chat_id przez: https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates"
    
    read -p "🤖 Podaj Telegram Bot Token: " bot_token
    read -p "💬 Podaj Chat ID: " chat_id
    
    # Zapisz konfigurację
    cat > ~/.ice_telegram_config << CONFIG
export TELEGRAM_BOT_TOKEN="$bot_token"
export TELEGRAM_CHAT_ID="$chat_id"
CONFIG
    
    echo "✅ Konfiguracja Telegram zapisana w ~/.ice_telegram_config"
else
    echo "✅ Konfiguracja Telegram już istnieje"
    source ~/.ice_telegram_config
    echo "🤖 Bot Token: ${TELEGRAM_BOT_TOKEN:0:10}..."
    echo "💬 Chat ID: $TELEGRAM_CHAT_ID"
fi

# Dodaj do .bashrc lub .zshrc
if ! grep -q "ice_telegram_config" ~/.bashrc; then
    echo "source ~/.ice_telegram_config" >> ~/.bashrc
    echo "✅ Dodano do ~/.bashrc"
fi

echo "🎉 KONFIGURACJA ZAKOŃCZONA!"
