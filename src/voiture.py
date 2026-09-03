from pydantic import BaseModel


class Voiture(BaseModel):
    marque: str
    modele: str
    couleur: str
    km: int


