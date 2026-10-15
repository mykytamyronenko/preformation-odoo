"""
algo fr non faite
"""

"""
Exercice 17 :
exo17-À l’aide d’une boucle TantQue … Faire, améliorez l’algorithme du distributeur
de boissons pour qu’il demande au client s’il désire une autre boisson (Tant qu’il en a
envie).
"""
eau = 10
fanta = 10
coca = 5
cafe = 5

user_choice = None

menu = """
coca : 1
fanta : 2
eau : 3
café : 4
"""

print(menu)

while True:
    user_choice = int(input("Entrez le numéro de la boisson : "))
    match user_choice:
        case 1:
            if coca > 0:
                print("Voici votre coca")
                coca -= 1
                print(f"stock en coca {coca}")
            else:
                print("Cette boisson n'est plus en stock")
        case 2:
            if fanta > 0:
                print("Voici votre fanta")
                fanta -= 1
                print(f"stock en fanta {fanta}")
            else:
                print("Cette boisson n'est plus en stock")
        case 3:
            if eau > 0:
                print("Voici votre eau")
                eau -= 1
                print(f"stock en eau {eau}")
            else:
                print("Cette boisson n'est plus en stock")
        case 4:
            if cafe > 0:
                print("Voici votre cafe")
                cafe -= 1
                print(f"stock en cafe {cafe}")
            else:
                print("Cette boisson n'est plus en stock")
        case _:
            print("ERROR")

    reponse17 = input("Voulez vous une autre boisson? y/n :")
    if reponse17 != "y":
        break


"""
Exercice 18 :
exo18-À l’aide d’une boucle TantQue … Faire, améliorez l’algorithme de la
calculatrice afin qu’elle demande à l’utilisateur s’il veut faire un autre calcul (tant
qu’il le désire).
"""
nb_1 = None
operateur = None
nb_2 = None

while True:
    nb_1 = int(input("Entrez le premier nombre : "))
    operateur = input("Entrez un opérateur : ")
    nb_2 = int(input("Entrez le second nombre : "))

    match operateur:
        case "+":
            print(f"{nb_1} {operateur} {nb_2} = {str(nb_1 + nb_2)}")
        case "-":
            print(f"{nb_1} {operateur} {nb_2} = {str(nb_1 - nb_2)}")
        case "*":
            print(f"{nb_1} {operateur} {nb_2} = {str(nb_1 * nb_2)}")
        case "/":
            if nb_2 == 0:
                print("La division par zéro n'eset pas possible")
            else:
                print(f"{nb_1} {operateur} {nb_2} = {str(nb_1 / nb_2)}")
        case "%":
            print(f"{nb_1} {operateur} {nb_2} = {str(nb_1 % nb_2)}")

    reponse18 = input("Voulez faire un autre calcule? y/n :")
    if reponse18 != "y":
        break


"""
Exercice 19 :
exo19-À l’aide de la boucle TantQue … Faire, réalisez un algorithme calculant le
résultat de N10. N étant un nombre saisi par l’utilisateur.
"""

while True:
    user_number = int(input("Entrez un nombre : "))
    result19 = user_number ** 10
    print(f"{user_number} ** 10 = {result19}")
    reponse19 = input("Voulez faire un autre calcule? y/n :")
    if reponse19 != "y":
        break


"""
Exercice 20 :
exo20-Reprenez l’exercice précédent et modifiez-le pour que l’utilisateur entre
également l’exposant qu’il désire calculer.
"""

while True:
    user_number = int(input("Entrez un nombre : "))
    power = int(input("Entrez l'exposant : "))
    result19 = user_number ** power
    print(f"{user_number} ** {power} = {result19}")
    reponse19 = input("Voulez faire un autre calcule? y/n :")
    if reponse19 != "y":
        break

"""
Exercice 21 :
exo21-Améliorez le "C'est plus, c'est moins, c'est gagné" pour qu'il tourne en boucle tant que le juste_prix n'a pas été trouvé.
L'ordinateur choisit un nombre aléatoirement entre 1 et 100. L'utilisateur est invité à entrer un nombre et l'algorithme nous
répond "C'est plus" ou "C'est moins". Lorsqu'on a trouvé le bon nombre, l'algorithme affiche le nombre de tentatives
effectuées pour trouver le résultat
"""
from random import randint
juste_prix = randint(1, 100)

number_of_tries = 0

while True:
    number_of_tries += 1
    user_number = int(input("Devinez le juste prix : "))

    if user_number > juste_prix:
        print("C'est moins.")
    elif user_number < juste_prix:
        print("C'est plus.")
    else:
        break

print("C'est gagné !")
print(f"Le juste prix est : {juste_prix}")
print(f"Nombre d'essai(s) : {number_of_tries}")
