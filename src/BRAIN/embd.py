# Make sure to `pip install openai` first
from src.BRAIN.lm_ai import client 
import numpy as np
from src.DATA.prompts import Dic 
from functools import lru_cache 
#from src.BRAIN
def get_embedding(text:str, model="nomic-ai/nomic-embed-text-v1.5-GGUF") -> list[float]:
    text = text.replace("\n", " ").strip()
    try:
        embdedding = client.embeddings.create(input=[text], model=model).data[0].embedding
    except Exception as e:
        pass


def cosine_similarity(embedding1:list[float], embedding2:list[float]) -> float:
    dot_product = np.dot(embedding1, embedding2)
    norm_embedding1 = np.linalg.norm(embedding1)
    norm_embedding2 = np.linalg.norm(embedding2)
    similarity = dot_product / (norm_embedding1 * norm_embedding2)
    return similarity

def find_percentage(similarity_score):
    return round(similarity_score * 100)

# Applying caching to the get_embedding function as well
@lru_cache(maxsize=128)
def get_embedding_cached(prompt):
    return get_embedding(prompt)


def similar_prompt(prompt:str , threshold = 55) -> str:
    embedding1 = get_embedding_cached(prompt.lower().strip())
    content_type = None 
    maximum = float('-inf')
    
    for key , val in Dic.items():
        embedding2 = get_embedding_cached(val['role'])
        
        similarity_score = cosine_similarity(embedding1 , embedding2)
        percentage = find_percentage(similarity_score)
        if similarity_score > maximum and percentage > threshold:
            maximum = similarity_score 
            content_type = key 
            
    # in this case we send prompt to .
    if not content_type:
        maximum = 0.01
        content_type = f"chat + {prompt}"
        
    print(get_embedding_cached.cache_info())
    print(f"The most similar content type is: {content_type} with a similarity score of {find_percentage(maximum)}")
    return content_type 

#print(get_embedding_cached.cache_info())

# prompt = "tell me a story"
# similar_prompt(prompt)
# # embdeing1 = get_embedding(prompt)
# # # similarity = cosine_similarity(embedding1, embedding2)
# # # print(f'Cosine similarity: {similarity}')

# # print(get_embedding("Once upon a time, there was a cat."))
