#sentiment Analysis

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def load_sentiment_analyzer():
    """Load a sentiment analysis pipeline using a specific pre-trained model."""
    model_name = "cardiffnlp/twitter-roberta-base-sentiment"
    
    try:
        # Load the tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        
        # Create a pipeline
        sentiment_analyzer = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
        return sentiment_analyzer
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def analyze_sentiment(sentiment_analyzer, text):
    """Analyze sentiment using the provided analyzer."""
    results = sentiment_analyzer(text[:512])  # Limit to 512 characters for efficiency
    return results

def process_text_file(file_path):
    """Reads text from a file and performs sentiment analysis."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        if not text.strip():
            print("The file is empty. No text to analyze.")
            return
        
        print("Loading sentiment analyzer...")
        sentiment_analyzer = load_sentiment_analyzer()
        
        if sentiment_analyzer is None:
            print("Failed to load the sentiment analyzer.")
            return
        
        print("Analyzing sentiment...")
        sentiment_results = analyze_sentiment(sentiment_analyzer, text)
        
        for result in sentiment_results:
            print(f"Label: {result['label']}, Confidence: {result['score']:.2f}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error processing file: {e}")

# if __name__ == "__main__":
#     file_path = "/Users/doctorranjan/Desktop/NFSU/DS_AI_project/DS_AI_Phishing_URL_Detetction/Testwebsite.txt" 
#     process_text_file(file_path)
    
    
# For this model, the labels correspond to:

# LABEL_0 = Negative sentiment
# LABEL_1 = Neutral sentiment
# LABEL_2 = Positive sentiment