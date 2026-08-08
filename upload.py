import os
import pandas as pd
import glob

def load_csv(file_path):
    """
    Loads any CSV file and returns a pandas DataFrame.
    """

    # Check whether file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Read CSV
    df = pd.read_csv(file_path)

    print("=" * 50)
    print("✅ CSV Loaded Successfully")
    print("=" * 50)

    print(f"\nRows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nFirst Five Rows:")
    print(df.head())

    return df

    

    from sqlalchemy import create_engine
from database import engine

def upload_to_mysql(df, table_name):

    # Replace existing table if it already exists
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print("=" * 50)
    print(f"✅ '{table_name}' uploaded successfully!")
    print("=" * 50)

import glob
import os

def upload_folder(folder_path):
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

    if not csv_files:
        print("No CSV files found.")
        return

    for file in csv_files:
        print(f"\nUploading {os.path.basename(file)}")

        df = load_csv(file)

        table_name = os.path.splitext(os.path.basename(file))[0]

        upload_to_mysql(df, table_name)

    print("\n✅ All CSV files uploaded successfully!")