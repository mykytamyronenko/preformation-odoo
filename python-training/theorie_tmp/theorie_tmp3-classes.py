# () = héritage, avec classe parent et arguments
class TechnoCite(Organization):
    # self équivalent à this
    def __init__(self, title:str, author, year, publisher):
        super().__init__()
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher


1 + 2 + \
3


# en pyhton → un script = une classe, car nom de fichier = nom de classe,
# ici le fichier doit être nommé TechnoCite
# CamelCase pour les classe
            
# __init__
# __str__
# __add__ __mul__ __div__
# __repr__ → debugage
# __call__

import pandas as pd

pd.array([1, 2, 3], dtype="Int64")

# peu d'interface en python

# getter, setter dans tous les langagues


"""
encoe optimisation
"""


# vaut mieux que ça fonctionne et mal opti quel quelque chose qui ne fonctionne pas,
# donc faire un truc simple puis optimiser



# range(len) est moins bien que →
# [x for x in range(10) if x % 2 == 0] → crée liste en même temps

# mots = ["papa", "maman", "fils", "fille", "chien"]
# {mot : len{mot} for mot in mots} → création de dico à partir d'une liste
# {num : liste.count(num) for num in set(liste)} → pas besoin du set
# set plus rapide quand on a des doublons (exemple sur ligne juste au dessus)



for i, elem in enumerate(mots):
    print(f"A l'index {i} se trouve le mot {elem}")

# 0 : papa
# 1 : maman
# ...

# zip → jamais utilisé


# a, b = b, a → échanger les valeurs

# liste[:] → très imortant
# liste[::-1] → reverse
# liste[start:end-1,-1]

# import collection est cool mais on ne sait pas si on pourra l'utiliser (counter est le plus cool)