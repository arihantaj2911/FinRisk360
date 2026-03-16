import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, 'data', 'german_credit.csv')
OUTPUT_FILE = os.path.join(BASE_DIR, 'data', 'cleaned_credit_data.csv')

def run_preprocessing():
    if not os.path.exists(INPUT_FILE):
        return

    df = pd.read_csv(INPUT_FILE)

    df['number_credits'] = df['number_credits'].replace({'3-Feb': '2-3', '5-Apr': '4-5'})

    df['credit_risk'] = df['credit_risk'].map({'good': 1, 'bad': 0})

    le = LabelEncoder()
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col].astype(str))

    df.to_csv(OUTPUT_FILE, index=False)

if __name__ == "__main__":
    run_preprocessing()