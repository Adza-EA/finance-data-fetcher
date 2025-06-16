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
    news = stock.news or []
    return [n for n in news if isinstance(n, dict)]  # returns a list of news dictionaries
