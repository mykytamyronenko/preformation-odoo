"""
• exo23-Écrire un algorithme demandant à l’utilisateur le nombre de joueurs (max 10
joueurs). Ensuite, l’algorithme doit demander à l’utilisateur le score de chaque
joueur. Une fois ceci fini, il faut afficher la moyenne des scores. Faites de même en
Python
"""

number_of_player = int(input("Entrez un nombre de joueurs (max 10) : "))

while 0 >= number_of_player or number_of_player > 10:
    number_of_player = int(input("Entrez un nombre inférieur ou égale à 10 : "))

average = 0

for i in range(1,number_of_player+1,1):
    player_score = int(input(f"Entrez le score du joueur {i} : "))
    average = average + player_score

average = average / number_of_player
print(f"Moyenne des scores : {average}")

"""
• exo24-Inverser un tableau : soit un tableau T. Saisir ce tableau. Changer de place les
éléments de ce tableau de façon à ce que le nouveau tableau soit une sorte de miroir
de l'ancien et afficher le nouveau tableau.
"""

t = [1,2,3,4,5]
# t.reverse()
# print(t)

t2 = []

for i in range(1,len(t)+1,1):
    t2.append(t[-i])

print(t2)

"""
• exo25-À l’aide des boucles, réalisez un algorithme permettant de trier un tableau
d’entiers dans l’ordre croissant. Mettez-le ensuite en pratique avec le Python.
"""

table = [66,55,88,11,99,22,44,33,77,100]
#table.sort()

for i in range(0,len(table),1):
    for j in range(0,len(table),1):
        if table[i] < table[j]:
            tmp = table[i]
            table[i] = table[j]
            table[j] = tmp

print(table)
