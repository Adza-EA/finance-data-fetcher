# utils/fetch_stock.py

import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date, interval='1d'):
    """
    Fetch historical stock data using yfinance.

    Args:
        ticker (str): Stock ticker (e.g., 'AAPL')
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format
        interval (str): Data frequency ('1d', '1wk', '1mo')

    Returns:
        pd.DataFrame: Stock price data
    """
    df = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        interval=interval,
        auto_adjust=True,
        progress=False
    )
    return df
