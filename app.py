import pandas as pd
import streamlit as st
import joblib

# ======================================
# Page Configuration
# ======================================

st.set_page_config(
    page_title="Telecom Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# ======================================
# Load Model
# ======================================

model = joblib.load("logistic_regression_model.pkl")
scaler = joblib.load("scaler.pkl")

# ======================================
# Sidebar
# ======================================

st.sidebar.title("📊 Telecom Churn Predictor")

st.sidebar.markdown(
"""
Predict customer churn using Machine Learning.
"""
)


st.sidebar.markdown("---")

st.sidebar.subheader("📌 About")

st.sidebar.info("""
This application predicts whether a telecom customer is likely to churn using a trained Logistic Regression model.

Fill in the customer information and click **Predict Customer Churn** to view the prediction.
""")

st.sidebar.subheader("👩‍💻 Developer")

st.sidebar.success("Himanshi")

st.sidebar.markdown("---")

st.sidebar.subheader("🛠 Tech Stack")

st.sidebar.markdown("""
- Python
- Scikit-Learn
- Streamlit
""")

st.sidebar.markdown("---")

st.sidebar.caption("Version 1.0")


# ======================================
# Hero Section
# ======================================

st.title("📊 Telecom Customer Churn Prediction")

st.markdown("""
Predict whether a telecom customer is likely to leave the company based on
customer demographics, subscription details and billing information.
""")

st.markdown("---")

st.subheader("📈 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Accuracy", "80.34%")

with col2:
    st.metric("Precision", "65.20%")

with col3:
    st.metric("ROC-AUC", "84.10%")

st.markdown("---")

# ======================================
# Customer Details Section
# ======================================

st.header("📝 Customer Information")

st.write("Fill in the customer details below.")

# ======================================
# Customer Basic Information
# ======================================

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

with col2:

    tenure = st.slider(
        "Tenure (Months)",
        min_value=0,
        max_value=72,
        value=12
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=18.0,
        max_value=120.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.0
    )

st.markdown("---")

st.header("🌐 Service Details")

col3, col4 = st.columns(2)

with col3:

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

with col4:

    paperless = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

st.markdown("---")

st.header("📺 Additional Services")

col5, col6 = st.columns(2)

with col5:

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

with col6:

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )

st.markdown("---")


left, center, right = st.columns([1, 2, 1])

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🚀 Predict Customer Churn",
    use_container_width=True
)

