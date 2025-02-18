# src/verify_item_names.py

import requests

API_URL = "https://tarkov.dev/api/v2/items"

def fetch_item_names():
    """Fetch and print all item names from the Tarkov.dev API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        items = response.json().get("data", [])
        for item in items:
            print(item.get("name"))
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_item_names()
