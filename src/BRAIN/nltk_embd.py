import json
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.DATA.prompts import Dic  


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
# Preprocess the text by tokenizing, removing stopwords, and stemming
# Preprocess the text by tokenizing, removing stopwords, and lemmatizing
def preprocess_text(text):
    
    custom_stop_words = [
    'a', 'an', 'the', 'is', 'it', 'to', 'and', 'of', 'in', 'for', 'on', 'with', 
    'at', 'by', 'from', 'as', 'that', 'which', 'this', 'these', 'those', 'has', 
    'have', 'had', 'were', 'was', 'be', 'been', 'being', 'are', 'am', 'or', 
    'but', 'if', 'when', 'then', 'else', 'so', 'more', 'less', 'some', 'many', 
    'each', 'every', 'most', 'other', 'own', 'same', 'such', 'only', 'just', 
    'also', 'how', 'where', 'what', 'why', 'who', 'whom', 'whose', 'which',
    'the', 'a', 'are', 'your', 'in', 'with', 'to', 'and', 'as', 'for', 'on', 
    'task', 'role', '.']

    #stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text.lower())
    tagged_tokens = nltk.pos_tag(tokens)
    tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(tag)) for token, tag in tagged_tokens if token.isalnum() and token not in custom_stop_words]
    return ' '.join(tokens)

# Train the TF-IDF vectorizer on the dataset
def train_tfidf_vectorizer(dataset):
    if not isinstance(dataset, list) or not all(isinstance(entry, dict) for entry in dataset):
        raise ValueError("Dataset should be a list of dictionaries")

    corpus = [preprocess_text(entry['content']) for entry in dataset]
    vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_df=0.1, min_df=1)
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X

# Create a dataset from the provided dictionary
def create_dataset(dic):
    return [{'type': key, 'content': value.get('role', ''), 'prompt': value.get('prompt', '')} for key, value in dic.items()]

# Retrieve the most relevant content based on the query
def get_content(query, vectorizer, X, dataset):
    query = preprocess_text(query)
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, X)
    
    # Debug: Print similarities to check what's going wrong
    #print("Similarities:", similarities)
    
    best_match_index = similarities.argmax()
    
    # Debug: Print best match index and corresponding entry
    print("Best match index:", best_match_index)
    
    matched_entry = dataset[best_match_index]
    return {
        'type': matched_entry['type'],
        'content': matched_entry['content'],
        'prompt': matched_entry['prompt']
    }

# Main function to process the user query
def nltk_sim_prompt(text):
    # Uncomment these lines if you haven't downloaded the NLTK resources
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    dataset = create_dataset(Dic)
    vectorizer, X = train_tfidf_vectorizer(dataset)
    result = get_content(text, vectorizer, X, dataset)
    return result['type']

# Example usage
if __name__ == "__main__":
    nltk_sim_prompt("tell me a joke")
