import requests
from deep_translator import GoogleTranslator


NEWS_API_KEY = "d3eda9a2d72c4c68a5d6f872c4c86304"
NEWS_API_URL = "https://newsapi.org/v2/everything"




def fetch_news(company):
    params = {
        "q": company,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()
    
    if data["status"] == "ok":
        return data["articles"][:10]
    return []

def translate_to_hindi(text):
    if text:
        return GoogleTranslator(source="en", target="hi").translate(text)
    return ""

def analyze_sentiment(text, model):
    if not text:
        return "Neutral"
    result = model(text)
    return result[0]['label']

