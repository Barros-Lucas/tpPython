class Grille:
    def __init__(self,nbLigne, nbColonne):
        if nbLigne>0 or nbColonne>0:
            self.nbLigne = nbLigne
            self.nbColonne = nbColonne
            self.bateaux = []
        else:
            raise Exception("Une grille doit avoir un nombre de ligne/colonne supérieure à 0")

    def __iadd__(self, other):
        self.ajoutBateau(other)
        return self

    def ajoutBateau(self,bateau):
        self.bateaux.append(bateau)



    def coup(self,posX,posY):
        if posX <=self.nbColonne and posX >0 and posY<=self.nbLigne and posY>0:
            for bat in self.bateaux:
                retour = bat.est_touche(posX, posY)
                if retour != 0:
                    return retour
            return 0
        else:
            return -1

    def __str__(self):
        bat = ""
        for i in self.bateaux:
            if not i.est_coule:
                bat += str(i)+" "
        return f"{bat}"