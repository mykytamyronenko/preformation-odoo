from models.animal import animal

class chat(animal):
    def __init__(self,
                 nom,
                 poids,
                 taille,
                 sexe,
                 age,
                 age_humain,
                 date_arrivee,
                 caractere: str,
                 griffe_coupee: bool,
                 poil_long: bool
                 ):
        super().__init__(nom, poids, taille, sexe, age, age_humain, date_arrivee)
        self.caractere = caractere
        self.griffe_coupee = griffe_coupee
        self.poil_long = poil_long
        self.deces_prob = 0.005

        def crier(self) -> str:
            return super().crier() + "MEOW"

        def calcule_age_humain(self, age) -> int:
            return super().calcule_age_humain(age) * 7

        @property
        def caractere(self):
            return self.__caractere

        @caractere.setter
        def caractere(self, value: str):
            if not isinstance(value, str):
                raise TypeError("Le caractere doit être valide.")
            self.__caractere = value


        
        @property
        def griffe_coupee(self):
            return self.__griffe_coupee

        @griffe_coupee.setter
        def griffe_coupee(self, value: bool):
            if not isinstance(value, bool):
                raise TypeError("Le type doit être boolean.")
            self.__griffe_coupee = value


        @property
        def poil_long(self):
            return self.__poil_long

        @poil_long.setter
        def poil_long(self, value: bool):
            if not isinstance(value, bool):
                raise TypeError("Le type doit être boolean.")
            self.__poil_long = value


        @property
        def poil_long(self):
            return self.__poil_long

        @poil_long.setter
        def poil_long(self, value: bool):
            if not isinstance(value, bool):
                raise TypeError("Le type doit être boolean.")
            self.__poil_long = value