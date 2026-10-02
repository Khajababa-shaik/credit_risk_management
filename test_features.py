from utils.model_loader import load_model_artifacts

artifacts = load_model_artifacts()

feature_columns = artifacts["feature_columns"]

print(type(feature_columns))
print(f"Total Features: {len(feature_columns)}")

print("\nFeature Names:")
for i, feature in enumerate(feature_columns, start=1):
    print(f"{i}. {feature}")