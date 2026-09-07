# Telecom Customer Churn Prediction

A Machine Learning web application that predicts whether a telecom customer is likely to churn based on customer demographics, account information, and subscribed services.

The application is built using **Python**, **Scikit-learn**, and **Streamlit**, and is deployed online for real-time predictions.

---

## Live Demo

🔗 **Live Application:**  
(https://telecom-customer-churn-prediction-app07.streamlit.app/)
🔗 **GitHub Repository:**  
https://github.com/Himanshi7104/telecom-customer-churn-prediction

---

## Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. This project uses Machine Learning to predict whether a customer is likely to leave the company based on customer demographics, account information, contract details, payment method, and subscribed services.

The application allows users to enter customer information and instantly receive:

- Churn Prediction
- Churn Probability
- Risk Level
- Key Factors affecting the prediction
- Suggested Business Action
- Estimated Monthly Charges
- Estimated Total Charges

The project combines **Machine Learning with business-oriented insights** to support customer retention decisions.

---

## Features

- Interactive Streamlit Web Application
- Real-time Churn Prediction
- Churn Probability Score
- Risk Level Classification (Low / Medium / High)
- Automatic Monthly Charges Estimation
- Automatic Total Charges Estimation
- Key Risk Indicators
- Business Recommendations
- Clean and user-friendly interface

---

## Automatic Charges Estimation

The application estimates customer charges automatically instead of requiring users to manually enter billing values.

A separate **Gradient Boosting Regression model** is used to estimate `MonthlyCharges` based on:

- Customer demographics
- Tenure
- Phone and internet services
- Additional subscribed services
- Contract type
- Paperless billing
- Payment method

The original `MonthlyCharges`, `TotalCharges`, and `Churn` variables are not used as input features for the charge estimation model to avoid data leakage.

The estimated total charges are then calculated as:

**Estimated Total Charges = Estimated Monthly Charges × Tenure**

The Monthly Charges estimation model achieved:

- **MAE:** 0.85
- **R²:** 0.9986

on the held-out test set.

---

## Dataset

**Dataset:** IBM Telco Customer Churn Dataset

The dataset contains customer demographic information, account details, billing information, contract details, payment methods, and subscribed telecom services used for churn analysis and prediction.

---

## Machine Learning Model

### Churn Prediction

**Model Used:**
- Logistic Regression

Data preprocessing included:

- Missing value handling
- Categorical Feature Encoding
- Feature Scaling
- Train-Test Split

The trained Logistic Regression model and scaler were saved using **Joblib** and integrated into the Streamlit application.

### Monthly Charges Estimation

**Model Used:**
- Gradient Boosting Regressor

The regression model estimates Monthly Charges using customer and service-related features.

The model is integrated into the Streamlit application to automatically generate estimated billing values for churn prediction.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib

---

## Project Structure

```text
telecom-customer-churn-prediction/
│
├── app.py
├── logistic_regression_model.pkl
├── monthly_charges_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Himanshi7104/telecom-customer-churn-prediction.git
```

### Move into the project folder

```bash
cd telecom-customer-churn-prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## Application Preview

The deployed application provides an interactive interface where users can enter customer information, estimate charges automatically, and receive a churn prediction with risk indicators and recommended business actions.

---

## Future Improvements

- Power BI dashboard for interactive business intelligence and churn analysis
- SQL-based customer churn analysis
- SHAP-based model explainability
- Additional Machine Learning models
- Model performance comparison
- Improved UI/UX
- Docker deployment
- Model monitoring

---

## Author

**Himanshi**

🔗 LinkedIn:  
www.linkedin.com/in/himanshi0710/

🔗 GitHub:  
https://github.com/Himanshi7104
