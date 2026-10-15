"""
• exo29-Refaites l'algorithme qui demande à l’utilisateur de taper 10 entiers et qui
affiche le plus petit de ces entiers mais cette fois-ci à l'aide d'un tableau et sans
retenir le minimum lors de la saisie. 
"""

minimum = float('inf')
number_list = []

for i in range(10): 
    number = int(input("Entrez un nombre (10 fois au total) : "))
    number_list.append(number)

    if number_list[i] < minimum:
        minimum = number_list[i]

print(minimum)


"""
• exo30-En considérant un tableau d'entiers trié dans l'ordre croissant, réaliser un
algorithme étant capable d'insérer une nouvelle valeur dans le tableau de façon à ce
que la tableau reste trié. Le but n'est évidemment pas d'insérer la valeur à la fin et
de trier après mais bien de l'insérer au bon endroit directement. 
"""

tab = [4,75,89,2,57,8,-7,42,48]
tab.sort()
print(tab)

added_number = int(input("Entrez un nombre à inserer dans le tableau : "))

tmp = 0

for i in range(len(tab)):
    if added_number <= tab[0]:
        tab.reverse()
        tab.append(added_number)
        tab.reverse()
        break
    elif added_number < tab[i]:
        tab.append(added_number)
        tab.reverse()
        for j in range(0,len(tab)-i,1):
            if tab[j] < tab[j+1]:
                tmp = tab[j+1]
                tab[j+1] = tab[j]
                tab[j] = tmp
        tab.reverse()
        break
    elif added_number >= tab[-1]:
        tab.append(added_number)
        break

print(f"Sans insert : {tab}")


tab = [4,75,89,2,57,8,-7,42,48]
tab.sort()
print(tab)

added_number = int(input("Entrez un nombre à inserer dans le tableau : "))

for i in range(len(tab)):
    if added_number < tab[i]:
        tab.insert(i,added_number)
        break
    elif added_number >= tab[-1]:
        tab.append(added_number)
        break

print(f"Avec insert : {tab}")


tab = [4, 75, 89, 2, 57, 8, -7, 42, 48]
tab.sort()
print("Tableau initial trié :", tab)

added_number = int(input("Entrez un nombre à insérer dans le tableau : "))

index_insertion = len(tab)
for i in range(len(tab)):
    if added_number < tab[i]:
        index_insertion = i
        break

tab.insert(index_insertion, added_number)

print("Tableau final :", tab)

"""
• exo31-Réalisez un algorithme dans lequel nous devons rechercher une valeur (entrée
par l'utilisateur) dans un tableau d'entiers. 
"""

int_table = [4,75,89,2,57,8,-7,42,48]

number_to_find = int(input("Entrez un nombre à trouver dans le tableua d'entiers : "))

if number_to_find in int_table:
    pos = int_table.index(number_to_find) + 1
    print(f"Le nombre {number_to_find} est trouvé et est à la position {pos}")
else:
    print("Le nombre n'existe pas dans le tableau.")
