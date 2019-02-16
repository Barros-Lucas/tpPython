class Element:
    def __init__(self,posX,posY):
        self.posX = posX;
        self.posY = posY;
        self.estTouche = False;

    def toucher(self):
        self.estTouche = True;
        return self.estTouche

    def __str__(self):
        if self.estTouche:
            return "X"
        else:
            return " "
