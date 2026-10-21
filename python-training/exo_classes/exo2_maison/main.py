# Exo2 maison
# Simuler la vie dans un petit village dans lequel des maisons peuvent être construites à
# des adresses bien précises ou qu’elles peuvent être également détruites.
# Assurez-vous que les attributs de vos différentes classes possèdent un getter et un
# setter bien défini.
# Bonus :
# Ajouter des propriétaires aux maisons. Les propriétaires peuvent acheter et vendre les
# maisons ou bien les louer à d’autres personnes.

from models import village, maison, proprietaire

m1 = maison("Rue des rues", 1, 3)

v1 = village("The village")

print(m1.to_string())

print(v1.to_string())

v1.construire_maison(100)

print(v1.to_string())
# print(v1.liste_des_maisons())

v1.detruire_maison(20)

print(v1.to_string())