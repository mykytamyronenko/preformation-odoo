from datetime import date
import re

livres = {
    1: {"id": 1, "title": "1984", "author": ["George Orwell"],
        "year": 1949, "available": True},
    2: {"id": 2, "title": "Le Petit Prince", "author": ["Antoine de Saint-Exupéry"],
        "year": 1943, "available": True},
    3: {"id": 3, "title": "Good Omens", "author": ["Terry Pratchett", "Neil Gaiman"],
        "year": 1990, "available": True},
}

users = {
    1: {"id": 1, "username": "alice", "email": "alice@bstorm.be", "booksIds": []},
    2: {"id": 2, "username": "bob", "email": "bob@bstorm.be", "booksIds": []},
}

###############################

# Affichage des livres et leur dispo
def book_list(livres):
    if not livres:
        print("La bibliothèque est vide.")
        return

    for k,v in livres.items():
        print(f"Livre {k} :\n"
            f"Titre : {v['title']}\n"
            f"Auteur(s) : {', '.join(v['author'])}\n"
            f"Année de publication : {v['year']}\n"
            f"Disponible : {'Oui' if v['available'] else 'Non'}\n")


# Ajout d'un livre
def add_book(livres):
    new_author = None
    new_authors = list()
    new_availability = True

    new_title = input("Entrez le titre du nouveau livre : ")

    print("Vous pouvez entrez plusieurs auteur (écrivez 0 et taper enter pour passer à la suite)")
    while new_author != "0":
        new_author = input("Entrez le nom de l'auteur du nouveau livre : ")

        if new_author != "0":
            new_authors.append(new_author)

    while True:
        try:
            new_year = int(input("Entrez l'année de publication du nouveau livre : "))
        except ValueError:
            print("Erreur : Entrez une année valide.")
            continue

        if new_year <= 0 or new_year > date.today().year:
            print("Erreur : L'année doit être comprise entre 1 et l'année actuelle.")
            continue

        break

    new_id = max(livres.keys()) + 1 if livres else 1

    livres[new_id] = {
        "id": new_id,
        "title": new_title,
        "author": new_authors,
        "year": new_year,
        "available": new_availability
    }


# Modification d'un livre
def modify_book(livres):
    if not livres:
        print("La bibliothèque est vide. Aucun livre à modifier.")
        return
    
    for k,v in livres.items():
        print(f"Livre {k} :\n"
            f"Titre : {v['title']}\n"
            f"Auteur(s) : {', '.join(v['author'])}\n"
            f"Année de publication : {v['year']}\n"
            f"Disponible : {'Oui' if v['available'] else 'Non'}\n")

    while True:
        try:
            Book_to_modify = int(input("Entrez le numéro du livre que vous souhaiter modifier : "))
        except ValueError:
            print("Erreur : Entrez un nombre valide.")
            continue

        if Book_to_modify not in livres:
            print("Aucun livre n'a ce numéro.")
            continue
        break

    other_author = None
    other_authors = list()
    current_id = livres[Book_to_modify]["id"]
    current_availability = livres[Book_to_modify]["available"]

    other_title = input("Entrez le titre du nouveau livre : ")

    print("Vous pouvez entrez plusieurs auteur (écrivez 0 et taper enter pour passer à la suite)")
    while other_author != "0":
        other_author = input("Entrez le nom de l'auteur du nouveau livre : ")

        if other_author != "0":
            other_authors.append(other_author)

    while True:
        try:
            other_year = int(input("Entrez l'année de publication du nouveau livre : "))
            break
        except ValueError:
            print("Erreur : Entrez une année valide.")

    livres[Book_to_modify] = {
        "id": current_id,
        "title": other_title,
        "author": other_authors,
        "year": other_year,
        "available": current_availability
    }


# Suppression d'un livre
def delete_book(livres):
    if not livres:
        print("La bibliothèque est vide. Aucun livre à supprimer.")
        return

    for k,v in livres.items():
        print(f"Livre {k} :\n"
            f"Titre : {v['title']}\n"
            f"Auteur(s) : {', '.join(v['author'])}\n"
            f"Année de publication : {v['year']}\n"
            f"Disponible : {'Oui' if v['available'] else 'Non'}\n")

    while True:
        try:
            book_to_del = int(input("Entrez le numéro du livre que vous souhaitez supprimer : "))
        except ValueError:
            print("Erreur : Entrez un nombre valide.")
            continue

        if book_to_del not in livres:
            print("Ce livre n'existe pas.")
            continue

        if livres[book_to_del]['available'] == False:
            print("Ce livre des loué, et ne peut être supprimé.")
            continue

        break

    del livres[book_to_del]


