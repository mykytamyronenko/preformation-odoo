from models.maison import maison

class village:
    def __init__(self, nom: str, nb_maison: int = 0, num_des_maisons: list[int] = []) -> None:
        if nb_maison < 0:
            raise ValueError("Le nombre de maison ne peut pas être négatif.")

        self.nom = nom
        self.nb_maison = nb_maison
        self.num_des_maisons = num_des_maisons

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, nouveau_nom: str) -> None:
        self._nom = nouveau_nom


    @property
    def nb_maison(self) -> int:
        return self._nb_maison

    @nb_maison.setter
    def nb_maison(self, nouveau_nb_maison: int) -> None:
        self._nb_maison = nouveau_nb_maison


    def construire_maison(self, maison: int) -> None:
        self.nb_maison += maison
        for i in range(maison):
            self.num_des_maisons.append(i)

    def detruire_maison(self, maison: int) -> None:
        self.nb_maison -= maison


    def to_string(self) -> str:
        return f"Ce village se nomme '{self.nom}' et a {self.nb_maison} maison(s)."

    # def liste_des_maisons(self) -> str:
    #     for i in range(len(self.num_des_maisons)):
    #         print(f"maison avec n° : {self.num_des_maisons[i]}")