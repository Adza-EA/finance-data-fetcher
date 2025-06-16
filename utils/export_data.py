# utils/export_data.py

import pandas as pd

def export_to_excel(data, filename='output.xlsx'):
    """
    Export one or more pandas DataFrames to Excel.

    Args:
        data (dict or pd.DataFrame): If dict, each key becomes a sheet.
        filename (str): Output Excel file name

    Returns:
        None
    """
    if isinstance(data, dict):
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            for sheet, df in data.items():
                df.to_excel(writer, sheet_name=sheet)
    elif isinstance(data, pd.DataFrame):
        data.to_excel(filename, index=True)
    else:
        raise ValueError("Input must be a DataFrame or a dictionary of DataFrames.")
