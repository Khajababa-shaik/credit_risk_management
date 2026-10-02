credit-risk-model/
│
├── app.py # Streamlit Application
├── requirements.txt # Project Dependencies
├── README.md # Project Documentation
├── .gitignore # Ignore unnecessary files
│
├── assets/ # UI Resources
│ ├── logo.png
│ ├── banner.png
│ ├── favicon.ico
│ └── style.css
│
├── data/
│ ├── raw/
│ │ └── german_credit_data.csv
│ │
│ ├── processed/
│ │ └── processed_credit_data.csv
│ │
│ └── predictions/
│ └── prediction_history.csv
│
├── notebooks/
│ ├── 01_Data_Understanding.ipynb
│ ├── 02_Data_Cleaning.ipynb
│ ├── 03_EDA.ipynb
│ ├── 04_Feature_Engineering.ipynb
│ ├── 05_Model_Training.ipynb
│ └── 06_Model_Evaluation.ipynb
│
├── models/
│ ├── best_model.pkl
│ ├── scaler.pkl
│ ├── encoder.pkl
│ └── feature_columns.pkl
│
├── utils/
│ ├── **init**.py
│ ├── config.py
│ ├── preprocessing.py
│ ├── predictor.py
│ ├── model_loader.py
│ ├── feature_engineering.py
│ └── report_generator.py
│
├── pages/
│ ├── 1_Dashboard.py
│ ├── 2_Predict.py
│ ├── 3_Analytics.py
│ └── 4_About.py
│
├── outputs/
│ ├── reports/
│ ├── charts/
│ └── logs/
│
└── screenshots/
├── dashboard.png
├── prediction.png
└── analytics.png
