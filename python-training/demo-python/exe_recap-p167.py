"""
• exo34-Algorithme du peleur de patate.
Le peleur de patate possède un seau dans lequel se trouvent les
pommes de terre non pelées. Il prend une pomme de terre dans
ce sceau, la pelle et la place ensuite dans une grosse marmite
jusqu’à ce qu’elle soit pleine. Si le seau est vide, il est capable de le
remplir.
La marmite peut contenir un maximum de 50 pommes de terre
tandis que le sceau peut en contenir maximum 17.
• Réalisez cet algorithme.
"""

def peeling_a_potato(unpeeled_potatoes_in_bucket=0,peeled_potatoes_in_pot=0,max_potatoes_in_bucket=17,max_potatoes_in_pot=50):
    while peeled_potatoes_in_pot < max_potatoes_in_pot:
        print(f"Il reste {unpeeled_potatoes_in_bucket} patates dans le seau.")
        print(f"Il reste {peeled_potatoes_in_pot} patates dans la marmite.")

        if unpeeled_potatoes_in_bucket <= 0:
            want_to_add_potatoes_in_bucket = input("Voulez-vous ajouter des patates dans le seau? (y/n) : ")

            if want_to_add_potatoes_in_bucket == "y":
                number_of_potatoes_to_add_in_bucket = int(input("Combien ? "))

                while number_of_potatoes_to_add_in_bucket <= 0 or number_of_potatoes_to_add_in_bucket > max_potatoes_in_bucket:
                    print("Le nombre total de patates dans le seau ne peut être négatif et ne peut pas dépasser 17")
                    number_of_potatoes_to_add_in_bucket = int(input("Combien voulez-vous en ajouter ? "))

                unpeeled_potatoes_in_bucket += number_of_potatoes_to_add_in_bucket
                print(f"nous avons {unpeeled_potatoes_in_bucket} patates dans le seau.")

            elif want_to_add_potatoes_in_bucket == "n":
                return

        want_to_peel = input("Voulez vous éplucher une ou des patate(s) ? (y/n) : ")

        if want_to_peel == "y":
            number_of_potatoes_to_peel = int(input("Combien ? "))

            while number_of_potatoes_to_peel <= 0 or number_of_potatoes_to_peel > unpeeled_potatoes_in_bucket:
                if number_of_potatoes_to_peel == 0:
                    number_of_potatoes_to_peel = int(input("Il faut au moins éplucher une patate, veuillez choisir un nombre de patates adéquat : "))
                elif number_of_potatoes_to_peel > unpeeled_potatoes_in_bucket:
                    number_of_potatoes_to_peel = int(input("Vous ne pouvez pas éplucher plus de patates qu'il y en a, Veuillez choisir un nombre de patates adéquat : "))
                else:
                    number_of_potatoes_to_peel = int(input("Le nombre ne peut être négatif, Veuillez choisir un nombre de patates adéquat : "))

            if number_of_potatoes_to_peel > 0 and number_of_potatoes_to_peel <= unpeeled_potatoes_in_bucket:
                unpeeled_potatoes_in_bucket -= number_of_potatoes_to_peel
                peeled_potatoes_in_pot += number_of_potatoes_to_peel

            elif number_of_potatoes_to_peel < 0:
                print("Le nombre de patates ne peut pas être négatif.")

            elif number_of_potatoes_to_peel > unpeeled_potatoes_in_bucket:
                print("Il n'y a pas suffisamment de patates dans le seau.")

        else:
            return

    if peeled_potatoes_in_pot >= max_potatoes_in_pot:
        print(f"La marmite est remplie avec {max_potatoes_in_pot} patates.")
        if peeled_potatoes_in_pot > max_potatoes_in_pot:
            print(f"pomme(s) de terre épluchée(s) en trop : {peeled_potatoes_in_pot - max_potatoes_in_pot}")
        

    return

peeling_a_potato()





# Code optimisé : faut principalement réduire la longueur des noms des variable



# def peeling_a_potato(unpeeled=0, peeled=0, max_in_bucket=17, max_in_pot=50):
#     while peeled < max_in_pot:
#         print(f"\nIl reste {unpeeled} patate(s) dans le seau et {peeled} dans la marmite.")

#         # Ajout de patates dans le seau
#         if unpeeled <= 0:
#             want_to_add = input("Voulez-vous ajouter des patates dans le seau? (y/n) : ").strip().lower()
            
#             if want_to_add == "y":
#                 while True:
#                     try:
#                         to_add = int(input("Combien ? "))
#                         # On vérifie que la capacité TOTALE ne dépasse pas le maximum
#                         if to_add <= 0 or (unpeeled + to_add > max_in_bucket):
#                             print(f"Erreur : Le nombre doit être positif et le seau ne peut pas contenir plus de {max_in_bucket} patates au total.")
#                         else:
#                             unpeeled += to_add
#                             break
#                     except ValueError:
#                         print("Veuillez entrer un nombre entier valide.")
#             elif want_to_add == "n":
#                 return
#             else:
#                 print("Entrée invalide. Veuillez répondre par 'y' ou 'n'.")
#                 continue

#         # Épluchage des patates
#         want_to_peel = input("Voulez-vous éplucher des patates ? (y/n) : ").strip().lower()
        
#         if want_to_peel == "y":
#             while True:
#                 try:
#                     to_peel = int(input("Combien ? "))
#                     if to_peel <= 0:
#                         print("Il faut au moins éplucher une patate.")
#                     elif to_peel > unpeeled:
#                         print("Vous ne pouvez pas éplucher plus de patates qu'il n'y en a dans le seau.")
#                     else:
#                         unpeeled -= to_peel
#                         peeled += to_peel
#                         break # Sortie de la boucle de validation une fois les données correctes
#                 except ValueError:
#                     print("Veuillez entrer un nombre entier valide.")
#         elif want_to_peel == "n":
#             return
#         else:
#             print("Entrée invalide.")

#     # Fin de la boucle (marmite pleine)
#     print(f"\nLa marmite est remplie avec au moins {max_in_pot} patates.")
#     if peeled > max_in_pot:
#         print(f"Pomme(s) de terre épluchée(s) en trop : {peeled - max_in_pot}")
