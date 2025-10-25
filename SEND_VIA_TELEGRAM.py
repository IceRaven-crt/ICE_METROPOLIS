import requests
import os

bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
file_path = "ICE_METROPOLIS_FINAL.zip"

url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
files = {'document': open(file_path, 'rb')}
data = {'chat_id': chat_id}

response = requests.post(url, files=files, data=data)
print("📤 Wysłano przez Telegram:", response.status_code)
