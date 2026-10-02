# from utils.model_loader import load_model_artifacts
# from utils.prediction import create_features, predict_credit_risk

# artifacts = load_model_artifacts()

# model = artifacts["model"]
# preprocessor = artifacts["preprocessor"]

# sample = create_features(
#     age=35,
#     job=2,
#     credit_amount=5000,
#     duration=24,
#     sex="male",
#     housing="own",
#     saving_accounts="little",
#     checking_account="moderate",
#     purpose="car",
# )

# prediction, probability = predict_credit_risk(
#     model,
#     preprocessor,
#     sample,
# )

# print("Prediction :", prediction)
# print("Probability:", probability)

from utils.model_loader import load_model_artifacts
from utils.prediction import create_features, predict_credit_risk

# Load model artifacts
artifacts = load_model_artifacts()

model = artifacts["model"]
preprocessor = artifacts["preprocessor"]
target_encoder = artifacts["target_encoder"]

# Sample input
sample = create_features(
    age=35,
    job=2,
    credit_amount=5000,
    duration=24,
    sex="male",
    housing="own",
    saving_accounts="little",
    checking_account="moderate",
    purpose="car",
)

# Prediction
result = predict_credit_risk(
    model=model,
    preprocessor=preprocessor,
    target_encoder=target_encoder,
    user_df=sample,
)

print(result)