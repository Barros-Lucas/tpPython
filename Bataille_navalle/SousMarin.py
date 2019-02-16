from Bateau import Bateau

class SousMarin(Bateau):
    def __init__(self,posX,posY,direction):
        Bateau.__init__(self,posX,posY,direction,1)
        self.est_surface = True;

    def plonger(self):
        self.est_surface = False

    def emerger(self):
        self.est_surface = True

    def surface(self):
        return self.est_surface

    def est_touche(self, posX, posY):
        if self.surface():
            return super().est_touche(self,posX,posY)
        else:
            return 0

    def __str__(self):
        return "Sous-Marin"