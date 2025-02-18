# src/check_prices.py

from config.settings import VENDOR_PRICES
from notify import send_telegram_message

def check_prices(items):
    """Compare fetched prices to vendor prices and send alerts for profitable items."""
    for item in items:
        name = item.get("name")
        flea_price = item.get("avg24hPrice", 0)
        vendor_price = VENDOR_PRICES.get(name)
        if vendor_price and flea_price < vendor_price:
            message = (
                f"ALERT: '{name}' is selling for {flea_price}₽ on the flea market, "
                f"below the vendor price of {vendor_price}₽."
            )
            print(message)
            send_telegram_message(message)
