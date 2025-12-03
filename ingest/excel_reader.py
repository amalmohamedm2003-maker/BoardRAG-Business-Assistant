import pandas as pd
import os

def extract_excel_text(path: str):
    df = pd.read_excel(path)
    lines = []

    for index, row in df.iterrows():
        row_text = " | ".join([str(x) for x in row.values])
        lines.append(row_text)

    return {
        "file_name": os.path.basename(path),
        "rows": lines
    }
