from typing import List  # Add this import
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Charger le modèle de SentenceTransformer
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def get_embeddings(competences: List[str]):
    """
    Obtenir l'embedding moyen des compétences fournies.
    """
    embeddings = model.encode(competences)
    return embeddings.mean(axis=0)  # Compute the mean embedding

def calculate_similarity(embedding1, embedding2):
    """
    Calculer la similarité cosinus entre deux embeddings.
    """
    return cosine_similarity([embedding1], [embedding2])[0][0]