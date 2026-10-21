from models.proprietaire import proprietaire

class maison:
    def __init__(self, rue: str, numero: int, nb_fenetre: int) -> None:
        if numero <= 0:
            raise ValueError("Le numéro d'une maison ne peut pas être 0 ou négatif.")

        if nb_fenetre <= 0:
            raise ValueError("Le nombre de fenêtres ne peut pas être 0 ou négatif.")

        self.rue = rue
        self.numero = numero
        self.nb_fenetre = nb_fenetre


    @property
    def rue(self) -> str:
        return self._rue

    @rue.setter
    def rue(self, nouvelle_rue: str) -> None:
        self._rue = nouvelle_rue

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, nouveau_numero: int) -> None:
        self._numero = nouveau_numero


    @property
    def nb_fenetre(self) -> int:
        return self._nb_fenetre

    @nb_fenetre.setter
    def nb_fenetre(self, nouveau_nb_fenetre: str) -> None:
        self._nb_fenetre = nouveau_nb_fenetre


    def to_string(self) -> str:
        return f"Cette maison a {self.nb_fenetre} nombres de fenêtre" \
            f" et son adresse est : {self.rue} {self.numero}."