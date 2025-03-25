from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Function to fetch news articles from Google News RSS
def fetch_news(company):
    url = f"/content/tata_news_sentiment.csv"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")
    articles = soup.find_all("item")

    if not articles:  # If no articles found, return empty
        return []

    news_data = []
    for article in articles[:5]:  # Fetch only top 5 articles
        title = article.title.text
        link = article.link.text
        news_data.append({"title": title, "link": link})

    return news_data

# Function for sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# API Endpoint to fetch news and sentiment
@app.route("/news", methods=["GET"])
def get_news():
    company = request.args.get("company")

    if not company:
        return jsonify({"error": "No company name provided"}), 400

    news_articles = fetch_news(company)

    if not news_articles:
        return jsonify({"message": "No articles found", "articles": []})

    # Perform sentiment analysis on article titles
    for article in news_articles:
        article["sentiment"] = analyze_sentiment(article["title"])

    return jsonify({"company": company, "articles": news_articles})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
