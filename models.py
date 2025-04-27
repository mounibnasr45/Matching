from pydantic import BaseModel
from typing import List

# Modèle pour un profil
class Profile(BaseModel):
    id: int
    nom: str
    competences: List[str]

# Modèle pour une demande de compétences
class SkillRequest(BaseModel):
    id: int
    competences_recherchees: List[str]
