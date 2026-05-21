# ⚙️ Predictive Equipment Health Monitoring System

An AI-powered industrial monitoring system that predicts machine failures using Machine Learning, interactive dashboards, analytics, and real-time risk monitoring.

This project was developed using Python, Streamlit, Scikit-learn, MySQL, Plotly, and Random Forest Classifier.

---

# 🚀 Project Overview

The Predictive Equipment Health Monitoring System helps industries detect potential machine failures before they occur.

The system analyzes machine operating parameters such as:

- Air Temperature
- Process Temperature
- Rotational Speed (RPM)
- Torque
- Tool Wear

Using Machine Learning, the application predicts whether a machine is:

✅ Healthy  
⚠️ At Risk of Failure

The system also provides:
- Failure probability analysis
- Interactive analytics dashboard
- Prediction history tracking
- User authentication
- Real-time visualization

---

# 🧠 Machine Learning Workflow

The ML pipeline includes:

1. Data Understanding
2. Data Cleaning
3. Feature Selection
4. Handling Imbalanced Data using SMOTE
5. Model Training using Random Forest
6. Model Evaluation
7. Feature Importance Analysis
8. Model Deployment using Streamlit

---

# 📊 Features

## 🔐 Authentication System
- User Registration
- User Login
- Session-based access

---

## 🤖 Machine Failure Prediction
Predicts machine health using:
- Random Forest Classifier
- Trained ML model (.pkl)

---

## 📈 Failure Probability Analysis
Displays:
- Healthy probability
- Failure probability
- Risk percentage

---

## 📉 Interactive Charts
Includes:
- Gauge Chart
- Risk Visualization
- Failure Trend Analysis
- Pie Charts

---

## 📋 Prediction History Dashboard
Stores and displays:
- Previous predictions
- Failure probability
- Machine parameters
- Prediction timestamps

---

## 📊 Analytics Dashboard
Shows:
- Total Predictions
- Total Failures
- Healthy Machines
- Average Risk Percentage

---

## 📥 Report Exporting
Download prediction reports as:
- CSV files

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## Machine Learning
- Scikit-learn
- Random Forest Classifier
- SMOTE

## Database
- MySQL

## Visualization
- Plotly
- Matplotlib

## Data Processing
- Pandas
- NumPy

---

# 🗂️ Project Structure

```bash
predictive-maintenance-system/

│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── predictive_maintenance_model.pkl
│
├── dataset/
│   └── ai4i2020.csv
│
├── utils/
│   ├── predict.py
│   ├── database.py
│   ├── auth.py
│   ├── charts.py
│   ├── analytics.py
│   └── feature_importance.py
│
├── notebooks/
│   └── training.ipynb
