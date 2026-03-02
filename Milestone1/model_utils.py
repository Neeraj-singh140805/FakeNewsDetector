import pickle
import re
import string
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

sentiment_analyzer = SentimentIntensityAnalyzer()

# ---------------- CLEANING ----------------

def clean_text(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r'\(reuters\)', ' ', text)
    text = re.sub(r'reuters', ' ', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ---------------- STYLE METRICS ----------------

def emotional_intensity_score(text):
    return round(abs(sentiment_analyzer.polarity_scores(text)["compound"]), 2)

# ---------------- MAIN ANALYSIS ----------------

def analyze_article(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prob_real = model.predict_proba(vec)[0][1]
    credibility = round(prob_real * 100, 2)

    return {
        "credibility": credibility,
        "prediction": "Likely REAL news" if credibility >= 50 else "Likely FAKE news",
        "emotional_intensity": emotional_intensity_score(text),
    }