"""
• exo26-En considérant deux tableaux d'entiers (non triés), réalisez un algorithme qui
place tous les éléments des deux tableaux dans un troisième. Ce dernier doit être
trié une fois l'algorithme terminé. Notez que le tri doit être fait en même temps que
la fusion des deux tableaux et pas après. (Indice : tab.reverse())

"""

tab1 = [44, 88, 22, 77, 99, -58, 598]
tab2 = [55, 100, 66, 11, 33, 98, -45, -75, 90, 2, 4]
tab3 = []

while tab1 or tab2:
    if tab1:
        max_tab1 = max(tab1)

    if tab2:
        max_tab2 = max(tab2)

    if not tab1:
        tab3.append(max_tab2)
        tab2.remove(max_tab2)

    elif not tab2:
        tab3.append(max_tab1)
        tab1.remove(max_tab1)

    elif max_tab1 > max_tab2:
        tab3.append(max_tab1)
        tab1.remove(max_tab1)

    else:
        tab3.append(max_tab2)
        tab2.remove(max_tab2)

tab3.reverse()

print(f"Solution initiale : {tab3}")



tab1 = [44,88,22,77,99,-58,598]
tab2 = [55,100,66,11,33,98,-45,-75,90,2,4]
tab3 = []

while tab1 or tab2:
    max_tab1 = max(tab1) if tab1 else float('-inf')
    max_tab2 = max(tab2) if tab2 else float('-inf')

    if max_tab1 > max_tab2:
        tab3.append(max_tab1)
        tab1.remove(max_tab1)
    else:
        tab3.append(max_tab2)
        tab2.remove(max_tab2)
tab3.reverse()
print(f"Solution plus propre : {tab3}")


"""
• exo27-Réalisez un algorithme nous permettant de déplacer un pion dans un tableau
de 10 éléments. Au début, le pion se trouve dans la première case du tableau. Nous
pouvons ensuite le déplacer par la gauche (g), par la droite (d) ou de stopper
l'algorithme (q) (Indice : l'exo doit être exécuté dans la console Windows).
"""
pawn = 1

tableau_de_parcours = [0] * 10
print(tableau_de_parcours)

tableau_de_parcours[0] = pawn
print(tableau_de_parcours)

move = None

while move != "q":
    move = input("g pour gauche, d pour droite : ")
    if move == "g":
        for i in range(0,len(tableau_de_parcours),1):
            if tableau_de_parcours[0] != 1:
                if tableau_de_parcours[i] == 1:
                    tableau_de_parcours[i] = 0
                    tableau_de_parcours[i-1] = 1
                    break
            else:
                print("Le pion ne peut pas aller plus à gauche.")
                break

    if move == "d":
        for i in range(0,len(tableau_de_parcours),1):
            if tableau_de_parcours[-1] != 1:
                if tableau_de_parcours[i] == 1:
                    tableau_de_parcours[i] = 0
                    tableau_de_parcours[i+1] = 1
                    break
            else:
                print("Le pion ne peut pas aller plus à droite.")
                break
    print(tableau_de_parcours)

"""
• exo28-Réalisez un algorithme permettant de rechercher une valeur dans un tableau.
Si la valeur se trouve bien dans la tableau, nous affichons sa position. 
"""

tableau = [88,75,44,76,25,801,100]

finder = int(input("Entrez une valeur présente dans le tableau : "))

found = False

for i in range(0,len(tableau),1):
    if finder == tableau[i]:
        print(f"position de la valeur : {i+1}")
        found = True

if found == False :
    print("Cette valeur n'existe pas dans le tableau.")