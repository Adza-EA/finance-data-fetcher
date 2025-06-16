# utils/fetch_info.py

import yfinance as yf

def get_company_info(ticker):
    """
    Fetch company metadata such as name, sector, market cap, etc.

    Args:
        ticker (str): Stock ticker

    Returns:
        dict: Company information
    """
    stock = yf.Ticker(ticker)
    return stock.info  # returns a Python dictionary
