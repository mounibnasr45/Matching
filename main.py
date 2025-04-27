from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from utils import calculate_similarity, get_embeddings
from models import Profile, SkillRequest
import os
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
port = int(os.environ.get("PORT", 8000))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only. Restrict in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Charger les profils et compétences depuis les fichiers CSV
profiles_df = pd.read_csv('data/profiles.csv')
skills_df = pd.read_csv('data/skills.csv')

# Préparer les profils et compétences sous forme d'objets
profiles = [Profile(id=row['id'], nom=row['nom'], competences=row['competences'].split(", ")) for _, row in profiles_df.iterrows()]
skills = [SkillRequest(id=row['id'], competences_recherchees=row['competences_recherchees'].split(", ")) for _, row in skills_df.iterrows()]

@app.get("/")
def read_root():
    return {"message": "Système de matching des compétences"}

@app.post("/matching/")
def get_matching_profiles(skill_request: SkillRequest):
    # Embeddings des compétences recherchées
    skill_request_embedding = get_embeddings(skill_request.competences_recherchees)
    
    # Calcul de la similarité avec tous les profils
    matching_profiles = []
    for profile in profiles:
        profile_embedding = get_embeddings(profile.competences)
        similarity_score = calculate_similarity(skill_request_embedding, profile_embedding)
        matching_profiles.append({
            "profil_id": profile.id,
            "nom": profile.nom,
            "competences": profile.competences,
            "score": float(similarity_score)  # Convert numpy.float32 to Python float
        })
    
    # Trier par score de similarité décroissant
    sorted_profiles = sorted(matching_profiles, key=lambda x: x['score'], reverse=True)
    
    return sorted_profiles
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
