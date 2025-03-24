
import streamlit as st
import pandas as pd

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("tata_news_sentiment.csv")  # Ensure correct file path

df = load_data()

# Streamlit UI
st.title("📢 News Sentiment Analysis")

# Dropdown for company selection
company = st.selectbox("Select a company:", ["tata_news", "Reliance"])

# Display news and sentiment
if company == "tata_news":
    st.subheader("📌 News Articles")
    st.write(df[["Title", "Link"]])  # Display articles

    st.subheader("📊 Sentiment Report")
    st.write(df[["Sentiment"]])  # Display sentiment report

elif company == "Reliance":
    st.subheader("🚨 Currently no articles present for Reliance.")
