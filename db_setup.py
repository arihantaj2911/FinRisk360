import sqlite3
import pandas as pd
import os

BASE_DIR = '/app' if os.path.exists('/app') else os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CSV_PATH = os.path.join(DATA_DIR, 'cleaned_credit_data.csv')
DB_PATH = os.path.join(DATA_DIR, 'finrisk.db')

def setup_database():
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
        df.to_sql('historical_loans', conn, if_exists='replace', index=False)
        
    conn.execute('CREATE TABLE IF NOT EXISTS predictions_log (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, credit_risk_prediction TEXT, probability_score REAL, input_features TEXT)')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()