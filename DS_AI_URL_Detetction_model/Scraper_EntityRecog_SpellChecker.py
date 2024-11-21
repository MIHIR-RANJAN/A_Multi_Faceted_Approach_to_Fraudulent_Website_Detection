#website Scrapper

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from pathlib import Path
import os
from transformers import pipeline
from nltk.tokenize import sent_tokenize
from tqdm import tqdm
import re
from spellchecker import SpellChecker

def scrape_website(url, output_folder):
    """
    Scrapes all text content from a website and saves it to a text file.
    
    Args:
        url (str): The website URL to scrape
        output_folder (str): The folder path where the output file will be saved
    """
    try:
        # Convert to Path object for better path handling
        output_path = Path(output_folder)
        
        # Print current working directory
        print(f"Current working directory: {os.getcwd()}")
        
        # Create full directory path if it doesn't exist
        output_path.mkdir(parents=True, exist_ok=True)
        print(f"Created/verified directory: {output_path.absolute()}")
        
        # Send HTTP request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        print(f"Fetching content from: {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(['script', 'style']):
            script.decompose()
            
        # Get text content
        text_content = soup.get_text(separator='\n', strip=True)
        
        # Generate output file path
        output_file = output_path / 'website.txt'
        
        # Save content to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Source URL: {url}\n\n")
            f.write(text_content)
            
        print(f"\nFile saved successfully!")
        print(f"File location: {output_file.absolute()}")
        print(f"File size: {output_file.stat().st_size / 1024:.2f} KB")
        
        # Verify file exists and is accessible
        if output_file.exists():
            print("File verification successful - file exists and is accessible")
            
            # Show how to access the folder in file explorer
            if os.name == 'nt':  # Windows
                print(f"\nTo open the folder in Windows Explorer, run:")
                print(f"explorer {output_file.parent}")
            else:  # MacOS/Linux
                print(f"\nTo open the folder in Finder/File Explorer, run:")
                print(f"open '{output_file.parent}'")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage
# if __name__ == "__main__":
#     website_url = "https://goa.nfsu.ac.in/"  
#     save_folder = "/Users/doctorranjan/Desktop/NFSU/DS_AI_project/DS_AI_Phishing_URL_Detetction"
#     scrape_website(website_url, save_folder)


#ORG recog 

class OrganizationRecognizer:
    def __init__(self):
        """Initialize the transformer-based NER model."""
        #print("Loading transformer model...")
        self.ner_transformer = pipeline("ner", model="dslim/bert-base-NER")
        #print("Transformer model loaded successfully!")

    def analyze_text(self, text):
        """Extract organization entities and calculate confidence scores."""
        sentences = sent_tokenize(text)  # Split the text into sentences
        org_entities = []
        
        #print("Analyzing text...")
        for sentence in tqdm(sentences, desc="Processing sentences"):
            try:
                results = self.ner_transformer(sentence)
                for result in results:
                    if result['entity'] == 'B-ORG':  # Look for "ORGANIZATION" entities
                        org_entities.append(result['score'])
            except Exception as e:
                print(f"Error processing sentence: {sentence}\n{e}")

        return org_entities

def process_text_file(file_path):
    """Process a text file and calculate average confidence for organization entities."""
    try:
        #print(f"Reading file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Initialize recognizer
        recognizer = OrganizationRecognizer()

        # Analyze text for organization entities
        org_entities = recognizer.analyze_text(text)

        # Calculate and display the average confidence score
        if org_entities:
            avg_confidence = sum(org_entities) / len(org_entities)
            print(f"\nAverage confidence score for ORGANIZATION entities: {avg_confidence:.3f}")
        else:
            print("\nNo ORGANIZATION entities found in the text.")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

# if __name__ == "__main__":
#     # Input file path
#     input_file = "/Users/doctorranjan/Desktop/NFSU/DS_AI_project/DS_AI_Phishing_URL_Detetction/Testwebsite.txt".strip()

#     if not os.path.isfile(input_file):
#         print("Invalid file path. Please check and try again.")
#     else:
#         process_text_file(input_file)


#speeling Checker



def extract_valid_words(text):
    """
    Extract words that contain only alphabetic characters.
    Excludes symbols, numbers, or mixed content.
    """
    return re.findall(r'\b[a-zA-Z]+\b', text)

def check_spelling(words):
    """
    Check spelling for the list of valid words and return corrections.
    """
    spell = SpellChecker()
    misspelled = spell.unknown(words)
    corrections = {}

    for word in misspelled:
        # Suggest the most likely correction
        corrections[word] = spell.correction(word)
    
    return corrections, len(misspelled)

def process_text_file(file_path):
    """
    Process a text file to find and correct spelling errors.
    Also calculate the percentage of correctly spelled words.
    """
    try:
        # Read the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        #print("Extracting valid words...")
        valid_words = extract_valid_words(text)

        #print(f"Total valid words found: {len(valid_words)}")
        
        #print("Checking for spelling errors...")
        corrections, misspelled_count = check_spelling(valid_words)

        # Calculate percentage of correctly spelled words
        total_words = len(valid_words)
        correct_words_count = total_words - misspelled_count
        accuracy_percentage = (correct_words_count / total_words) * 100 if total_words > 0 else 0

        # Print percentage
        print(f"\nPercentage of correctly spelled words: {accuracy_percentage:.2f}%")
    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

# if __name__ == "__main__":
#     file_path = "/Users/doctorranjan/Desktop/NFSU/DS_AI_project/DS_AI_Phishing_URL_Detetction/website.txt".strip()
    
#     if not file_path or not file_path.endswith('.txt'):
#         print("Please provide a valid text file.")
#     else:
#         process_text_file(file_path)
