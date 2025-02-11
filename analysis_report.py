from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(analysis):
    c = canvas.Canvas("analysis_report.pdf", pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 12)
    c.drawString(100, height - 50, "Cryptocurrency Data Analysis Report")

    c.drawString(100, height - 80, f"Top 5 Cryptocurrencies by Market Cap:")
    y_pos = height - 100
    for i, crypto in enumerate(analysis['top_5']):
        c.drawString(100, y_pos, f"{i + 1}. {crypto['name']} - {crypto['symbol']} - Market Cap: {crypto['market_cap']}")
        y_pos -= 20

    c.drawString(100, y_pos, f"\nAverage Price of Top 50 Cryptos: ${analysis['average_price']:.2f}")
    y_pos -= 20
    c.drawString(100, y_pos, f"Highest 24h Price Change: {analysis['highest_change']:.2f}%")
    y_pos -= 20
    c.drawString(100, y_pos, f"Lowest 24h Price Change: {analysis['lowest_change']:.2f}%")

    c.save()

if __name__ == "__main__":
    from data_analysis import analyze_data
    from data_fetcher import fetch_top_cryptos

    data = fetch_top_cryptos()
    analysis = analyze_data(data)
    generate_report(analysis)
