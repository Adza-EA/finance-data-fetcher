# utils/fetch_news.py

import yfinance as yf

def get_latest_news(ticker):
    """
    Get recent news articles related to a company.

    Args:
        ticker (str): Stock ticker

    Returns:
        list: News headlines and summaries
    """
    stock = yf.Ticker(ticker)
    return stock.news  # returns a list of news dictionaries
