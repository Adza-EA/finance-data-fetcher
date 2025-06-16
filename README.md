# 📊 Finance Data Fetcher

A modular Python project for fetching and exporting comprehensive financial data using the [`yfinance`](https://pypi.org/project/yfinance/) library. Designed for beginners and finance/data enthusiasts, this tool makes it easy to collect stock prices, company details, financial statements, news, and options data—all in a few lines of code.

---

## 📂 Project Structure

finance-data-fetcher/
- ├── main.py 
- ├── requirements.txt
- ├── README.md 
- ├── .gitignore
- ├── LICENCE
- ├── utils/ 
- │ ├── init.py
- │ ├── fetch_stock.py
- │ ├── fetch_info.py
- │ ├── fetch_financials.py
- │ ├── fetch_news.py
- │ ├── fetch_options.py
- │ └── export_data.py
- └── sample_output/
- └── AAPL_finance_data.xlsx


---

## 🚀 Features

- 🔹 Fetch **historical stock prices** for any ticker
- 🔹 Retrieve **company information** such as sector, industry, and market cap
- 🔹 Download **financial statements**: income, balance sheet, and cash flow
- 🔹 Read the **latest news** headlines related to a company
- 🔹 Get **options chain data** including calls and puts
- 🔹 **Export everything to Excel** with multi-sheet support

---

## 🛠️ Setup & Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/finance-data-fetcher.git
   cd finance-data-fetcher

2. **Install required packages**
   ```bash
   pip install -r requirements.txt

3. ***Run the main script***
   ```bash
   python main.py

4. ***Check the output***
The Excel file (e.g., AAPL_finance_data.xlsx) will be saved in the root directory or sample_output/.



## 📌 Customization Guide
You can edit the variables at the top of main.py:

    ```python
    TICKER = "AAPL"                  # Change to your desired stock symbol
    START_DATE = "2023-01-01"        # Historical data start
    END_DATE = "2025-06-16"          # Historical data end
    INTERVAL = "1d"                  # '1d', '1wk', or '1mo'
    EXPIRY_DATE = None               # Optional: e.g., '2024-07-19'


***📦 Requirements***
Python 3.7+

Packages:
yfinance
pandas
openpyxl

All dependencies can be installed using:

    ```bash
    pip install -r requirements.txt


## 🧠 How It Works
Each function is modular and stored inside the utils/ folder:

File	Description
fetch_stock.py	         Fetch historical stock data
fetch_info.py        	Get company metadata
fetch_financials.py	   Retrieve financial statements
fetch_news.py	Load     latest news about the company
fetch_options.py     	Get options chain data
export_data.py       	Export data to Excel

You can import and use them independently or run everything via main.py.

## 📤 Example Output
The exported Excel file includes multiple sheets like:

Stock_Data
Income_Statement
Balance_Sheet
Cash_Flow
Options_Calls
Options_Puts

Check the sample_output/ folder to see example files.

## 🤝 Contributing
Have an idea to improve this tool (e.g., add charts, web app, or database export)?
Feel free to fork this repo and submit a pull request!

📄 License
This project is open-source and available under the MIT License.

🙌 Acknowledgments
Yahoo Finance API via yFinance
Open-source community for tools and support
