import streamlit as st
import pickle
import re
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# -------------------------
# Load model + vectorizer
# -------------------------
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

sentiment_analyzer = SentimentIntensityAnalyzer()

# -------------------------
# Style Dictionaries
# -------------------------
SENSATIONAL_WORDS = {
    "shocking", "unbelievable", "explosive",
    "disaster", "nightmare", "chaos",
    "outrageous", "incredible",
    "terrifying", "horrifying"
}

HYPERBOLE_WORDS = {
    "always", "never", "everyone", "no one",
    "worst ever", "best ever",
    "guaranteed", "totally"
}

CLICKBAIT_PATTERNS = [
    r"you won'?t believe",
    r"what happens next",
    r"number \d+",
    r"this is what happened",
    r"will blow your mind"
]

# -------------------------
# Cleaning Function
# -------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\(reuters\)', ' ', text)
    text = re.sub(r'reuters', ' ', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# -------------------------
# Style Metric Functions
# -------------------------
def sensational_score(text):
    words = re.findall(r'\w+', text.lower())
    count = sum(word in SENSATIONAL_WORDS for word in words)
    return round((count / max(len(words), 1)) * 100, 2)

def clickbait_score(text):
    return sum(bool(re.search(p, text.lower())) for p in CLICKBAIT_PATTERNS)

def exaggeration_score(text):
    lower = text.lower()
    count = sum(phrase in lower for phrase in HYPERBOLE_WORDS)
    superlatives = re.findall(r'\b\w+est\b', lower)
    return count + len(superlatives)

def visual_emphasis_score(text):
    words = text.split()
    caps = sum(word.isupper() and len(word) > 2 for word in words)
    punct = text.count("!") + text.count("?")
    return caps + punct

def emotional_intensity_score(text):
    return round(abs(sentiment_analyzer.polarity_scores(text)["compound"]), 2)

# -------------------------
# Explanation Generator
# -------------------------
def generate_explanation(credibility, sens, click, exaggeration, visual, emotional):

    reasons = []
    is_real = credibility >= 50

    if is_real:
        reasons.append(
            "The machine learning model identified structural and linguistic patterns "
            "that are commonly found in legitimate news reporting."
        )

        if sens < 3:
            reasons.append("The article contains minimal sensational wording.")

        if click == 0:
            reasons.append("No clickbait-style phrases were detected.")

        if exaggeration <= 2:
            reasons.append("The content avoids excessive exaggeration or extreme claims.")

        if emotional > 0.7:
            reasons.append(
                "Although the tone is emotionally strong, emotional reporting alone does not indicate misinformation."
            )
        else:
            reasons.append("The tone remains relatively balanced and neutral.")

        if visual > 5:
            reasons.append(
                "Some visual emphasis (capitalization or punctuation) was detected, "
                "but it was not sufficient to override credibility indicators."
            )

    else:
        reasons.append(
            "The model detected patterns that closely resemble previously identified misinformation articles."
        )

        if sens >= 3:
            reasons.append("A high level of sensational language was found.")

        if click > 0:
            reasons.append("Clickbait-style phrasing was detected.")

        if exaggeration > 2:
            reasons.append("Exaggerated or extreme language increases suspicion.")

        if emotional > 0.7:
            reasons.append("The article relies heavily on emotional intensity.")

        if visual > 5:
            reasons.append("Excessive capitalization or dramatic punctuation was identified.")

    return " ".join(reasons)

# -------------------------
# Streamlit UI
# -------------------------
st.title("📰 News Credibility Analyzer")

user_input = st.text_area("Paste News Article Here")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter text.")
    else:
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        prob_real = model.predict_proba(vec)[0][1]
        credibility = round(prob_real * 100, 2)

        st.markdown("## Credibility Analysis Report")

        if credibility >= 50:
            st.success(f"Likely REAL News ({credibility}%)")
        else:
            st.error(f"Likely FAKE News ({credibility}%)")

        st.write("---")

        # Compute Metrics
        sens = sensational_score(user_input)
        click = clickbait_score(user_input)
        exaggeration = exaggeration_score(user_input)
        visual = visual_emphasis_score(user_input)
        emotional = emotional_intensity_score(user_input)

        # Display Indicators
        st.markdown("### Writing Style Indicators")
        st.write(f"Sensational Score: {sens}")
        st.write(f"Clickbait Score: {click}")
        st.write(f"Exaggeration Score: {exaggeration}")
        st.write(f"Visual Emphasis Score: {visual}")
        st.write(f"Emotional Intensity: {emotional}")

        st.write("---")

        # Explanation Section
        st.markdown("### Why This Was Classified This Way")

        explanation = generate_explanation(
            credibility, sens, click, exaggeration, visual, emotional
        )

        st.write(explanation)