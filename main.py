import re
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.util import ngrams
from textstat import flesch_reading_ease, gunning_fog

# Ensure you download NLTK resources if not already done
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(f"[{string.punctuation}]", "", text.lower())
    # Tokenize words
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

# Function to calculate keyword density
def calculate_keyword_density(tokens):
    total_words = len(tokens)
    word_counts = Counter(tokens)
    keyword_density = {word: (count / total_words) * 100 for word, count in word_counts.items()}
    return keyword_density

# Function to generate n-grams
def generate_ngrams(tokens, n=2):
    n_grams = list(ngrams(tokens, n))
    return Counter(n_grams)

# Function to calculate readability metrics
def calculate_readability(text):
    readability_scores = {
        "Flesch Reading Ease": flesch_reading_ease(text),
        "Gunning Fog Index": gunning_fog(text),
        "Average Sentence Length": len(word_tokenize(text)) / len(sent_tokenize(text)),
    }
    return readability_scores

# Main function to analyze SEO metrics from a text file
def analyze_seo(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Preprocess text
    tokens = preprocess_text(text)
    print(f'Total number of tokens : {tokens}')

    # Keyword density analysis
    keyword_density = calculate_keyword_density(tokens)

    # N-gram analysis (bigrams and trigrams)
    bigrams = generate_ngrams(tokens, n=2)
    trigrams = generate_ngrams(tokens, n=3)

    # Readability metrics
    readability_scores = calculate_readability(text)

    # Results dictionary
    results = {
        "Keyword Density": keyword_density,
        "Top Bigrams": bigrams.most_common(10),
        "Top Trigrams": trigrams.most_common(10),
        "Readability Scores": readability_scores,
    }

    print(f'result will be : {results}')

    return results

# Example usage
if __name__ == "__main__":
    file_path = "Kundan Jewellery.txt"  # Replace with your file path
    print(f'file path is : {file_path}')
    seo_results = analyze_seo(file_path)
    
    
    print("Keyword Density:")
    print(seo_results["Keyword Density"])
    
    print("\nTop Bigrams:")
    print(seo_results["Top Bigrams"])
    
    print("\nTop Trigrams:")
    print(seo_results["Top Trigrams"])
    
    print("\nReadability Scores:")
    print(seo_results["Readability Scores"])