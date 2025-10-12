import requests
import os

BOT_TOKEN = "8363880640:AAEzGosrXpd15yUe2fh1yDIoda2dtwRwqMA"
CHAT_ID = "6535301121"  # Twój user ID, ale sprawdźmy czy to działa

print("🤖 ŁĄCZĘ Z BOTEM ICE_SYSTEM_2025...")

# Najpierw sprawdźmy bot
test_url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
test_response = requests.get(test_url)

if test_response.status_code == 200:
    bot_info = test_response.json()
    print(f"✅ Bot działa: {bot_info['result']['first_name']}")
    print(f"🔗 Username: @{bot_info['result']['username']}")
else:
    print("❌ Problem z botem:", test_response.text)
    exit()

# Sprawdźmy updates żeby znaleźć chat_id
updates_url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
updates_response = requests.get(updates_url)

if updates_response.status_code == 200:
    updates = updates_response.json()
    if updates['result']:
        chat_id = updates['result'][0]['message']['chat']['id']
        print(f"📨 Znaleziono chat_id: {chat_id}")
        CHAT_ID = chat_id
    else:
        print("ℹ️  Brak wiadomości - używam domyślnego chat_id")

print(f"📤 Wysyłam ICE_METROPOLIS do chat_id: {CHAT_ID}")

# Wyślij plik
file_path = "ICE_METROPOLIS_FINAL.zip"
if os.path.exists(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    files = {'document': open(file_path, 'rb')}
    data = {'chat_id': CHAT_ID, 'caption': '🧊 ICE_METROPOLIS - FULL SYSTEM DEPLOYMENT'}
    
    response = requests.post(url, files=files, data=data)
    
    if response.status_code == 200:
        print("🎉 PLIK WYSŁANY POPRAWNIE!")
        print("📦 Możesz go pobrać z Telegrama!")
    else:
        print("❌ Błąd wysyłania:", response.text)
else:
    print("❌ Plik nie istnieje:", file_path)
