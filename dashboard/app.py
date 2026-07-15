import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Customer Churn Prediction Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction Dashboard")

# Load Dataset
df = pd.read_csv("dataset/customer_churn.csv")

# Convert TotalCharges
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# Dataset Preview
st.header("Dataset Preview")
st.dataframe(df.head())

# Dataset Information
st.header("Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Churned Customers", df[df["Churn"]=="Yes"].shape[0])

# Churn Distribution
st.header("Customer Churn Distribution")

fig, ax = plt.subplots()

df["Churn"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)

# Gender Distribution
st.header("Gender Distribution")

fig, ax = plt.subplots()

df["gender"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)

# Contract Type
st.header("Contract Type Distribution")

fig, ax = plt.subplots()

df["Contract"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)

# Internet Service
st.header("Internet Service")

fig, ax = plt.subplots()

df["InternetService"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)

# Monthly Charges
st.header("Monthly Charges")

fig, ax = plt.subplots()

ax.hist(df["MonthlyCharges"], bins=30)

st.pyplot(fig)

# Tenure
st.header("Customer Tenure")

fig, ax = plt.subplots()

ax.hist(df["tenure"], bins=30)

st.pyplot(fig)

st.success("Dashboard Loaded Successfully!")