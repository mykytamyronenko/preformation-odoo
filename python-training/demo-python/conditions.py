# def test(value : int):
#     """
#     info sur la fonction
#     """

#     pass

# test()

day_of_week = int(input("Entrez le jour de la semaine en temps en entier : "))

match day_of_week:
    case 1:
        print("lundi")
    case 5:
        print("vendredi")
    case _:
        print("autre")

note = float(input("Entrez la note de l'éleve : "))

match note:
    case n if n >= 90:
        resultat = "A"
    case n if n >= 70:
        resultat = "B"

print("Le résultat the la note : ",note)

a = 5
b = 10
c = 15
valeur = 7

if a < valeur < c:
    pass # utile pour le code vide

if (a < b) and (b != 50):
    pass

# plusieurs verifications dans le if
if a < b and b != 50 or True:
    pass

# tester une seule valeur
match valeur:
    case 10 :
        pass