import sys
import os

# Dynamically add the root directory to sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

# Now, imports should work
from config.settings import VENDOR_PRICES
from src.fetch_price import fetch_item_prices
from src.check_price import check_prices

def main():
    """Run the Tarkov price tracker bot."""
    print("\n🔍 Checking Tarkov flea market prices...")
    items = fetch_item_prices()
    
    if items:
        check_prices(items)
    else:
        print("❌ No data received. Retrying in 10 minutes.")

if __name__ == "__main__":
    main()
