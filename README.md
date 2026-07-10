# Telecom Customer Churn Prediction

A Machine Learning web application that predicts whether a telecom customer is likely to churn based on customer demographics, account information, and subscribed services.

The application is built using **Python**, **Scikit-learn**, and **Streamlit**, and is deployed online for real-time predictions.

---

## Live Demo

🔗 **Live Application:**  
https://telecom-customer-churn-prediction-abuhtjef5hebappv5ji3eapp.streamlit.app/

🔗 **GitHub Repository:**  
https://github.com/Himanshi7104/telecom-customer-churn-prediction

---

## Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. This project uses Machine Learning to predict whether a customer is likely to leave the company based on various customer attributes.

The application allows users to enter customer information and instantly receive:

- Churn Prediction
- Churn Probability
- Risk Level
- Key Factors affecting the prediction
- Suggested Business Action

---

## Features

- Interactive Streamlit Web Application
- Real-time Churn Prediction
- Churn Probability Score
- Risk Level Classification (Low / Medium / High)
- Business Insights based on customer profile
- Clean and user-friendly interface

---

## Dataset

**Dataset:** IBM Telco Customer Churn Dataset

The dataset contains customer demographic information, account details, billing information, and subscribed telecom services used for churn prediction.

---

## Machine Learning Model

Model Used:

- Logistic Regression

Data preprocessing included:

- Missing value handling
- Feature Encoding
- Feature Scaling
- Train-Test Split

The trained model and scaler were saved using Joblib and integrated into the Streamlit application.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## Project Structure

```text
telecom-customer-churn-prediction/
│
├── app.py
├── logistic_regression_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Himanshi7104/telecom-customer-churn-prediction.git
```

Move into the project folder

```bash
cd telecom-customer-churn-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Application Preview

> Screenshots will be added soon.

---

## Future Improvements

- SHAP-based model explainability
- Additional Machine Learning models
- Improved UI/UX
- Docker deployment
- Model monitoring

---

## Author

**Himanshi**

LinkedIn: *www.linkedin.com/in/himanshi0710*

GitHub: https://github.com/Himanshi7104
