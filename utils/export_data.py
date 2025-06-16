# utils/export_data.py

import pandas as pd

def export_to_excel(data_dict, filename='output.xlsx'):
    """
    Export multiple DataFrames to different sheets in an Excel file.

    Args:
        data_dict (dict): Dictionary of {sheet_name: DataFrame}
        filename (str): Output Excel file name
    """
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        for sheet_name, df in data_dict.items():
            if isinstance(df, pd.DataFrame):
                # Remove timezone from datetime columns
                for col in df.select_dtypes(include=['datetimetz']).columns:
                    df[col] = df[col].dt.tz_localize(None)
                # Also ensure index (if datetime) is timezone naive
                if pd.api.types.is_datetime64tz_dtype(df.index):
                    df.index = df.index.tz_localize(None)
                df.to_excel(writer, sheet_name=sheet_name[:31])  # Excel sheet names max = 31 chars
