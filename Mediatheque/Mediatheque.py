from Document import Document
from Livre import Livre

class Mediatheque:
    def __init__(self, nom=None):
        self.nom = nom
        self.docs = []
        self.ids = 0

    def ajouter(self, doc):
        self.docs.append((self.ids,doc))
        self.ids+=1

    def supprimer(self, indice):
        self.docs.remove(indice)

    #def modifier(self, indice):

    def each_livre(self):
        livres = []
        for i in self.docs:
            if isinstance(i,Livre):
                livres.append(i)
        return livres

    def contains(self, id):
        for i in range(len(self.docs)):
            if id == self.docs[i][1]:
                return True
        return False

    def __str__(self):
        doc = "\n"
        for i in self.docs:
            doc += str(i[0])+" : "+str(i[1])+'\n'
        return f"\nLa médiatheque : {self.nom}, possède les documents : {doc}"