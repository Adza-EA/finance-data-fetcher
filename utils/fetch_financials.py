# utils/fetch_financials.py

import yfinance as yf

def get_financial_statements(ticker):
    """
    Get income statement, balance sheet, and cash flow statement.

    Args:
        ticker (str): Stock ticker

    Returns:
        dict: Dictionary with 'income', 'balance', and 'cashflow' DataFrames
    """
    stock = yf.Ticker(ticker)
    return {
        'income': stock.financials,
        'balance': stock.balance_sheet,
        'cashflow': stock.cashflow
    }
