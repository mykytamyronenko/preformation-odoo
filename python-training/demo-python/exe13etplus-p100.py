"""
algo fr non faite -> présent sur le github -> 3exo-boucles.algo
"""

"""
exo13-À l’aide d’une boucle, afficher la table de multiplication par 2. 
Ensuite, coder votre algorithme en Python.
- récupérer la table à afficher 
- récupérer le nombre d'éléments à afficher
"""

even_numbers_list = list()
# even_numbers_list = [], même chose ici

for i in range(0,101,2):
    if i != 0:
        print(i)
        even_numbers_list.append(i)
print(even_numbers_list)

for j in range(0,len(even_numbers_list),1):
    j += 1
print(j)


"""
exo14-Reprenez l’algorithme du lanceur de balles de tennis et
faites en sorte qu’il lance une balle tant que le stock n’est pas vide.
Il y a donc 2 variables stock_balles et pret , panier_vide

- afficher à chaque balle lancé le nombre de balle restante
- afficher un message lors de l'arret
"""

ready = False
panier_vide = True

stock_balls = int(input("Combien de balles avez vous mis : "))

if stock_balls > 0:
    panier_vide = False

while panier_vide == False:
    response = input("Etes-vous prêt? y-n :")
    if response == 'y':
        print("Balle lancé")
        ready = True
        stock_balls -= 1
        print(f"il reste {stock_balls} balles")
    if stock_balls < 1:
        panier_vide = True
    ready = False
    

"""
• exo15-À l’aide de deux boucles, 
afficher les tables de multiplication de 1 à 9. 
Ensuite, coder votre algorithme en Python.
"""

for i in range(1,10,1):
    print(f"Table de {i} : ")
    for j in range(1,11,1):
        print(f"{i}x{j} = {i * j}")

"""
Jeu du plus ou moins

Génération d'un nombre aléatoire 
- from random import randint
result = randint(1,10)

dans une boucle 
    - demander à l'utilisateur d'entrez une valeur
    - afficher plus ou moins 
    - compter le nombre coups
    
    - afficher un message lorsqu'il à trouvez le nombre avec le nombre de coups
"""

from random import randint
result = randint(1, 10)

number_of_tries = 0

victory = False

while not victory:
    number_of_tries += 1
    user_number = int(input("Devinez le nombre : "))

    if user_number > result:
        print("C'est moins.")
    elif user_number < result:
        print("C'est plus.")
    else:
        victory = True
        print("C'est gagné !")
        print(f"Le nombre est : {result}")
        print(f"Nombre d'essai(s) : {number_of_tries}")
