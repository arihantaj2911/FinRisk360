import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt
import shap
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'cleaned_credit_data.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'risk_model.pkl')

def explain_model():
    if not os.path.exists(MODEL_PATH):
        return
        
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    
    df = pd.read_csv(DATA_PATH)
    X = df.drop('credit_risk', axis=1)

    importances = pd.Series(model.feature_importances_, index=X.columns)
    importances.nlargest(10).plot(kind='barh', figsize=(10, 6), color='skyblue')
    plt.title('Top 10 Most Important Features (Global)')
    plt.xlabel('Importance Score')
    plt.tight_layout()
    plt.savefig(os.path.join(BASE_DIR, 'feature_importance.png'))
    plt.close()

    explainer = shap.TreeExplainer(model)
    X_sample = X.iloc[:100]
    shap_values = explainer.shap_values(X_sample)

    if isinstance(shap_values, list):
        values_to_plot = shap_values[1]
    elif isinstance(shap_values, np.ndarray) and len(shap_values.shape) == 3:
        values_to_plot = shap_values[:, :, 1]
    else:
        values_to_plot = shap_values

    plt.figure(figsize=(12, 8))
    shap.summary_plot(values_to_plot, X_sample, show=False)
    plt.title('SHAP Summary: Drivers of Credit Risk')
    plt.tight_layout()
    plt.savefig(os.path.join(BASE_DIR, 'shap_summary.png'))
    plt.close()

if __name__ == "__main__":
    explain_model()