if predict:

    # ============================
    # Create Input Dictionary
    # ============================

    input_data = {

        'SeniorCitizen': 1 if senior == "Yes" else 0,
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,

        'gender_Male': 1 if gender == "Male" else 0,

        'Partner_Yes': 1 if partner == "Yes" else 0,

        'Dependents_Yes': 1 if dependents == "Yes" else 0,

        'PhoneService_Yes': 1 if phone_service == "Yes" else 0,

        'MultipleLines_No phone service': 1 if multiple_lines == "No phone service" else 0,
        'MultipleLines_Yes': 1 if multiple_lines == "Yes" else 0,

        'InternetService_Fiber optic': 1 if internet_service == "Fiber optic" else 0,
        'InternetService_No': 1 if internet_service == "No" else 0,

        'OnlineSecurity_No internet service': 1 if online_security == "No internet service" else 0,
        'OnlineSecurity_Yes': 1 if online_security == "Yes" else 0,

        'OnlineBackup_No internet service': 1 if online_backup == "No internet service" else 0,
        'OnlineBackup_Yes': 1 if online_backup == "Yes" else 0,

        'DeviceProtection_No internet service': 1 if device_protection == "No internet service" else 0,
        'DeviceProtection_Yes': 1 if device_protection == "Yes" else 0,

        'TechSupport_No internet service': 1 if tech_support == "No internet service" else 0,
        'TechSupport_Yes': 1 if tech_support == "Yes" else 0,

        'StreamingTV_No internet service': 1 if streaming_tv == "No internet service" else 0,
        'StreamingTV_Yes': 1 if streaming_tv == "Yes" else 0,

        'StreamingMovies_No internet service': 1 if streaming_movies == "No internet service" else 0,
        'StreamingMovies_Yes': 1 if streaming_movies == "Yes" else 0,

        'Contract_One year': 1 if contract == "One year" else 0,
        'Contract_Two year': 1 if contract == "Two year" else 0,

        'PaperlessBilling_Yes': 1 if paperless == "Yes" else 0,

        'PaymentMethod_Credit card (automatic)': 1 if payment == "Credit card (automatic)" else 0,
        'PaymentMethod_Electronic check': 1 if payment == "Electronic check" else 0,
        'PaymentMethod_Mailed check': 1 if payment == "Mailed check" else 0
    }

    # ==========================================
    # Convert dictionary to DataFrame
    # ==========================================

    input_df = pd.DataFrame([input_data])

    # Ensure correct column order
    feature_order = [
        'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',
        'gender_Male', 'Partner_Yes', 'Dependents_Yes',
        'PhoneService_Yes', 'MultipleLines_No phone service',
        'MultipleLines_Yes', 'InternetService_Fiber optic',
        'InternetService_No', 'OnlineSecurity_No internet service',
        'OnlineSecurity_Yes', 'OnlineBackup_No internet service',
        'OnlineBackup_Yes', 'DeviceProtection_No internet service',
        'DeviceProtection_Yes', 'TechSupport_No internet service',
        'TechSupport_Yes', 'StreamingTV_No internet service',
        'StreamingTV_Yes', 'StreamingMovies_No internet service',
        'StreamingMovies_Yes', 'Contract_One year',
        'Contract_Two year', 'PaperlessBilling_Yes',
        'PaymentMethod_Credit card (automatic)',
        'PaymentMethod_Electronic check',
        'PaymentMethod_Mailed check'
    ]

    input_df = input_df[feature_order]

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.markdown("---")

    st.subheader("📊 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:

        if prediction == 1:
            st.error("🚨 High Churn Risk")
            st.write(
                "The customer has a high probability of leaving the telecom service."
        )
        else:
            st.success("✅ Customer Likely to Stay")
            st.write(
                "The customer shows a low probability of churn based on the provided information."
        )

    st.metric(
        label="Churn Probability",
        value=f"{probability:.2%}"
    )

    st.caption("Estimated probability generated by the trained Logistic Regression model.")

    with col2:

        if probability < 0.30:
            st.success("🟢 Risk Level: LOW")

        elif probability < 0.70:
            st.warning("🟡 Risk Level: MEDIUM")

        else:
            st.error("🔴 Risk Level: HIGH")

        st.progress(float(probability))

    st.markdown("---")

    

    st.subheader("💡 Top Factors Affecting the Prediction")

    factors = []

# Positive (increase churn risk)
    if monthly_charges > 80:
        factors.append(("🔴", "High Monthly Charges", "Increase churn risk"))

    if payment == "Electronic check":
        factors.append(("🔴", "Electronic Check Payment", "Customers using this payment method churn more frequently"))

    if internet_service == "Fiber optic":
        factors.append(("🔴", "Fiber Optic Internet", "Historically associated with higher churn"))

    if paperless == "Yes":
        factors.append(("🟡", "Paperless Billing", "Slight positive association with churn"))

# Negative (reduce churn risk)
    if tenure > 24:
        factors.append(("🟢", "Long Customer Tenure", "Reduces churn risk"))

    if contract != "Month-to-month":
        factors.append(("🟢", "Long-Term Contract", "Strongly reduces churn"))

    if len(factors) == 0:
        st.info("No major churn-driving factors detected for this customer.")

    for icon, title, desc in factors:
        st.write(f"**{icon} {title}**")
        st.caption(desc)

    st.markdown("---")

    st.subheader("📌 Suggested Business Action")

    if probability >= 0.70:
        st.error(
        "Offer a retention discount, priority customer support, or a long-term contract to reduce churn risk."
    )

    elif probability >= 0.30:
        st.warning(
            "Monitor customer engagement and consider targeted promotional offers."
    )

    else:
        st.success(
            "No immediate retention action is required. Continue providing a positive customer experience."
    )

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;
color:grey;'>

Developed by <b>Himanshi</b>

📊 Telecom Customer Churn Prediction using Machine Learning

Built using Streamlit | Scikit-Learn | Python

</div>
""",
unsafe_allow_html=True
)
