# Cryptocurrency Analysis Project

## **Project Overview**

This project fetches live cryptocurrency data for the top 50 cryptocurrencies, performs basic analysis, and provides a live-updating Excel sheet with the data. Additionally, it generates an analysis report summarizing key insights.


---

## **Folder Structure**

```
crypto_analysis/
|
├── data_fetcher.py          # Script to fetch live cryptocurrency data
├── data_analysis.py         # Script to analyze the fetched data
├── live_updating_excel.py   # Script to create and update a live Excel sheet
├── analysis_report.py       # Script to generate a PDF report
├── requirements.txt         # File with all required Python libraries
├── CryptoData.xlsx          # Live-updating Excel sheet (auto-generated)
├── analysis_report.pdf      # PDF report (auto-generated)
└── README.md                # Documentation for the project
```


---

## **Setup Instructions**

### **1. Prerequisites**

Ensure you have the following installed:

* Python 3.8 or later
* pip (Python package manager)

### **2. Create Virtual Environment**

Run the following commands to set up the environment:

```bash
mkdir crypto_analysis && cd crypto_analysis
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, use the following:

```bash
pip install requests openpyxl schedule reportlab
```


---

## **Testing Instructions**

### **1. Fetch Cryptocurrency Data**

Run the `data_fetcher.py` script to fetch live cryptocurrency data:

```bash
python data_fetcher.py
```

**Expected Output:**

* A JSON-like list of the top 50 cryptocurrencies showing fields like `name`, `symbol`, `current_price`, `market_cap`, etc.

### **2. Analyze Cryptocurrency Data**

Run the `data_analysis.py` script to perform analysis:

```bash
python data_analysis.py
```

**Expected Output:**

* List of the top 5 cryptocurrencies by market cap.
* Average price of the top 50 cryptocurrencies.
* Highest and lowest 24-hour price change.

### **3. Live-Updating Excel Sheet**

Run the `live_updating_excel.py` script to generate the live Excel sheet:

```bash
python live_updating_excel.py
```


1. Open the generated file `CryptoData.xlsx`.
2. Verify that it contains live data for the top 50 cryptocurrencies.
3. Wait for 5 minutes (or as per the interval set in the code) and confirm the data updates.

**Optional:** For faster testing, change the update interval in the script to 1 minute:

```python
schedule.every(1).minutes.do(update_excel)
```

### **4. Generate PDF Analysis Report**

Run the `analysis_report.py` script to generate the report:

```bash
python analysis_report.py
```

**Expected Output:**

* A PDF file named `analysis_report.pdf` containing:
  * Top 5 cryptocurrencies by market cap.
  * Average price.
  * Highest and lowest 24-hour price change.

Open the PDF to verify:

```bash
xdg-open analysis_report.pdf  # Linux
open analysis_report.pdf      # macOS
start analysis_report.pdf     # Windows
```

### **5. Test Background Execution for Live Excel Updates**

Run the Excel script in the background:

```bash
nohup python live_updating_excel.py &
```

Check if the script is running:

```bash
ps aux | grep live_updating_excel.py
```

To stop the background script:

```bash
pkill -f live_updating_excel.py
```


---

## **Submission Instructions**


1. **Package the Project:**
   Create a zip file of the project directory:

```bash
zip -r crypto_analysis.zip .
```


2. **Upload Excel File:**
   Share the `CryptoData.xlsx` file by uploading it to a cloud service (e.g., Google Drive) and generating a shareable link.
3. **Submit PDF Report:**
   Include the `analysis_report.pdf` in your submission.


---

## **Notes**

* Ensure your system is connected to the internet while running the scripts.
* Make sure to configure the update interval in the `live_updating_excel.py` script as needed.
* If you encounter errors, check the API limits of the data source or verify your Python dependencies.


---

For any questions or troubleshooting, feel free to reach out to @chirag