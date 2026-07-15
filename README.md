# Customer Churn Prediction Using Machine Learning

## Overview

This project predicts whether a telecom customer is likely to leave the company's services based on customer demographics, account information, and service usage. The objective is to help businesses identify customers at risk of churning so that retention strategies can be implemented.

---

## Dataset

- **Source:** IBM Telco Customer Churn Dataset (Kaggle)
- **Records:** 7,043 customers
- **Features:** 21 customer attributes
- **Target Variable:** Churn (Yes/No)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

---

## Project Workflow

- Data Loading
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Model Training
- Model Evaluation
- Model Comparison
- Feature Importance Analysis
- Dashboard Development

---

## Machine Learning Models

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

---

## Results

Random Forest achieved the best overall performance and was selected as the final model. The trained model was saved for future predictions and integrated into a Streamlit dashboard.

---

## Dashboard Features

- Dataset Preview
- Customer Statistics
- Churn Distribution
- Gender Distribution
- Contract Type Analysis
- Internet Service Analysis
- Monthly Charges Distribution
- Customer Tenure Distribution

---

## Project Structure

```text
Customer-Churn-Prediction
│
├── dashboard/
├── dataset/
├── images/
├── models/
├── notebooks/
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

---

## Future Improvements

- Hyperparameter tuning
- Cross-validation
- XGBoost implementation
- Deployment on Streamlit Cloud
- Interactive prediction interface

---

## Author

Developed as part of a Data Science Internship project.


