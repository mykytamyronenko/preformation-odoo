"""
Améliorez encore le juste_prix : l'utilisateur a droit à 10 essais après ces 10
essais, il a perdu.
• L'ordinateur affiche le juste_prix
• Ajouter un niveau :
– facile : entre 1 et 10
– moyen : entre 1 et 100
– difficile : entre 1 et 1000
• Tant que la personne veut rejouer, redemandez le niveau et générez un
nombre.
• Vérifiez que tout caractère entré est correct, c'est-à-dire pour que le
programme ne plante jamais.
"""

from random import randint
want_to_play = True

while want_to_play:
    difficulty_is_correct = False
    response_user_is_y_or_n = False
    can_try_again = True

    while not difficulty_is_correct:
        difficulty = input("Veillez à choisir (facile/moyen/difficile) : ")
        difficulty_is_correct = True

        if difficulty == "facile":
            juste_prix = randint(1, 10)
        elif difficulty == "moyen":
            juste_prix = randint(1, 100)
        elif difficulty == "difficile":
            juste_prix = randint(1, 1000)
        else:
            print("Vous n'avez pas choisit une difficulté existante.")
            difficulty_is_correct = False

    number_of_tries = 0
    max_number_of_tries = 10

    while can_try_again:
        number_of_tries += 1
        
        number_is_a_number = False

        while not number_is_a_number:
            user_number = input("Devinez le juste prix : ")

            if user_number.isdigit():
                number_is_a_number = True
                user_number = int(user_number)
            else:
                print("Veuillez saisir un nombre.")

        if user_number > juste_prix:
            print("C'est moins.")
        elif user_number < juste_prix:
            print("C'est plus.")
        else:
            print("C'est gagné !")
            print(f"Le juste prix est : {juste_prix}")
            print(f"Nombre d'essai(s) : {number_of_tries}")
            can_try_again = False

        if number_of_tries == max_number_of_tries and can_try_again:
            print(f"Le nombre d'essais maximal ({max_number_of_tries}) a été atteind.")
            print(f"Le prix juste prix était {juste_prix}")
            can_try_again = False

    while not response_user_is_y_or_n:
        response_user = input("Voulez vous rejouer? (y/n) : ")
        if response_user in ("y", "n"):
            response_user_is_y_or_n = True
        else:
            print("Veuillez à écrire y ou n.")

    if response_user == "n":
        want_to_play = False