# 💳 Credit Risk Prediction System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical-blue?logo=numpy)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# 📌 Project Overview

The **Credit Risk Prediction System** is a Machine Learning application that predicts whether a loan applicant is a **Good Credit Risk** or **Bad Credit Risk**.

The project follows a complete end-to-end Machine Learning pipeline including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Model Deployment using Streamlit

The application allows users to enter applicant details and instantly receive a credit risk prediction along with confidence scores and recommendations.

---

# 🚀 Features

✅ Professional ML Pipeline

✅ Data Cleaning

✅ Feature Engineering

✅ Multiple Machine Learning Models

- Logistic Regression
- KNN
- Decision Tree
- Random Forest
- Extra Trees
- Gradient Boosting
- AdaBoost

✅ Automatic Best Model Selection

✅ Probability Prediction

✅ Streamlit Dashboard

✅ Applicant Summary

✅ Risk Recommendation

---

# 📂 Project Structure

```text
credit-risk-model/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│
├── data/
│   ├── raw/
│   │   └── german_credit_data.csv
│   │
│   └── processed/
│       ├── cleaned_credit_data.csv
│       └── engineered_credit_data.csv
│
├── models/
│   ├── best_model.pkl
│   ├── preprocessor.pkl
│   ├── feature_columns.pkl
│   └── target_encoder.pkl
│
├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_EDA.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Model_Training.ipynb
│   └── 06_Model_Evaluation.ipynb
│
├── outputs/
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   ├── feature_importance.png
│   ├── learning_curve.png
│   └── model_report.csv
│
└── utils/
    ├── model_loader.py
    └── prediction.py
```

---

# 📊 Dataset

Dataset Used:

**German Credit Risk Dataset**

Number of Records

- 1000 Customers

Target Variable

- Good Credit
- Bad Credit

---

# ⚙️ Machine Learning Workflow

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Encoding
      │
      ▼
Scaling
      │
      ▼
Train/Test Split
      │
      ▼
Train 7 ML Models
      │
      ▼
Model Evaluation
      │
      ▼
Best Model Selection
      │
      ▼
Save Model (.pkl)
      │
      ▼
Streamlit Deployment
```

---

# 🧠 Feature Engineering

The following engineered features were created:

- Credit_Per_Month
- Credit_Age_Ratio
- Age_Duration_Product
- Credit_Age_Product
- Log_Credit_Amount
- Log_Duration

Categorical Features were encoded using:

- OneHotEncoder

Numerical Features were scaled using:

- StandardScaler

---

# 🤖 Models Trained

| Model               | Status |
| ------------------- | ------ |
| Logistic Regression | ✅     |
| KNN                 | ✅     |
| Decision Tree       | ✅     |
| Random Forest       | ✅     |
| Extra Trees         | ✅     |
| Gradient Boosting   | ✅     |
| AdaBoost            | ✅     |

The best performing model is automatically selected and saved as:

```
models/best_model.pkl
```

---

# 📈 Evaluation Metrics

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Generated outputs include:

- Confusion Matrix
- ROC Curve
- Learning Curve
- Feature Importance
- Model Comparison Report

---

# 💻 Streamlit Application

The application allows users to:

- Enter applicant details
- Predict credit risk
- View confidence score
- View approval recommendation
- Display applicant summary

---

# 🖼️ Screenshots

## Home Page

```
assets/home.png
```

---

## Prediction Result

```
assets/result.png
```

---

# 🛠️ Installation

Clone the repository

```bash
git clone https://github.com/Khajababa-shaik/credit-risk-model.git
```

Move into project

```bash
cd credit-risk-model
```

Create virtual environment

```bash
python -m venv myenv
```

Activate environment

### Windows

```bash
myenv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Application will open at

```
http://localhost:8501
```

---

# 📦 Requirements

Main Libraries

- Python 3.10
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Joblib
- Matplotlib
- Seaborn

---

# 📈 Future Improvements

- SHAP Explainability
- LIME Explanation
- XGBoost
- LightGBM
- Hyperparameter Tuning
- Docker Deployment
- Cloud Deployment
- Authentication
- Loan PDF Report Generation

---

# 👨‍💻 Author

**Khaja Baba Shaik**

AI Engineer | Machine Learning | Python Developer

GitHub

https://github.com/Khajababa-shaik

LinkedIn

https://www.linkedin.com/in/khajababashaik

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.

---

# 📜 License

This project is licensed under the MIT License.
