from Bateau import Bateau

class Escorteur(Bateau):
    def __init__(self,posX,posY,direction):
        Bateau.__init__(self,posX,posY,direction,2)

    def __str__(self):
        return "Escorteur"