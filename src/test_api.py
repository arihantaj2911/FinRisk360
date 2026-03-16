import requests

url = 'http://127.0.0.1:5000/predict'

risky_applicant = {
    "status": 0,
    "duration": 48,
    "credit_history": 2,
    "purpose": 0,
    "amount": 15000,
    "savings": 0,
    "employment_duration": 0,
    "installment_rate": 4,
    "personal_status_sex": 1, 
    "other_debtors": 0, 
    "present_residence": 4, 
    "property": 3,
    "age": 22,
    "other_installment_plans": 0,
    "housing": 2,
    "number_credits": 1, 
    "job": 0,
    "people_liable": 1,        
    "telephone": 0, 
    "foreign_worker": 1
}

response = requests.post(url, json=risky_applicant)

print("API Response:", response.json())