from config.settings import VENDOR_PRICES
from src.notify import send_telegram_message

def check_prices(items):
    """Compare flea market prices to vendor prices and send alerts if under vendor price."""
    for item in items:
        name = item.get("name")
        flea_price = item.get("avg24hPrice")  # Get 24-hour average price

        if flea_price is None:
            print(f"⚠️ Skipping '{name}' - No price data available.")
            continue  # Skip items without valid pricing

        if name in VENDOR_PRICES and flea_price < VENDOR_PRICES[name]:
            vendor_price = VENDOR_PRICES[name]
            
            # ✅ Print formatted message in terminal
            print(f"🚨 '{name}' is only {flea_price:,}₽ but sells for {vendor_price:,}₽!")

            # ✅ Send formatted alert to Telegram
            send_telegram_message(name, flea_price, vendor_price)
