"4"
"0 1"
"1 0"
"1 1"
"0 0"

# map = appliquer une fonction sur chaque ittérable

# list(map(lambda x : int(x), ligne.strip().split(" ")))

""" vieux et à éviter
f #file
f.open()
f.close()
"""

# rw, ra, w+a
# rb = read byte, same for w and a
# with open("theorie_tmp.py", "r") as f: # r = read, w = write, a = append (ajouter à la fin)
#     for lignes in f:
#         print(list(map(lambda x : int(x), ligne.strip().split(" "))))


# rare mais on peut del à la fin du with open pour les fichiers temporaires


# plus de 15 chiffre après la "," déconne

epsilon = 10**(-8)
0.5 - 0.5 < epsilon
# and instanceof(0.5 + 0.5,float)

with open("theorie_tmp.txt", "w") as f: # r = read, w = write, a = append (ajouter à la fin)
    f.write("coucou")