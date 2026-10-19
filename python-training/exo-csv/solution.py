
import csv
from pathlib import Path


def read_csv(file):
    path = Path(__file__).parent / file

    with open(path, newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)
        result = list(lecteur)

    return result


def convertir_quantite(valeur):
    try:
        quantite = int(valeur)
    except (ValueError, TypeError):
        return 0

    if quantite < 0:
        return 0

    return quantite


def customers_company(ville):
    result = read_csv("clients.csv")

    for c in result:
        if c["type"] == "entreprise" and c["ville"] == ville:
            print(c)


def indexer_par_id(liste):
    index = {}

    for element in liste:
        index[element["id"]] = element

    return index


def main():
    result_products = read_csv("produits.csv")

    for p in result_products:
        p["prix_unitaire"] = float(p["prix_unitaire"]) if p["prix_unitaire"] else 0.0
        p["stock"] = int(p["stock"]) if p["stock"] else 0
        print(p)

    print(f"Nombre de produits : {len(result_products)}")



    result_customers = read_csv("clients.csv")

    for c in result_customers:
        print(c)

    print(f"Nombre de clients : {len(result_customers)}")



    result_orders = read_csv("commandes.csv")

    for o in result_orders:
        o["quantite"] = convertir_quantite(o["quantite"])
        print(o)

    print(f"Nombre de commandes : {len(result_orders)}")

    commandes_par_etat = {}

    for o in result_orders:
        etat = o["etat"]

        if etat not in commandes_par_etat:
            commandes_par_etat[etat] = 0

        commandes_par_etat[etat] += 1

    for etat, nombre in commandes_par_etat.items():
        print(f"{etat} : {nombre}")


    print("les commandes confirmées :")
    for o in result_orders:
        if o["etat"] == "confirmee":
            print(o)


    print("Les commandes passées en mars 2026 :")
    for commande in result_orders:
        if commande["date"].startswith("2026-03"):
            print(commande)

    print("Les clients de type entreprise d'une ville donnée :")
    customers_company("Namur")


    print("calculer de montant : `quantité * prix unitaire du produit :")
    for o in result_orders:
        for p in result_products:
            if o["produit_id"] == p["id"]:
                quantite = int(o["quantite"])
                prix_unitaire = float(p["prix_unitaire"])

                montant = quantite * prix_unitaire

                print(f"Commande {o['id']} : {montant:.2f} €")


    # print("Montant de chaque commande confirmée, avec nom du client, nom du produit :")
    # for o in result_orders:
    #     for p in result_products:
    #         for c in result_customers:
    #             if o["produit_id"] == p["id"] and o["etat"] == "confirmee" \
    #             and o["client_id"] == c["id"]:
    #                 quantite = int(o["quantite"])
    #                 prix_unitaire = float(p["prix_unitaire"])

    #                 montant = quantite * prix_unitaire

    #                 print(f"Commande {o['id']} : {montant:.2f} €, {p["nom"]}, {c["nom"]}")

    
    # products_by_id = {p["id"]: p for p in result_products}
    products_by_id = {}
    for p in result_products:
        products_by_id[p["id"]] = p

    customers_by_id = {c["id"]: c for c in result_customers}

    print("Montant de chaque commande confirmée, avec nom du client et du produit :")

    for o in result_orders:
        if o["etat"] != "confirmee":
            continue

        p = products_by_id.get(o["produit_id"])
        c = customers_by_id.get(o["client_id"])

        if p is None or c is None:
            continue

        quantite = int(o["quantite"])
        prix_unitaire = float(p["prix_unitaire"])
        montant = quantite * prix_unitaire

        print(
            f"Commande {o['id']} : {montant:.2f} €, "
            f"{p['nom']}, {c['nom']}"
        )


    # print("Les commandes confirmées dont le montant dépasse 500 €")
    # for o in result_orders:
    #     for p in result_products:
    #         if o["produit_id"] == p["id"]:
    #             quantite = int(o["quantite"])
    #             prix_unitaire = float(p["prix_unitaire"])

    #             montant = quantite * prix_unitaire

    #             if montant > 500 and o["etat"] == "confirmee":
    #                 print(f"Commande {o['id']} : {montant:.2f} €")

    print("Les commandes confirmées dont le montant dépasse 500 €")

    products_by_id = {p["id"]: p for p in result_products}

    for o in result_orders:
        if o["etat"] != "confirmee":
            continue

        p = products_by_id.get(o["produit_id"])
        if p is None:
            continue

        quantite = int(o["quantite"])
        prix_unitaire = float(p["prix_unitaire"])
        montant = quantite * prix_unitaire

        if montant > 500:
            print(f"Commande {o['id']} : {montant:.2f} €")



    products_index = indexer_par_id(result_products)
    customers_index = indexer_par_id(result_customers)


    print("calculer de montant : `quantité * prix unitaire du produit :")
    for o in result_orders:
        p = products_index.get(o["produit_id"])

        if p is None:
            continue

        quantite = int(o["quantite"])
        prix_unitaire = float(p["prix_unitaire"])

        montant = quantite * prix_unitaire
        print(f"Commande {o['id']} : {montant:.2f} €")


    print("Montant de chaque commande confirmée, avec nom du client et du produit :")
    for o in result_orders:
        if o["etat"] != "confirmee":
            continue

        p = products_index.get(o["produit_id"])
        c = customers_index.get(o["client_id"])

        if p is None or c is None:
            continue

        quantite = int(o["quantite"])
        prix_unitaire = float(p["prix_unitaire"])
        montant = quantite * prix_unitaire

        print(f"Commande {o['id']} : {montant:.2f} €, {p['nom']}, {c['nom']}")


    print("Les commandes confirmées dont le montant dépasse 500 € :")
    for o in result_orders:
        p = products_index.get(o["produit_id"])

        if p is None:
            continue

        quantite = int(o["quantite"])
        prix_unitaire = float(p["prix_unitaire"])

        montant = quantite * prix_unitaire

        if montant > 500:
            print(f"Commande {o['id']} : {montant:.2f} €")


    print("Calculer le chiffre d'affaires par client (uniquement les commandes confirmées) :")
    products_index = indexer_par_id(result_products)
    customers_index = indexer_par_id(result_customers)

    ca_per_customer = {}

    for o in result_orders:
        if o["etat"] != "confirmee":
            continue

        p = products_index.get(o["produit_id"])
        c = customers_index.get(o["client_id"])

        if p is None or c is None:
            continue

        quantite = int(o["quantite"])
        prix_unitaire = float(p["prix_unitaire"])
        montant = quantite * prix_unitaire

        customer_name = c["nom"]

        ca_per_customer[customer_name] = ca_per_customer.get(customer_name, 0) + montant

    for client, ca in ca_per_customer.items():
        print(f"{client} : {ca:.2f} €")


    print("Calculer le chiffre d'affaires par catégorie de produit :")
    ca_par_categorie = {}

    for o in result_orders:
        p = products_index.get(o["produit_id"])

        if p is None:
            continue

        quantite = int(o["quantite"])
        prix_unitaire = float(p["prix_unitaire"])
        montant = quantite * prix_unitaire

        categorie = p["categorie"]

        ca_par_categorie[categorie] = ca_par_categorie.get(categorie, 0) + montant

    for categorie, ca in ca_par_categorie.items():
        print(f"{categorie} : {ca:.2f} €")


    orders_per_month = {}

    print("Calculer le nombre de commandes par mois :")
    for o in result_orders:
        month = o["date"][:7]

        orders_per_month[month] = orders_per_month.get(month, 0) + 1

        for m, om in sorted(orders_per_month.items()):
            print(f"{m} : {om}")

    





if __name__ == "__main__":
    main()