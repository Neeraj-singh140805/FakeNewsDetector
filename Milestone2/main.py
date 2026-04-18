from predict import predict_news
from rag.news_fetcher import fetch_news
from agents.analyzer import analyze


def run_pipeline(query):

    # ML prediction
    ml_result = predict_news(query)

    # Fetch news (RAG)
    docs = fetch_news(query)

    # -------- FALLBACK: No docs --------
    if not docs:
        fallback_docs = [
            "No reliable news articles were found. Use general knowledge and reasoning to evaluate this claim carefully."
        ]

        answer = analyze(query, fallback_docs)

        confidence = round(
            (ml_result["credibility"] * 0.7), 2
        )

        return {
            "ml": ml_result,
            "docs": [],
            "answer": answer,
            "metrics": ml_result["metrics"],
            "confidence": confidence
        }

    # -------- NORMAL FLOW --------
    # Extract only text for LLM (since docs are dictionaries now)
    doc_texts = [doc.get("content", "") for doc in docs if doc.get("content")]

    answer = analyze(query, doc_texts)

    confidence = round(
        (ml_result["credibility"] * 0.6) + 20,
        2
    )

    return {
        "ml": ml_result,
        "docs": docs,
        "answer": answer,
        "metrics": ml_result["metrics"],
        "confidence": confidence
    }