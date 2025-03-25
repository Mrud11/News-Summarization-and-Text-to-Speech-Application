import streamlit as st
import pandas as pd

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("tata_news_sentiment.csv")  # Ensure correct file path

df = load_data()

# Streamlit UI
st.title("📢 News Sentiment Analysis")

# Dropdown for company selection (with default placeholder)
company = st.selectbox("Select a company:", ["Select an option", "tata_news", "Reliance"])

# Show content only after a valid selection
#if company != "Select an option":
if company == "tata_news":
        st.subheader("📌 News Articles")
        st.write(df[["Title", "Link"]])  # Display articles

        st.subheader("📊 Sentiment Report")
        st.write(df[["Sentiment"]])  # Display sentiment report

        # Play comparative analysis audio
        st.subheader("🔊 Comparative Analysis (Audio in Hindi)")
        st.audio("comparative_analysis.mp3", format="audio/mp3")  # Play the MP3 file

elif company == "Reliance":
        st.subheader("🚨 Currently no articles present for Reliance.")

