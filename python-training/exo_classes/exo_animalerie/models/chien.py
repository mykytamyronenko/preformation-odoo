from models.animal import animal

class chien(animal):
    def __init__(self,
                 nom,
                 poids,
                 taille,
                 sexe,
                 age,
                 age_humain,
                 date_arrivee,
                 couleur_collier: str,
                 dresse: bool,
                 race: str
                 ):
        super().__init__(nom, poids, taille, sexe, age, age_humain, date_arrivee)
        self.couleur_collier = couleur_collier
        self.dresse = dresse
        self.race = race
        self.deces_prob = 0.01


    def crier(self):
        return super().crier() + "WOUF"


    def calcule_age_humain(self, age):
        return super().calcule_age_humain(age) * 6


    @property
    def couleur_collier(self):
        return self.__couleur_collier

    @couleur_collier.setter
    def couleur_collier(self, value: str):
        if not isinstance(value, str):
            raise TypeError("La couleur doit être valide.")
        self.__couleur_collier = value


    @property
    def dresse(self):
        return self.__dresse

    @dresse.setter
    def dresse(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("Le type doit être boolean.")
        self.__dresse = value


    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, value: str):
        if not isinstance(value, str):
            raise TypeError("La race doit être valide.")
        self.__race = value