import pandas as pd
try:
    df = pd.read_parquet("brick/hiv.parquet")
    print(f"File is readable. Rows: {len(df)}")
    print(df.head())
except Exception as e:
    print(f"Error reading parquet: {e}")
