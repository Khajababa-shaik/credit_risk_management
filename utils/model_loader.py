# ==========================================================
# Import Libraries
# ==========================================================

import joblib
from pathlib import Path


# ==========================================================
# Models Directory
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"


# ==========================================================
# Load Model Files
# ==========================================================

def load_model_artifacts():
    """
    Load all saved machine learning artifacts.

    Returns
    -------
    dict
        Dictionary containing model, preprocessor,
        target encoder and feature columns.
    """

    artifacts = {

        "model": joblib.load(MODELS_DIR / "best_model.pkl"),

        "preprocessor": joblib.load(
            MODELS_DIR / "preprocessor.pkl"
        ),

        "target_encoder": joblib.load(
            MODELS_DIR / "target_encoder.pkl"
        ),

        "feature_columns": joblib.load(
            MODELS_DIR / "feature_columns.pkl"
        )

    }

    return artifacts