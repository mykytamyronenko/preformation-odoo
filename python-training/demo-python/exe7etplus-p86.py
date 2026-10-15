"""
exo07-Année bissextile (Pseudo-Code + Python)
Réaliser un petit algorithme qui sur base d’une année donnée va déterminer s’il s’agit d’une année
bissextile. Une année est bissextile si elle est divisible par 4, mais non divisible par 100. Ou si elle est
divisible par 400. (ex: 2020, 1600 bissextiles. 1900 pas bissextile)
"""

year = int(input("Entrez une année au choix : "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("bissextiles ? ",True)
else:
    print("bissextiles ? ",False)

"""
exo8-Lanceur de balles de tennis (Pseudo-Code + Python)
(Indice : booleen = bool(int(input("Veuillez insérer : 1 = oui / 0 = non"))
Réaliser l’algorithme d’un lanceur de balles de tennis. Ce lanceur possède deux états :
– prêt : permet de savoir si le tennisman est prêt. Il ne faut pas lancer de balles dans le cas contraire
– panier_vide : permet de savoir s’il y a encore des balles disponibles
Le lanceur de balle possède l’opération « lancerBalle » qui, vous l’aurez compris, permet de lancer
une balle.
"""
# booleen = bool(int(input("Veuillez insérer : 1 = oui / 0 = non"))
# pret = False
# panier_vide = True
# lancer_balle = False

# if pret == True and panier_vide == False:
#     lancer_balle == True
# else:
#     lancer_balle == False

ready = False
panier_vide = True

stock_balls = int(input("Combien de balles avez vous mis : "))

if stock_balls > 0:
    panier_vide = False
    response = input("Etes-vous prêt? y-n :")
    if response == 'y':
        ready = True

if ready and not panier_vide:
    print("La partie commence !")
    print("Balle lancé")
    stock_balls -= 1
    print(f"il reste {stock_balls} balles")



"""
exo09-Distributeur de boissons (Pseudo-Code + Python)
Réaliser l’algorithme d’un distributeur de boissons. Ce dernier propose plusieurs boissons et
l’utilisateur choisit celle qu’il désire en entrant le numéro correspondant. Ne pas oublier de vérifier
s’il y a encore des boissons en stock.
"""


eau = 10
fanta = 10
coca = 5
cafe = 5

User_choice = None

menu = """
coca : 1
fanta : 2
eau : 3
café : 4
"""

print(menu)

User_choice = int(input("Entrez le numéro de la boisson : "))

match User_choice:
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

"""
exo10-Calculatrice (Pseudo-Code + Python)
Réaliser l’algorithme d’une calculatrice basique. L’utilisateur
est invité à saisir un nombre, un opérateur, et un deuxième
nombre. La calculatrice affiche ensuite le résultat. (Gérer la
division par 0)
"""

nb_1 = None
operateur = None
nb_2 = None

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


"""
exo11-Note (Pseudo-Code + Python)
Ecrire un algorithme qui met l'appréciation par rapport à des
notes. Ces notes sont comprises entre 0 et 20.
/!\ Gérer les erreurs : ex : -2; 25
"""

# score = int(input("Entrez une note : "))

# match score:
#     case 1:
#         print("Vous avez 1")
#     case 2:
#         print("Vous avez 2")
#     case 3:
#         print("Vous avez 3")
#     case 4:
#         print("Vous avez 1")
#     case 5:
#         print("Vous avez 2")
#     case 6:
#         print("Vous avez 3")
#     case 7:
#         print("Vous avez 1")
#     case 8:
#         print("Vous avez 2")
#     case 9:
#         print("Vous avez 3")
#     case 10:
#         print("Vous avez 1")
#     case 11:
#         print("Vous avez 2")
#     case 12:
#         print("Vous avez 3")
#     case 13:
#         print("Vous avez 13")
#     case 14:
#         print("Vous avez 14")
#     case 15:
#         print("Vous avez 15")
#     case 16:
#         print("Vous avez 16")
#     case 17:
#         print("Vous avez 17")
#     case 18:
#         print("Vous avez 18")
#     case 19:
#         print("Vous avez 19")
#     case 20:
#         print("Vous avez 20")
#     case _:
#         print("ERREUR")

note = int(input("Entrez votre note : "))

if 0 <= note <= 20:
    match note:
        case _ if note >= 18:
            print("TB")
        case _ if 15 < note < 18:
            print("B")
        case _ if 10 < note < 15:
            print("S")
        case _ if note <= 10:
            print("I")

"""
exo12-Réalisez un algorithme utilisant le convertisseur de
secondes, il reçoit deux durées (jours, heures, minutes et
secondes) et calcule la différence entre ces dernières.

"""

nb_day = int(input("Entrez un nombre de jours : "))
nb_hour = int(input("Entrez un nombre d'heure : "))
nb_minute = int(input("Entrez un nombre de minutes : "))
nb_second = int(input("Entrez un nombre de secondes : "))

nb_day2 = int(input("Entrez un second nombre de jours : "))
nb_hour2 = int(input("Entrez un second nombre d'heure : "))
nb_minute2 = int(input("Entrez un second nombre de minutes : "))
nb_second2 = int(input("Entrez un second nombre de secondes : "))

number1 = nb_day * 86400 + nb_hour * 3600 + nb_minute * 60 + nb_second
number2 = nb_day2 * 86400 + nb_hour2 * 3600 + nb_minute2 * 60 + nb_second2

if number1 >= number2:
    result = number1 - number2
    print("result : ",result)
else:
    result = number2 - number1
    print("result : ",result)

jours_diff = result // 86400
reste = result % 86400

heures_diff = reste // 3600
reste = reste % 3600

minutes_diff = reste // 60
secondes_diff = reste % 60

print(f"La différence est de : {jours_diff}j, {heures_diff}h, {minutes_diff}m, {secondes_diff}s")

"""
Memory game, retenir le plus de mots dans un while
"""

ma_list = list()
points = 0
end_game = False

while not end_game:
    mot = input("Entrez un mot : ")
    ma_list.append(mot)

    print("Entrez les mots un par un ddans l'ordre : ")
    for i in range(0,len(ma_list),1):
        input_user = input(f"Mot n° {i + 1} ")
        if ma_list[i] != input_user:
            end_game = True
            break
        points += 1
print(f"Vous avez memoriser {points} mots")


"""
MAYBE A FAIRE
Programme interactif, gestion de stock
ajout = input, append
suppr = valeur, remove
modif = récuperation, afficher la valeur, remplacer
lecture = print
"""