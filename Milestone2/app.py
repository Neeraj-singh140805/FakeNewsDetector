import streamlit as st
from main import run_pipeline

st.set_page_config(page_title="Fake News Detector", layout="wide")

st.title("🧠 Fake News Detector (Agentic AI)")
st.markdown("Analyze news using **Machine Learning + RAG + LLM reasoning**")

st.divider()

query = st.text_area("📝 Enter news text here:", height=150)

if st.button("🔍 Analyze"):

    if not query.strip():
        st.warning("⚠️ Please enter some text")
    else:
        with st.spinner("Analyzing..."):
            result = run_pipeline(query)

        st.divider()

        if "error" in result:
            st.error(result["error"])

        else:
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📊 Model Prediction")
                st.metric(label="Verdict", value=result["ml"]["verdict"])
                st.metric(label="Credibility", value=f"{result['ml']['credibility']}%")

                st.subheader("📈 Confidence Score")
                confidence = result.get("confidence", 0)
                st.progress(confidence / 100)
                st.write(f"{confidence}%")

            with col2:
                st.subheader("🧾 Linguistic Analysis")
                st.json(result["metrics"])

            st.divider()

            st.subheader("📰 Evidence Retrieved")

            if result["docs"]:
                for i, doc in enumerate(result["docs"], 1):
                    st.markdown(f"**{i}. {doc.get('title', 'No Title')}**")
                    st.write((doc.get("content", "")[:200] + "...") if doc.get("content") else "")
                    
                    if doc.get("url"):
                        st.markdown(f"[Read full article]({doc['url']})")
                    
                    if doc.get("source"):
                        st.caption(f"Source: {doc['source']}")
                    
                    st.divider()
            else:
                st.info("No relevant news articles found")

            st.divider()

            st.subheader("🧠 Fact-Check Explanation")
            st.write(result["answer"])

            st.divider()

            st.caption("⚙️ Powered by ML + Retrieval-Augmented Generation + LLM reasoning")