import pandas as pd
import os
import pyarrow as pa
import pyarrow.parquet as pq

input_path = "download/HIV.csv"
output_path = "brick/hiv.parquet"

def build_brick():
    print(f"Reading {input_path}...")
    df = pd.read_csv(input_path)
    
    print("Columns:", df.columns)
    
    # Clean up column names
    df.columns = [c.lower().strip() for c in df.columns]
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Write to parquet
    print(f"Writing to {output_path}...")
    table = pa.Table.from_pandas(df)
    pq.write_table(table, output_path)
    print("Build complete.")

if __name__ == "__main__":
    build_brick()
