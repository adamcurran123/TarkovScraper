# src/fetch_prices.py

import requests

API_URL = "https://api.tarkov.dev/graphql"

def fetch_item_prices():
    """Fetch item prices from Tarkov.dev GraphQL API."""
    query = """
    {
        items {
            name
            avg24hPrice
        }
    }
    """
    try:
        response = requests.post(API_URL, json={'query': query})
        response.raise_for_status()
        data = response.json()
        
        # Debugging: Log the entire response
        print(f"API Response: {data}")
        
        if 'errors' in data:
            print(f"GraphQL errors: {data['errors']}")
            return []
        
        items = data.get('data', {}).get('items', [])
        
        # Debugging: Log the number of items fetched
        print(f"Number of items fetched: {len(items)}")
        
        return items
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return []
    except ValueError as e:
        print(f"JSON Decoding Error: {e}")
        return []
