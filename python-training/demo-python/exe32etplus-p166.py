"""
• exo32-Réalisez une fonction calculant le carré d’un nombre entier
donné en paramètre.
"""

def calcule_carre(valeur: float) -> float:
    resultat = valeur * valeur
    return resultat

print(calcule_carre(9))

"""
• exo33-Réalisez une fonction de recherche dans un tableau. Cette
fonction va recevoir un tableau, la taille du tableau, et la valeur
recherchée en paramètres et renvoyer l’indice de l’élément dans le
tableau. Si l’élément ne s’y trouve pas, la fonction renvoie -1.
"""

def finder_in_list(table : list,number_to_find : int) -> int:
    # table_length = len(table)
    # if number_to_find in table:
    #     for i in range(table_length):
    #         if number_to_find == table[i]:
    #             print(f"le nombre {number_to_find} est à l'indice : {i}")
    #             break
    # else:
    #     print("-1")
    return table.index(number_to_find) if number_to_find in table else -1

number_to_find = 4
result = finder_in_list([1,2,3,4,5],number_to_find)
print(f"le nombre {number_to_find} est à l'indice : {result}")

"""
• exo34-Réalisez une procédure dont l’objectif est de fusionner deux
tableaux d’entiers.
"""

def merge1(tab1 : list, tab2 : list) -> list:
    for i in range(len(tab2)):
        tab1.append(tab2[i])

    tab1.sort()

    return tab1

table1 = [1,3,5,7,9]
table2 = [2,4,6,8,10]
print(f"Solution initial : {merge1(table1,table2)}")



def merge2(tab1: list[int], tab2: list[int]) -> list[int]:
    i, j = 0, 0
    resultat = []
    
    while i < len(tab1) and j < len(tab2):
        if tab1[i] <= tab2[j]:
            resultat.append(tab1[i])
            i += 1
        else:
            resultat.append(tab2[j])
            j += 1

    resultat.extend(tab1[i:])
    resultat.extend(tab2[j:])
    
    return resultat

table1 = [1,3,5,7,9]
table2 = [2,4,6,8,10]
print(f"Fusion si liste déjà trié : {merge2(table1, table2)}")



def merge_simple(tab1: list[int], tab2: list[int]) -> list[int]:
    return tab1 + tab2
table1 = [1,3,5,7,99,11,55,77]
table2 = [2,4,6,8,55,1552,24,78,98,6525,78,4,5]
print(f"Fusion simple : {merge_simple(table1, table2)}")



def merge_and_sort(tab1: list[int], tab2: list[int]) -> list[int]:
    return sorted(tab1 + tab2)
table1 = [1,3,5,7,99,11,55,77]
table2 = [2,4,6,8,55,1552,24,78,98,6525,78,4,5]
print(f"Fusionné et trié : {merge_and_sort(table1, table2)}")