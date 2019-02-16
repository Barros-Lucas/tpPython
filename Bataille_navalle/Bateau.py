from Element import Element
class Bateau:
    def __init__(self,posX,posY,direction,nbElement):
        self.startX = posX;
        self.startY = posY;
        self.direction = direction;
        self.element = [Element] * nbElement
        self.placementElement()
        self.est_coule = False

    def placementElement(self):
        if self.direction:
            x = self.startX-1
            y = self.startY
        else:
            x = self.startX
            y = self.startY-1
        for i in range(0, len(self.element)):
            if self.direction:
                x += 1
            else:
                y += 1
            self.element[i] = Element(x,y)


    def all_element_hit(self):
        allHit = True
        for e in self.element:
            if not e.estTouche:
                allHit = False
        return allHit

    def est_touche(self,posX, posY):
        for e in self.element:
            if posX == e.posX and posY == e.posY:
                if not e.estTouche:
                    e.toucher()
                    if self.all_element_hit():
                        self.est_coule = True
                        return 3
                    else:
                        return 2
                else:
                    return 1
        return 0

class Croiseur(Bateau):
    def __init__(self, posX, posY, direction):
        Bateau.__init__(self, posX, posY, direction, 3)
    def __str__(self):
        return "Croiseur"


class Escorteur(Bateau):
    def __init__(self, posX, posY, direction):
        Bateau.__init__(self, posX, posY, direction, 1)

    def __str__(self):
        return "Escorteur"

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
        return "Sous-marin"



    """
        def __str__(self):
            sttr = "["
            for i in self.element:
                sttr += str(i)
                sttr += ","
            sttr += "]"
            return sttr
    """