# Ajout d'un utilisateur
def add_user(users):
    new_username = input("Entrez le nom du nouveau utilisateur : ")

    while True:
        new_email = input("Entrez l'email du nouvel utilisateur : ")
        
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        
        if re.match(email_pattern, new_email):
            break
        else:
            print("Erreur : Format d'email invalide. (Exemple: exemple@domaine.com)")

    new_id = max(users.keys()) + 1 if users else 1

    users[new_id] = {
        "id": new_id,
        "username": new_username,
        "email": new_email,
        "booksIds": []

    }

###############################

def list_rented_books(users, livres):
    print("========================")
    print("Liste des utilisateurs :")
    for v in users.values():
        print(f"{v['username']}")
    print("========================")

    user_to_choose = input("Choisissez l'utilisateur dont vous voulez voir les livres loués : ")

    for v in users.values():
        if user_to_choose == v['username']:
            print(f"Livre(s) loué(s) par {v['username']} : ")
            if v['booksIds']:
                for book_id in v['booksIds']:
                    print(f"- {livres[book_id]['title']}, écrit par {", ".join(livres[book_id]['author'])}")
            else:
                print("Aucun livre loué.")
            break

def rent_a_book(users, livres):
    print("========================")
    print("Liste des utilisateurs :")
    for v in users.values():
        print(f"{v['username']}")
    print("========================")

    renting_user = input("Quel utilisateur souhaite louer un livre : ")

    print("========================")
    for k,v in livres.items():
        if v['available']:
            print(f"Livre {k} :\n"
                f"Titre : {v['title']}\n"
                f"Auteur(s) : {', '.join(v['author'])}\n"
                f"Année de publication : {v['year']}\n"
                f"Disponible : {'Oui' if v['available'] else 'Non'}\n")

    book_to_rent = int(input("Écrivez le numéro du livre que vous souhaitez louer : "))

    for v_users in users.values():
        if renting_user == v_users['username']:
            
            if book_to_rent in livres:
                chosen_book = livres[book_to_rent]
                
                if chosen_book['available']:
                    chosen_book['available'] = False
                    v_users['booksIds'].append(chosen_book['id'])
                    print(f"Le livre '{chosen_book['title']}' a été loué par {v_users['username']}.")
                else:
                    print(f"Le livre '{chosen_book['title']}' est déjà loué.")
            break

def return_a_book(users, livres):
    print("========================")
    print("Liste des utilisateurs :")
    for v in users.values():
        print(f"{v['username']}")
    print("========================")

    returning_user = input("Quel utilisateur souhaite rendre un livre : ")

    for v in users.values():
        if returning_user == v['username']:
            if v['booksIds']:
                print(f"Liste du/des livre(s) loué(s) par {v['username']}.")
                for book_id in v['booksIds']:
                    print(f"n°{livres[book_id]['id']} - {livres[book_id]['title']}")
                book_to_return = int(input("Écrivez le numéro du livre que vous souhaitez rendre : "))
                v['booksIds'].remove(book_to_return)
                livres[book_to_return]['available'] = True
            else:
                print(f"Aucun livre loué par {v['username']}.")
            break

        
input_user_plus = None

while input_user_plus != "partir":
    input_user_plus = input("=========================================\n"
                "Voulez vous ?\n"
                "Voir les livre -> écrivez : afficher\n"
                "Ajouter un livre -> écrivez : ajouter\n"
                "Modifier un livre -> écrivez : modifier\n"
                "Supprimer un livre -> écrivez : supprimer\n"
                "Ajouter un utilisateur -> écrivez : ajouter u\n"
                "Voir les livres loués -> écrivez : location\n"
                "Louer un livre -> écrivez : louer\n"
                "Rendre un livre -> écrivez : rendre\n"
                "Partir -> écrivez : partir\n"
                "=========================================\n")

    match input_user_plus:
        case "afficher":
            book_list(livres)
        case "ajouter":
            add_book(livres)
        case "modifier":
            modify_book(livres)
        case "supprimer":
            delete_book(livres)
        case "ajouter u":
            add_user(users)
        case "location":
            list_rented_books(users, livres)
        case "louer":
            rent_a_book(users, livres)
        case "rendre":
            return_a_book(users, livres)
        case _:
            continue
