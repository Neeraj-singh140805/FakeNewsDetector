import pickle
import re
import string
import os
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Constants derived from your research logic
SENSATIONAL_WORDS = {
    "shocking", "unbelievable", "explosive", "disaster", "nightmare", 
    "chaos", "outrageous", "incredible", "terrifying", "horrifying"
}
HYPERBOLE_WORDS = {
    "always", "never", "everyone", "no one", "worst ever", 
    "best ever", "guaranteed", "totally"
}
CLICKBAIT_PATTERNS = [
    r"you won'?t believe", r"what happens next", r"number \d+", 
    r"this is what happened", r"will blow your mind"
]

# Initialize sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

def clean_text(text):
    """Preprocessing logic from news_credbility_analyzer notebook"""
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r'\(reuters\)', ' ', text)
    text = re.sub(r'reuters', ' ', text)
    text = re.sub(r'^[A-Z\s]+-\s', ' ', text)
    text = re.sub(r'\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b', ' ', text)
    text = re.sub(r'\b(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\b', ' ', text)
    
    leak_words = ["washington", "new york", "said", "told", "video", "image", "images", "watch", "breaking"]
    pattern = r'\b(' + '|'.join(leak_words) + r')\b'
    text = re.sub(pattern, ' ', text)
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_style_metrics(text):
    """Linguistic style scoring logic from notebook"""
    words = re.findall(r'\w+', text.lower())
    
    sens = round((sum(word in SENSATIONAL_WORDS for word in words) / max(len(words), 1)) * 100, 2)
    click = sum(bool(re.search(p, text.lower())) for p in CLICKBAIT_PATTERNS)
    
    lower = text.lower()
    exag = sum(phrase in lower for phrase in HYPERBOLE_WORDS)
    superlatives = re.findall(r'\b\w+est\b', lower)
    exag_count = exag + len(superlatives)
    
    orig_words = text.split()
    caps = sum(word.isupper() and len(word) > 2 for word in orig_words)
    punct = text.count("!") + text.count("?")
    visual_score = caps + punct
    
    sentiment = round(abs(sentiment_analyzer.polarity_scores(text)["compound"]), 2)
    
    return {
        "Sensationalism": sens,
        "Clickbait": click,
        "Exaggeration": exag_count,
        "VisualEmphasis": visual_score,
        "EmotionalIntensity": sentiment
    }

def predict_news(text):
    """Main classification function using the saved notebook models"""
    # Asset paths
    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(current_dir, "models", "model.pkl")
    vectorizer_path = os.path.join(current_dir, "models", "vectorizer.pkl")
    
    try:
        # Load models
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        with open(vectorizer_path, "rb") as f:
            vectorizer = pickle.load(f)
            
        # Transform and classify
        cleaned = clean_text(text)
        vec = vectorizer.transform([cleaned])
        
        # Check if model is LinearSVC or LogisticRegression
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(vec)[0][1]
            credibility = round(prob * 100, 2)
        else:
            # For LinearSVC or similar that don't have predict_proba
            prediction = model.predict(vec)[0]
            credibility = 100.0 if prediction == 1 else 0.0

        # Get style metadata
        metrics = get_style_metrics(text)
        
        return {
            "credibility": credibility,
            "metrics": metrics,
            "verdict": "REAL" if credibility >= 50 else "FAKE"
        }
    except Exception as e:
        print(f"Prediction Error: {e}")
        return None
