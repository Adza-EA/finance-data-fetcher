# main.py

from utils.fetch_stock import fetch_stock_data
from utils.fetch_info import get_company_info
from utils.fetch_financials import get_financial_statements
from utils.fetch_news import get_latest_news
from utils.fetch_options import get_options_data
from utils.export_data import export_to_excel

# Customize these values for different stocks and dates
TICKER = "AAPL"
START_DATE = "2023-01-01"
END_DATE = "2025-06-16"
INTERVAL = "1d"  # Options: '1d', '1wk', '1mo'
EXPIRY_DATE = None  # Optional: '2024-07-19'

# Fetch various data
stock_data = fetch_stock_data(TICKER, START_DATE, END_DATE, INTERVAL)
company_info = get_company_info(TICKER)
financials = get_financial_statements(TICKER)
news = get_latest_news(TICKER)
options = get_options_data(TICKER, EXPIRY_DATE)

# Combine exportable data
export_data = {
    "Stock_Data": stock_data,
    "Income_Statement": financials['income'],
    "Balance_Sheet": financials['balance'],
    "Cash_Flow": financials['cashflow'],
    "Options_Calls": options['calls'],
    "Options_Puts": options['puts']
}

# Export to Excel
export_to_excel(export_data, filename=f"{TICKER}_finance_data.xlsx")

# Optional: Print basic info
print(f"\n--- {TICKER} Company Info ---")
for key in ['longName', 'sector', 'industry', 'marketCap']:
    print(f"{key}: {company_info.get(key, 'N/A')}")

print(f"\nTop 3 news headlines for {TICKER}:")
for article in news[:3]:
    print(f"- {article['title']}")
