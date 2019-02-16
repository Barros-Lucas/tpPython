from Bateau import Bateau

class Croiseur(Bateau):
    def __init__(self,posX,posY,direction):
        Bateau.__init__(self,posX,posY,direction,3)

    def __str__(self):
        return "Croiseur"