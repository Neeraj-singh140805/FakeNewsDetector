# 📰 Fake News Detection & Writing-Style Analysis System

---

## 1. Project Overview

This project builds a **machine learning–based fake news detection system** combined with **writing-style analysis metrics**.

The system:

- Classifies news articles as **Real (1)** or **Fake (0)**
- Generates a **credibility score (0–100)**
- Analyses writing style using behavioural and linguistic signals
- Evaluates performance using **Accuracy, ROC-AUC, and Confusion Matrix**

The goal is not only prediction but also **interpretable credibility analysis** of news articles.

---

## 2. Libraries & Dependencies

**Core**
- pandas
- numpy
- re
- string  

**Machine Learning (scikit-learn)**
- train_test_split
- TfidfVectorizer
- LogisticRegression
- accuracy_score
- classification_report
- roc_auc_score
- confusion_matrix  

**NLP**
- vaderSentiment  

---

## 3. Dataset Preparation

Two datasets were used:

- **True.csv → label = 1**
- **Fake.csv → label = 0**

Steps:

1. Load both datasets  
2. Assign labels  
3. Merge into one dataframe  
4. Combine title + text into `content`  
5. Verify class balance  

Final structure:

| content | label |
|--------|------|
| article text | 0 / 1 |

---

## 4. Text Cleaning

A custom cleaning function removes noise and leakage.

Cleaning includes:

- Lowercasing  
- Removing publisher markers (e.g., Reuters)  
- Removing location/time tokens  
- Removing punctuation & numbers  
- Normalizing whitespace  

This prevents the model from learning dataset artifacts instead of real linguistic patterns.

---

## 5. Feature Engineering (TF-IDF)

Text is converted into vectors using:

TF-IDF captures important words and phrases while reducing common terms, creating a suitable representation for linear classifiers.

---

## 6. Model Training

**Model:** Logistic Regression  

Reasons:

- Strong baseline for text classification  
- Fast and stable  
- Interpretable  
- Effective with TF-IDF  

Training:

- 80/20 stratified split  
- Train on TF-IDF features  
- Predict on test set  

---

## 7. Model Evaluation

Metrics used:

- Accuracy  
- ROC-AUC  
- Precision / Recall / F1  
- Confusion Matrix  

Interpretation focus:

- False Positive → Fake predicted Real  
- False Negative → Real predicted Fake  

---

## 8. Writing-Style Analysis Metrics

The system includes rule-based linguistic indicators.

### Sensational Score
Frequency of dramatic words.

### Clickbait Score
Presence of attention-bait phrases.

### Exaggeration Score
Absolute and extreme wording.

### Visual Emphasis Score
ALL CAPS, !, ? usage.

### Emotional Intensity
VADER sentiment magnitude.

These metrics provide behavioural insight alongside model prediction.

---

## 9. Article Analysis Output

For each article the system produces:

- Credibility Score (0–100)
- Predicted Class
- Sensational Score
- Clickbait Score
- Exaggeration Score
- Visual Emphasis Score
- Emotional Intensity Score

---

## 10. System Flow

---

## 11. Strengths

- Interpretable features  
- Leakage-aware preprocessing  
- Behavioural analysis layer  
- Balanced dataset  
- Transparent predictions  

---

## 12. Limitations

- Dataset bias (Reuters-heavy)
- Linear model limitations
- Rule-based style metrics
- No cross-domain testing

---

# 13. Additional Work

## Multi-Matrix Credibility Modeling (Exploratory)

A second approach was explored using three credibility matrices:

- Linguistic style signals  
- Semantic consistency signals  
- Source reliability signals  

The pipeline included URL text extraction and feature fusion.  
However, large-scale article extraction produced incomplete and biased text, so this approach was paused to maintain dataset reliability.

---

## Merged Multi-Source Dataset Experiment

A third experiment attempted merging multiple extracted news datasets to expand coverage before applying the matrix pipeline.  
Due to inconsistencies and extraction bias across sources, this dataset was not used for final modeling.

---

# 14. Conclusion

This project demonstrates a practical fake-news detection system combining:

- TF-IDF text modeling  
- Logistic regression classification  
- Writing-style credibility metrics  

It emphasizes **interpretable misinformation detection** rather than black-box prediction.

---
# 15. Full Report 
**Download Detailed Project Report (PDF)**
👉 [View Report](Report.pdf)

# 15. Full Project Report  

**Download Detailed Project Report (PDF)**  
👉 [View Report](News Credibility Detection & Writing Style Analysis System Report.pdf)

**Project:** Fake News Detection & Credibility Analysis  
Machine Learning & NLP
