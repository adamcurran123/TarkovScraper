# src/notify.py

import requests
from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_message(message):
    """Send a message to the specified Telegram chat."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Telegram notification sent successfully.")
    except requests.RequestException as e:
        print(f"Failed to send Telegram message: {e}")
