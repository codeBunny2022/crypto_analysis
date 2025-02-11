import statistics

def analyze_data(crypto_data):
    # Sort by market capitalization
    sorted_data = sorted(crypto_data, key=lambda x: x['market_cap'], reverse=True)

    # Top 5 cryptocurrencies
    top_5 = sorted_data[:5]

    # Calculate the average price of the top 50
    avg_price = statistics.mean([crypto['current_price'] for crypto in crypto_data])

    # Find highest and lowest 24-hour price change
    price_changes = [crypto['price_change_percentage_24h'] for crypto in crypto_data]
    highest_change = max(price_changes)
    lowest_change = min(price_changes)

    return {
        "top_5": top_5,
        "average_price": avg_price,
        "highest_change": highest_change,
        "lowest_change": lowest_change
    }

if __name__ == "__main__":
    # Fetch data (from data_fetcher.py)
    from data_fetcher import fetch_top_cryptos
    data = fetch_top_cryptos()
    
    if data:
        analysis = analyze_data(data)
        print("Top 5 Cryptos:", analysis['top_5'])
        print("Average Price of Top 50 Cryptos:", analysis['average_price'])
        print("Highest 24h Price Change:", analysis['highest_change'])
        print("Lowest 24h Price Change:", analysis['lowest_change'])
