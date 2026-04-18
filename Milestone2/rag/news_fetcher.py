import requests
from dotenv import load_dotenv
import os
import re

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY missing")


def clean_query(query):
    query = query.lower()
    query = re.sub(r'[^a-zA-Z0-9\s]', '', query)
    keywords = query.split()
    keywords = [word for word in keywords if len(word) > 3]
    return " ".join(keywords[:6])


def fetch_news(query):
    url = "https://newsapi.org/v2/everything"

    search_query = clean_query(query)

    params = {
        "q": search_query,
        "apiKey": NEWS_API_KEY,
        "pageSize": 5,
        "sortBy": "relevancy",
        "language": "en"
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = []

    for article in data.get("articles", []):
        title = article.get("title")
        content = article.get("description") or article.get("content")
        url = article.get("url")
        source = article.get("source", {}).get("name")

        if content:
            articles.append({
                "title": title,
                "content": content,
                "url": url,
                "source": source
            })

    if not articles:
        params["q"] = "news " + search_query
        response = requests.get(url, params=params)
        data = response.json()

        for article in data.get("articles", []):
            content = article.get("content") or article.get("description")
            if content:
                articles.append(content)

    return articles
