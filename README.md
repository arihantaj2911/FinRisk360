# 🚀 FinRisk360 AI Pipeline

An End-to-End Real-Time Credit Risk Engine designed to automate loan approval decisions using Artificial Intelligence and Machine Learning, visualizing portfolio risk through a live dashboard.

## 📌 Project Overview
FinRisk360 bridges the gap between Data Science, Software Engineering, and Business Intelligence. It takes a trained Machine Learning AI model out of the Jupyter Notebook environment and deploys it into a fully containerized, full-stack application.

Users can submit loan applications via a responsive web interface. The data is processed by a backend API, evaluated by the AI model, securely logged into a local database, and visualized in real-time to monitor business risk.

## 🏗️ System Architecture
The backend services are completely isolated within a **Docker Container Environment**, ensuring cross-platform consistency.

* **Web UI (Frontend):** Collects applicant risk factors (HTML/CSS/JS).
* **Flask API (Backend):** Orchestrates the pipeline, formatting JSON requests and handling database logging.
* **Machine Learning Engine:** A Scikit-Learn Random Forest model that predicts the probability of loan default.
* **SQLite Database:** Acts as the local relational storage to persist every application and AI decision.
* **Power BI Dashboard:** Connects to the database to visualize live portfolio risk metrics and approval rates.

<img width="2528" height="1684" alt="Architecture_FinRisk360" src="https://github.com/user-attachments/assets/98801f92-55b5-42e0-8760-b4aa3828855f" />

## 🛠️ Tech Stack
* **Machine Learning & AI:** Python, Pandas, Scikit-Learn (Random Forest Classifier)
* **Backend API:** Flask, REST Architecture
* **Frontend:** HTML5, CSS3, JavaScript
* **Database:** SQLite3
* **DevOps:** Docker
* **Analytics:** Power BI

## 🚀 Quick Start Guide

### Prerequisites
Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running on your machine.

### Installation & Execution

**1. Clone the repository:**
```bash
git clone [https://github.com/arihantaj2911/FinRisk360.git](https://github.com/arihantaj2911/FinRisk360.git)
cd FinRisk360
2. Build the Docker Image:

Bash
docker build -t finrisk-app .
3. Run the Container:

Bash
docker run -p 5000:5000 finrisk-app
