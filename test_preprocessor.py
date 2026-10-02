from utils.model_loader import load_model_artifacts

artifacts = load_model_artifacts()

preprocessor = artifacts["preprocessor"]

print("=" * 60)
print("NUMERICAL FEATURES")
print("=" * 60)

print(preprocessor.transformers_[0][2])

print()

print("=" * 60)
print("CATEGORICAL FEATURES")
print("=" * 60)

print(preprocessor.transformers_[1][2])