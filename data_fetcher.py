import requests

# CoinGecko API endpoint
URL = 'https://api.coingecko.com/api/v3/coins/markets'

# Parameters to get top 50 by market cap
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 50,
    'page': 1,
    'sparkline': 'false'
}

def fetch_top_cryptos():
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return []

if __name__ == "__main__":
    data = fetch_top_cryptos()
    print(data)  # Print the raw data for debugging
