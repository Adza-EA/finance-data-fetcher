# utils/fetch_options.py

import yfinance as yf

def get_options_data(ticker, expiry_date=None):
    """
    Get options chain data.

    Args:
        ticker (str): Stock ticker
        expiry_date (str, optional): Specific expiration date ('YYYY-MM-DD')

    Returns:
        dict: Call and put options data as DataFrames
    """
    stock = yf.Ticker(ticker)
    if expiry_date is None:
        expiry_date = stock.options[0]  # use earliest expiry available

    opt_chain = stock.option_chain(expiry_date)
    return {
        'calls': opt_chain.calls,
        'puts': opt_chain.puts
    }
