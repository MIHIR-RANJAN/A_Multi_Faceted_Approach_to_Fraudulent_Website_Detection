# A Multi-Faceted Approach to Fraudulent Website Detection: Integrating URL Features and Content Analysis


## Overview
This project focuses on detecting fraudulent websites by integrating URL analysis and content-based techniques. The system evaluates websites based on various parameters such as URL structure, sentiment analysis, organizational entity recognition, and spelling checks. The approach enhances traditional fraud detection by incorporating machine learning models and NLP-based sentiment analysis.

## Features
- **URL-Based Analysis:** Examines 30 features of URLs, including domain length, HTTPS usage, and subdomain count.
- **Sentiment Analysis:** Utilizes Twitter RoBERTa to assess the intent of website content.
- **Organizational Entity Recognition:** Extracts and verifies organization names mentioned on the website.
- **Spelling Checker:** Detects subtle inconsistencies in website text.
- **Machine Learning Model:** Uses a Gradient Boosting Classifier (GBC) to predict fraudulent websites.

## Methodology
### 1. URL Detection Model
- Extracts URL features.
- Trains multiple classifiers (Logistic Regression, Random Forest, SVM, GBC).
- Selects the best-performing model for prediction.

### 2. Sentiment Analysis
- Uses the pre-trained `cardiffnlp/twitter-roberta-base-sentiment` model.
- Classifies content into positive, neutral, or negative sentiment.

### 3. Organizational Entity Recognition
- Applies a transformer-based Named Entity Recognition (NER) model.
- Cross-references identified organizations for legitimacy.

### 4. Spelling Checker
- Identifies and corrects spelling errors.
- Calculates accuracy scores for content consistency.

### 5. Weighted Scoring System
- URL Features: **30%**
- Sentiment Analysis: **30%**
- Organization Recognition: **20%**
- Spelling Checker: **20%**

## Results
- URL detection accuracy: **94.9%**
- Sentiment analysis, entity recognition, and spelling checks combined to improve fraud detection.
- Weighted scoring system provides comprehensive fraud detection.

## Future Enhancements
- **Logo Detection:** Identify misuse of brand logos.
- **Custom NLP Model:** Develop a dedicated sentiment analysis model.
- **Real-Time Updates:** Implement active learning techniques.
- **Multilingual Support:** Expand detection to non-English websites.
- **Browser Extension/API:** Enhance accessibility for real-world applications.

## References
Refer to the research paper for an in-depth literature review and methodology details.
