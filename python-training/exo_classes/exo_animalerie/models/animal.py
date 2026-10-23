class animal():
    def __init__(self,
                 nom: str,
                 poids: float,
                 taille: float,
                 sexe: str,
                 age: int,
                 age_humain: int,
                 date_arrivee: str) -> None:
        self.nom = nom
        self.poids = poids
        self.taille = taille
        self.sexe = sexe
        self.age = age
        self.age_humain = age_humain
        self.date_arrivee = date_arrivee

    def crier(self) -> str:
        return "Un animal fait un bruit"

    def calcule_age_humain(self, age) -> int:
        return age

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Le nom doit être valide.")
        self.__nom = value


    @property
    def poids(self):
        return self.__poids

    @poids.setter
    def poids(self, value: float):
        if not isinstance(value, float):
            raise TypeError("Le poids doit être valide.")

        if value and value < 0:
            raise ValueError("le poids doit être positif.")
        self.__poids = value


    @property
    def taille(self):
        return self.__taille

    @taille.setter
    def taille(self, value: float):
        if not isinstance(value, float):
            raise TypeError("La taille doit être valide.")

        if value and value < 0:
            raise ValueError("le taille doit être positif.")
        self.__taille = value


    @property
    def sexe(self):
        return self.__sexe

    @sexe.setter
    def sexe(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Le sexe doit être valide.")

        if value and value not in ("male", "female"):
            raise ValueError("Le sexe doit être soit male soit female.")
        self.__sexe = value


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int):
            raise TypeError("L'age doit être valide.")

        if value and value < 0:
            raise ValueError("l'age doit être positif.")
        self.__age = value


    @property
    def age_humain(self):
        return self.__age_humain

    @age_humain.setter
    def age_humain(self, value: int):
        if not isinstance(value, int):
            raise TypeError("L'age humain doit être valide.")

        if value and value < 0:
            raise ValueError("l'age humain doit être positif.")
        self.__age_humain = value


    @property
    def date_arrivee(self):
        return self.__date_arrivee

    @date_arrivee.setter
    def date_arrivee(self, value: str):
        if not isinstance(value, str):
            raise TypeError("La date d'arrivée doit être valide.")
        self.__date_arrivee = value


    def affichage(nom, poids, taille, sexe, age, age_humain, date_arrivee) -> str:
        return f"nom : {nom} \
            poids : {poids} \
            taille : {taille} \
            sexe : {sexe} \
            age : {age} \
            age_humain : {age_humain} \
            date_arrivee : {date_arrivee}"