import csv
from pathlib import Path

def read_file():
    chemin = Path(__file__).parent / "produits.csv"

    with open(chemin,newline="",encoding="utf-8") as fichier:
        result = csv.DictReader(fichier)
        return list(result)

def main():
    result = read_file()

    for p in result:
        p["prix_unitaire"] = float(p.get("prix_unitaire") or 0)
        print(f" {p.get("prix_unitaire")} type : {type(p.get("prix_unitaire"))}")

if __name__ == "__main__":
    main()
    


# Exemple Class 
class Produit:
    def __init__(self, nom, prix_unitaire, quantite):
        self.nom = nom
        self._prix_unitaire = prix_unitaire
        self.quantite = quantite
        
        
    @property
    def quantite(self):
        return self.__quantite
    
    @quantite.setter
    def quantite(self, value):
        if value > 0:
            self.__quantite = value
        else:
            raise ValueError("La quantité doit être supérieure à 0")
        
new_product = Produit("test", 10, 5)

print("----------------")
print(new_product.nom)
new_product.nom = "test2"
print(new_product.nom)

print("----------------")
print(new_product._prix_unitaire)
new_product._prix_unitaire = 20
print(new_product._prix_unitaire)

print("----------------")

print(new_product.quantite)
new_product.quantite = 50
print(new_product.quantite)
