# FinRisk360: End-to-End Real-Time Credit Risk Engine

FinRisk360 is a full-stack AI solution that automates credit risk assessment. It features a live data pipeline where user inputs from a web interface are processed by a Machine Learning model in Docker, stored in a database, and visualized instantly in a Power BI dashboard.

## 🚀 The Workflow
The project follows a circular data lifecycle:
1. **Frontend:** User submits loan details (Age, Amount, etc.) via a responsive Web UI.
2. **API (Brain):** A Flask API inside a Docker container runs the data through a ML model (`model.pkl`).
3. **Database:** The prediction and probability score are logged into a SQLite database.
4. **Analytics:** Power BI connects to the database to provide real-time risk insights and KPI tracking.



## 🛠️ Tech Stack
- **Languages:** Python (Flask), JavaScript, HTML5/CSS3
- **DevOps:** Docker (Containerization & Volumes)
- **Machine Learning:** Scikit-Learn (Classification Model)
- **Database:** SQLite3
- **Visualization:** Power BI Desktop

## 📊 Dashboard Features
- **Live Approval Rate:** Real-time breakdown of Good vs. Bad credit risks.
- **AI Confidence Gauge:** Average probability score of the current portfolio.
- **Portfolio Decomposition:** Drill-down analysis by Job, Housing, and Loan Purpose.
- **Risk Profiling:** Scatter plots analyzing the relationship between Age and Loan Amount.

## ⚙️ How to Run
1. **Build the Docker Image:**
   ```powershell
   docker build -t finrisk-app .

2. **Run the Container:**

PowerShell: 
docker run -d -p 5000:5000 -v ${PWD}/data:/app/data --name finrisk-app finrisk-app
Open the App:
Simply open index.html in your browser and submit an application.

Developed by: Arihant Sanjay Ostwal

LinkedIn: 