# ==========================================================
# Prediction Utilities
# ==========================================================

import numpy as np
import pandas as pd


# ==========================================================
# Create Features
# ==========================================================

def create_features(
    age,
    job,
    credit_amount,
    duration,
    sex,
    housing,
    saving_accounts,
    checking_account,
    purpose,
):
    """
    Create a one-row DataFrame containing all original
    and engineered features required by the trained model.
    """

    # --------------------------------------------------
    # Prevent division by zero
    # --------------------------------------------------

    age = max(age, 1)
    duration = max(duration, 1)

    # --------------------------------------------------
    # Engineered Features
    # --------------------------------------------------

    credit_per_month = credit_amount / duration

    credit_age_ratio = credit_amount / age

    age_duration_product = age * duration

    credit_age_product = credit_amount * age

    log_credit_amount = np.log1p(credit_amount)

    log_duration = np.log1p(duration)

    # --------------------------------------------------
    # Create Input DataFrame
    # --------------------------------------------------

    user_df = pd.DataFrame({

        "Age": [age],

        "Job": [job],

        "Credit amount": [credit_amount],

        "Duration": [duration],

        "Credit_Per_Month": [credit_per_month],

        "Credit_Age_Ratio": [credit_age_ratio],

        "Age_Duration_Product": [age_duration_product],

        "Credit_Age_Product": [credit_age_product],

        "Log_Credit_Amount": [log_credit_amount],

        "Log_Duration": [log_duration],

        "Sex": [sex],

        "Housing": [housing],

        "Saving accounts": [saving_accounts],

        "Checking account": [checking_account],

        "Purpose": [purpose]

    })

    return user_df


# ==========================================================
# Predict Credit Risk
# ==========================================================

def predict_credit_risk(
    model,
    preprocessor,
    target_encoder,
    user_df,
):
    """
    Predict credit risk.

    Returns:
        dict containing:
            prediction
            label
            confidence
            good_probability
            bad_probability
    """

    # --------------------------------------------------
    # Apply preprocessing
    # --------------------------------------------------

    processed = preprocessor.transform(user_df)

    processed = pd.DataFrame(
        processed,
        columns=preprocessor.get_feature_names_out()
    )

    # --------------------------------------------------
    # Model Prediction
    # --------------------------------------------------

    prediction = model.predict(processed)[0]

    probabilities = model.predict_proba(processed)[0]

    # --------------------------------------------------
    # Decode Prediction Label
    # --------------------------------------------------

    label = target_encoder.inverse_transform([prediction])[0]

    # --------------------------------------------------
    # Confidence
    # --------------------------------------------------

    confidence = max(probabilities) * 100

    # --------------------------------------------------
    # Return Results
    # --------------------------------------------------

    return {

        "prediction": int(prediction),

        "label": label,

        "confidence": round(confidence, 2),

        "good_probability": round(probabilities[1] * 100, 2),

        "bad_probability": round(probabilities[0] * 100, 2)

    }