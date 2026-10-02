# ==========================================================
# Credit Risk Prediction System
# ==========================================================
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

from utils.model_loader import load_model_artifacts
from utils.prediction import (
    create_features,
    predict_credit_risk,
)

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="💳",
    layout="wide",
)
# ==========================================================
# Load CSS
# ==========================================================

css_file = Path("assets/style.css")

if css_file.exists():

    with open(css_file) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
# ----------------------------------------------------------
# Load Model Artifacts
# ----------------------------------------------------------

artifacts = load_model_artifacts()

model = artifacts["model"]
preprocessor = artifacts["preprocessor"]
target_encoder = artifacts["target_encoder"]


with st.sidebar:

    st.title("🏦 Bank Dashboard")

    st.success("Model Loaded")

    st.write("---")

    st.write("### Model")

    st.write(type(model).__name__)

    st.write("")

    st.write("### Features")

    st.write(model.n_features_in_)

    st.write("")

    st.info(
        """
Dataset

German Credit Dataset

Machine Learning

Logistic Regression
"""
    )


    
# ----------------------------------------------------------
# Title
# ----------------------------------------------------------

st.title("💳 Credit Risk Prediction System")

st.markdown(
"""
# 💳 Credit Risk Prediction Dashboard

Machine Learning Powered Loan Approval System
"""
)

st.divider()

# ==========================================================
# INPUT FORM
# ==========================================================

col1, col2 = st.columns(2)

# ----------------------------------------------------------
# Left Column
# ----------------------------------------------------------

with col1:

    st.subheader("👤 Applicant Information")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
    )

    job = st.selectbox(
        "Job",
        [0, 1, 2, 3],
        help="""
0 = Unskilled & Non-resident

1 = Unskilled

2 = Skilled

3 = Highly Skilled / Management
"""
    )

    sex = st.selectbox(
        "Gender",
        ["male", "female"]
    )

    housing = st.selectbox(
        "Housing",
        [
            "own",
            "rent",
            "free"
        ]
    )

# ----------------------------------------------------------
# Right Column
# ----------------------------------------------------------

with col2:

    st.subheader("💰 Loan Information")

    credit_amount = st.number_input(
        "Credit Amount",
        min_value=100,
        value=5000,
    )

    duration = st.number_input(
        "Loan Duration (Months)",
        min_value=1,
        value=24,
    )

    saving_accounts = st.selectbox(
        "Saving Account",
        [
            "No Account",
            "little",
            "moderate",
            "quite rich",
            "rich"
        ]
    )

    checking_account = st.selectbox(
        "Checking Account",
        [
            "No Account",
            "little",
            "moderate",
            "rich"
        ]
    )

    purpose = st.selectbox(
        "Loan Purpose",
        [
            "business",
            "car",
            "domestic appliances",
            "education",
            "furniture/equipment",
            "radio/TV",
            "repairs",
            "vacation/others"
        ]
    )

# ==========================================================
# Prediction Button
# ==========================================================

st.divider()

predict_button = st.button(
    "🔍 Predict Credit Risk",
    use_container_width=True,
)

# ==========================================================
# Prediction
# ==========================================================

if predict_button:

    # ------------------------------------------------------
    # Create Features
    # ------------------------------------------------------

    user_df = create_features(
        age=age,
        job=job,
        credit_amount=credit_amount,
        duration=duration,
        sex=sex,
        housing=housing,
        saving_accounts=saving_accounts,
        checking_account=checking_account,
        purpose=purpose,
    )

    # ------------------------------------------------------
    # Make Prediction
    # ------------------------------------------------------

    result = predict_credit_risk(
        model=model,
        preprocessor=preprocessor,
        target_encoder=target_encoder,
        user_df=user_df,
    )

    prediction = result["prediction"]
    label = result["label"]
    confidence = result["confidence"]
    good_probability = result["good_probability"]
    bad_probability = result["bad_probability"]

    # ------------------------------------------------------
    # Dashboard
    # ------------------------------------------------------

    st.divider()

    st.header("📊 Prediction Result")

    # ------------------------------------------------------
    # Decision Card
    # ------------------------------------------------------

    if label.lower() == "good":

        st.success("✅ Loan Approved")

    else:

        st.error("❌ High Credit Risk")

    # ------------------------------------------------------
    # Metrics
    # ------------------------------------------------------

    metric1, metric2, metric3 = st.columns(3)

    with metric1:

        st.metric(
            label="Prediction",
            value=label.title(),
        )

    with metric2:

        st.metric(
            label="Confidence",
            value=f"{confidence:.2f}%",
        )

    with metric3:

        st.metric(
            label="Risk Score",
            value=f"{bad_probability:.2f}%",
        )

    # ------------------------------------------------------
    # Probability Bars
    # ------------------------------------------------------

    st.subheader("Prediction Probability")

    st.write("🟢 Good Credit Probability")

    st.progress(good_probability / 100)

    st.write(f"{good_probability:.2f}%")

    st.write("")

    st.write("🔴 Bad Credit Probability")

    st.progress(bad_probability / 100)

    st.write(f"{bad_probability:.2f}%")

    # ------------------------------------------------------
    # Applicant Summary
    # ------------------------------------------------------

    st.subheader("Applicant Summary")

    summary = pd.DataFrame({

        "Field": [
            "Age",
            "Job Level",
            "Gender",
            "Housing",
            "Credit Amount",
            "Duration",
            "Saving Account",
            "Checking Account",
            "Purpose"
        ],

        "Value": [
            age,
            job,
            sex,
            housing,
            credit_amount,
            duration,
            saving_accounts,
            checking_account,
            purpose
        ]

    })

    st.table(summary)

    # ------------------------------------------------------
    # Recommendation
    # ------------------------------------------------------

    st.subheader("Recommendation")

    if label.lower() == "good":

        st.success(
            f"""
### ✅ Low Credit Risk

The applicant has a **{good_probability:.2f}% probability** of being a good credit customer.

**Recommendation**

- Approve the loan.
- Perform standard KYC verification.
- Continue with the normal approval process.
"""
        )

    else:

        st.error(
            f"""
### ❌ High Credit Risk

The applicant has a **{bad_probability:.2f}% probability** of defaulting.

**Recommendation**

- Review repayment history.
- Verify monthly income.
- Request additional supporting documents.
- Consider reducing the loan amount.
- Perform manual credit assessment.
"""
        )

    # ------------------------------------------------------
    # Raw Prediction (Optional)
    # ------------------------------------------------------

    with st.expander("🔍 View Raw Prediction"):

        st.json(result)