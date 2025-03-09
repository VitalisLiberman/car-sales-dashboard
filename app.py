import streamlit as st
import pandas as pd
import plotly.express as px

# Load data and cache it for performance
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

df = load_data()

# App title
st.title("Car Sales Analysis in the USA")

# Price distribution histogram
st.header("Price Distribution of Cars")
fig = px.histogram(df, x="price", nbins=50, title="Price Distribution")
st.plotly_chart(fig)

# Scatter plot: Price vs Mileage
st.header("Price vs Mileage")
fig2 = px.scatter(df, x="odometer", y="price", opacity=0.5, title="Price vs Mileage")
st.plotly_chart(fig2)

# Filter cars by condition
st.header("Filter by Car Condition")
condition = st.selectbox("Select car condition", df["condition"].unique())
filtered_df = df[df["condition"] == condition]
st.write(f"Cars in condition: {condition}", filtered_df)

