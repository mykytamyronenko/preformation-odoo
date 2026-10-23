from models.animal import animal

class oiseau(animal):
    def __init__(self,
                 nom,
                 poids,
                 taille,
                 sexe, age,
                 age_humain,
                 date_arrivee,
                 couleur: str,
                 lieu_vie: str
                 ):
        super().__init__(nom, poids, taille, sexe, age, age_humain, date_arrivee)
        self.deces_prob = 0.03
        self.couleur = couleur
        self.lieu_vie = lieu_vie


    def crier(self):
        return super().crier() * "CUI-CUI"

    def calcule_age_humain(self, age):
        return super().calcule_age_humain(age) * 4


    @property
    def couleur(self):
        return self.__couleur

    @couleur.setter
    def couleur(self, value: str):
        if not isinstance(value, str):
            raise TypeError("La couleur doit être valide.")
        self.__couleur = value


    @property
    def lieu_vie(self):
        return self.__lieu_vie

    @lieu_vie.setter
    def lieu_vie(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Le lieu de vie doit être valide.")

        if value and value not in ("voliere", "cage"):
            raise ValueError("Le lieu de vie doit être une volière ou une cage.")
        self.__lieu_vie = value