from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import joblib
import os
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app)

DB_PATH = '/app/data/finrisk.db'
MODEL_PATH = '/app/models/risk_model.pkl'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_features TEXT,
            credit_risk_prediction TEXT,
            probability_score REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

if os.path.exists(MODEL_PATH):
    ML_MODEL = joblib.load(MODEL_PATH)
else:
    ML_MODEL = None

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    full_features = [
        data.get('status', 3),
        data.get('duration', 12),
        data.get('credit_history', 3),
        data.get('purpose', 0),
        data.get('amount', 5000),
        data.get('savings', 3),
        data.get('employment_duration', 3),
        data.get('installment_rate', 2),
        data.get('personal_status_sex', 1),
        data.get('other_debtors', 0),
        data.get('present_residence', 2),
        data.get('property', 1),
        data.get('age', 30),
        data.get('other_installment_plans', 0),
        data.get('housing', 1),
        data.get('number_credits', 1),
        data.get('job', 2),
        data.get('people_liable', 1),
        data.get('telephone', 0),
        data.get('foreign_worker', 1)
    ]
    
    if ML_MODEL:
        prob = ML_MODEL.predict_proba([full_features])[0][1]
    else:
        prob = 0.65
        
    label = 'Good' if prob >= 0.60 else 'Bad'
    score = round(float(prob), 2)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO predictions_log (input_features, credit_risk_prediction, probability_score, timestamp) VALUES (?, ?, ?, ?)",
        (str(data), label, score, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()
    
    return jsonify({
        'credit_risk_prediction': label,
        'probability_score': score
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)