import openpyxl
from data_fetcher import fetch_top_cryptos
import time
import schedule

# Initialize Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Crypto Data"

# Set headers in Excel sheet
headers = ["Name", "Symbol", "Price (USD)", "Market Cap", "24h Trading Volume", "Price Change (24h %)", "Last Updated"]
ws.append(headers)

def update_excel():
    data = fetch_top_cryptos()
    if data:
        for crypto in data:
            ws.append([
                crypto['name'],
                crypto['symbol'],
                crypto['current_price'],
                crypto['market_cap'],
                crypto['total_volume'],
                crypto['price_change_percentage_24h'],
                time.strftime("%Y-%m-%d %H:%M:%S")
            ])
        wb.save("CryptoData.xlsx")
        print("Excel sheet updated")

# Schedule the update every 5 minutes
schedule.every(5).minutes.do(update_excel)

if __name__ == "__main__":
    update_excel()  # Initial update
    while True:
        schedule.run_pending()
        time.sleep(1)
