from utils.model_loader import load_model_artifacts

artifacts = load_model_artifacts()

print(type(artifacts["model"]))
print(type(artifacts["preprocessor"]))
print(type(artifacts["target_encoder"]))
print(type(artifacts["feature_columns"]))