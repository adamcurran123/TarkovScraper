import requests
from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_message(item_name, flea_price, vendor_price):
    """Send a formatted notification to Telegram when a price drops below vendor value."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    # ✅ Add emojis & formatting
    message = (
        f"🛒 **DEAL ALERT!**\n"
        f"🔹 **Item:** `{item_name}`\n"
        f"💰 **Flea Market Price:** `{flea_price:,}₽`\n"
        f"🏪 **Vendor Buy Price:** `{vendor_price:,}₽`\n"
        f"🔥 **Profit Potential:** `{vendor_price - flea_price:,}₽` 🚀"
    )

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"  # ✅ Allows bold text
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise error for bad responses
        print("✅ Telegram notification sent.")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP Error: {http_err}")
        print(f"Response Text: {response.text}")  # Print full response from Telegram
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Request Error: {req_err}")
