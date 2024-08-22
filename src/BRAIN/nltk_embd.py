import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.DATA.prompts import Dic  # Assuming Dic is defined in qna.py
from src.DATA.stop_words import custom_stop_words

# Uncomment these lines if you haven't downloaded the NLTK resources


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
    #stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text.lower())
    tagged_tokens = nltk.pos_tag(tokens)
    filter_text = [
        lemmatizer.lemmatize(token, get_wordnet_pos(tag)) 
        for token, tag in tagged_tokens 
        if token.isalnum() and token not in custom_stop_words
    ]
    return ' '.join(filter_text)

# Train the TF-IDF vectorizer on the dataset
def train_tfidf_vectorizer(dataset):
    if not isinstance(dataset, list) or not all(isinstance(entry, dict) for entry in dataset):
        raise ValueError("Dataset should be a list of dictionaries")

    corpus = [preprocess_text(entry['content']) for entry in dataset]
    #ngram_range=(1, 3), max_df=0.1, min_df=1
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus).toarray()
    return vectorizer, X

# Create a dataset from the provided dictionary
def create_dataset(dic):
    return [{'type': key, 'content': value.get('role', ''), 'prompt': value.get('prompt', '')} for key, value in dic.items()]

def find_percentage(similarity_score):
    return round(similarity_score * 100)

# Retrieve the most relevant content based on the query
def get_content(query, vectorizer, X, dataset , threshold=30):
    query = preprocess_text(query)
    query_vec = vectorizer.transform([query]).toarray()
    similarities = cosine_similarity(query_vec, X)
    
    best_match_index = similarities.argmax()
    similarity_score =  find_percentage(similarities[0][best_match_index])
    
    if similarity_score >= threshold:
        content_type = dataset[best_match_index]['type']
        print(f"The most similar content type is: {content_type} with a similarity score of {similarity_score}")
        return content_type
    
    else:
        print(f"The most similar content type is: chat")
        content_type = f"chat + {query}"
        return content_type 
        
    
    
# Main function to process the user query
def nltk_sim_prompt(text):
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    dataset = create_dataset(Dic)
    vectorizer, X = train_tfidf_vectorizer(dataset)
    result = get_content(text, vectorizer, X, dataset)
    return result 

# Example usage
if __name__ == "__main__":
    nltk_sim_prompt("tell me a joke")
