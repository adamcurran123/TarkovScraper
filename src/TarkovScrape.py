import sys
import os
import time

# 🚀 Ensure the project root is added to Python's path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from config.settings import VENDOR_PRICES
from fetch_price import fetch_item_prices
from check_price import check_prices

def main():
    """Continuously run the Tarkov price tracker bot every 10 minutes."""
    print("\n🚀 Tarkov Price Tracker is starting...")
    
    while True:  # Runs indefinitely
        print("\n🔍 Checking Tarkov flea market prices...")
        items = fetch_item_prices()

        if items:
            check_prices(items)
        else:
            print("❌ No data received. Retrying in 10 minutes.")

        print("⏳ Waiting 10 minutes before checking again...\n")
        time.sleep(600)  # Wait for 600 seconds (10 minutes)

if __name__ == "__main__":
    main()
