"""
Exercice supplémentaires :
• 1) Réalisez un système de connexion à l'aide d'un mot de passe.
L'algorithme demande à l'utilisateur de saisir son mot de passe.
Si ce dernier valide de bon mot de passe, on le salue.
Par contre, si il fait une erreur trois fois de suite, un message lui
signalera que son compte est bloqué et il ne pourra pas réessayer une quatrième fois
"""
psw = input("Crée votre mdp : ")
number_of_tries = 0
max_number_of_tries = 3

while True:
    number_of_tries += 1
    psw_try = input("Saisissez le mot de passe : ")
    if psw_try == psw:
        print("Bienvenue!")
        break
    elif number_of_tries == max_number_of_tries:
        print("Vous avez saissit le mouvais mot de passe 3 fois, votre compte maintenant bloqué.")
        break
    else:
        print("Mauvais mot de passe.")
        continue


"""
• 2) Réalisez un algorithme qui demande un nombre à l'utilisateur et affiche autant de ligne
que le nombre spécifié par l'utilisateur.
Exemple : l'utilisateur a rentré le nombre 5 et l'algorithme affiche :
*
**
***
****
*****
"""

user_number = int(input("choisissez un nombre : "))

for i in range(0,user_number,1):
    print("*", end="")
    for j in range(0,i,1):
        print("*", end="")
    print()

for i in range(1, user_number + 1):
    print("*" * i)

"""
• 3) Ecrire un algorithme qui demande à l’utilisateur de taper 10 entiers
et qui affiche le plus petit de ces entiers.
"""

user_number3 = int(input("Saisissez un nombre : "))
min_number = user_number3

for i in range(0,9):
    user_number3 = int(input("Saisissez un nombre : "))
    if user_number3 < min_number:
        min_number = user_number3

print(f"Le plus petit nombre saisi est {min_number}")

"""
• 4) Algorithme demandant 3 nombres : nbRep, nbTiret, nbEspace.
Ce dernier affiche à l'écran autant de tiret que la valeur de nbTiret,
suivi d'autant d'espace que la valeur de nbEspace.
Le tout autant de fois que la valeur de nbRep.Exemple : si nbRep = 2,
nbTiret = 1 et nbEspace = 3 le résultat est le suivant :|- - |
"""
nb_rep = int(input("nombre de rep : "))
nb_tiret = int(input("nombre de tiret : "))
nb_espace = int(input("nombre d'espace : "))

for i in range(nb_rep):
    for j in range(nb_tiret):
        print("-",end="")
    for k in range(nb_espace):
        print(" ",end="")

