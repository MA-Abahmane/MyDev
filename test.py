
from abc import ABC, abstractmethod
import json


class Produit(ABC):

    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    @abstractmethod
    def afficher_details(self):
        pass


class ProduitAlimentaire(Produit):

    def __init__(self, nom, prix, date_expiration):
        super().__init__(nom, prix)
        self.date_expiration = date_expiration
    
    def afficher_details(self):
        print(self.__dict__)

class ProduitNonAlimentaire(Produit):

    def __init__(self, nom, prix, materiau):
        super().__init__(nom, prix)
        self.materiau = materiau

    def afficher_details(self):
        print(self.__dict__)


if __name__ == '__main__':
    p1 = ProduitAlimentaire('apple', 33, '3-2-1222')
    p2 = ProduitNonAlimentaire('broom', 55, '3-2-1221')
    #p1.afficher_details()
    #p2.afficher_details()

    p3 = ProduitAlimentaire('banana', 31, '3-1-1222')
    p4 = ProduitNonAlimentaire('table', 52, '3-1-1221')


class Stock:

    def __init__(self):
        self.stock = []

    def ajouter_produit(self, produit):
        self.stock.append(produit)

    def afficher_produits(self):
        for prd in self.stock:
            print(prd.__dict__)

    def rechercher_produit(self, nom):
        for prd in self.stock:
            if prd.nom == nom:
                return prd
        return None


if __name__ == '__main__':
    s = Stock()
    s.ajouter_produit(p1)
    s.ajouter_produit(p2)
    s.ajouter_produit(p3)
    s.ajouter_produit(p4)

    #print('found:', s.rechercher_produit('banana').__dict__)
    #s.afficher_produits()


def Jsave(lst):
    f = open('stock.json', 'w')
    dct = {'data': []}
    for prd in lst:
        dct['data'].append(prd.__dict__)
    json.dump(dct, f)
    f.close

def Jload():
    try:
        f = open('stock.json', 'r')
        contents = json.load(f)
        for ln in contents['data']:
            print(ln)
    except FileNotFoundError:
        print('The file is not found')


Jsave(s.stock)
#Jload()


def validator(entree):
    """ validate entree to only have characters, numbers and spaces """
    import re

    pat = r'^[a-zA-Z\d\s]+$'

    return True if re.search(pat, entree) else False

print(validator('da fAdsf dS34234'))
print(validator('EG FTR2 34G fd34 32sf d34 234_'))
print(validator('EG FTR2 34G fd34 32sf d34 234-'))
print(validator('5*'))