"""
exo21-Écrire un algorithme qui saisit 6 entiers et les
stocke dans un tableau, puis affiche le contenu de ce
tableau une fois qu’il est rempli.
"""
number_list = list()

for i in range(0,6,1):
    number = int(input("Entrez un nombre : "))
    number_list.append(number)

print(number_list)


"""
exo22-BONUS : initialiser un tableau de 10 entiers avec
les valeurs 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 à
l’aide d’une boucle. Ensuite, à l’aide d’une boucle
afficher la valeur de chaque cellule du tableau avec
l’opération Ecrire().
"""

number_list2 = list()

number = 2

for i in range(2,12,1):
    number_list2.append(number)
    number = 2 ** i

print(number_list2)

for i in range(0,len(number_list2),1):
    print(number_list2[i])
