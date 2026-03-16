import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'cleaned_credit_data.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'risk_model.pkl')

try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    exit()

X = df.drop('credit_risk', axis=1)
y = df['credit_risk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(
    n_estimators=100, 
    random_state=42, 
    class_weight='balanced' 
)

model.fit(X_train, y_train)

os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
with open(MODEL_PATH, 'wb') as f:
    pickle.dump(model, f)