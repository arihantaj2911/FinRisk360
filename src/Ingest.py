import pandas as pd
import os

def load_and_verify():
    data_path = os.path.join('data', 'credit_data.csv')
    
    df = pd.read_csv(data_path, sep=' ')
    
    null_counts = df.isnull().sum().sum()
    
    print(f"--- Data Health Check ---")
    print(f"Total Rows: {df.shape[0]} | Total Columns: {df.shape[1]}")
    print(f"Missing Values: {null_counts}")
    print(f"\nColumn Data Types:\n{df.dtypes.head()}")
    
    return df

if __name__ == "__main__":
    load_and_verify()