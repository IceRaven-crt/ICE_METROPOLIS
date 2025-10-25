import requests
import os

print("🤖 SPRAWDZAMY TELEGRAM BOT...")

# Sprawdź czy plik istnieje
file_path = "ICE_METROPOLIS_FINAL.zip"
if not os.path.exists(file_path):
    print("❌ Plik nie istnieje:", file_path)
    exit()

print(f"📦 Znaleziono plik: {file_path} ({os.path.getsize(file_path)} bajtów)")

# TEST - najpierw sprawdźmy czy bot działa
test_url = "https://api.telegram.org/botYOUR_BOT_TOKEN/getMe"
test_response = requests.get(test_url)
print(f"🔧 Test bota: {test_response.status_code}")

if test_response.status_code == 200:
    print("✅ Bot działa poprawnie!")
    
    # Teraz wyślij plik
    url = f"https://api.telegram.org/botYOUR_BOT_TOKEN/sendDocument"
    files = {'document': open(file_path, 'rb')}
    data = {'chat_id': 'YOUR_CHAT_ID'}
    
    response = requests.post(url, files=files, data=data)
    print(f"📤 Status wysyłania: {response.status_code}")
    
    if response.status_code == 200:
        print("🎉 PLIK WYSŁANY POPRAWNIE!")
        print("📋 Odpowiedź:", response.json())
    else:
        print("❌ Błąd wysyłania:", response.text)
else:
    print("❌ Problem z botem:", test_response.text)

print("\n🔍 PROBLEM MOŻE BYĆ:")
print("1. Zły BOT_TOKEN")
print("2. Zły CHAT_ID") 
print("3. Bot nie ma uprawnień")
print("4. Problem z siecią")
