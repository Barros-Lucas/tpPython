class ListePriorite:
    def __init__(self):
        self.liste = []
        self.prio_min = None
        self.prio_max = None
        self.length = 0
        self.empty = True

    def __str__(self):
        return f"{self.liste}"


   
    def add(self,importance,valeur):
        if self.empty:
            self.prio_min = importance
            self.prio_max = importance
            self.liste.append((importance,valeur))
            self.length +=1
            self.empty = False
            return self.liste
        elif importance >= self.prio_max:
            self.prio_max = importance
            self.liste.append((importance,valeur))
            self.length +=1
            self.empty = False
            return self.liste
        else:
            self.prio_min = importance
            indice = self.getIDinsert(importance)
            self.liste.insert(indice,(importance,valeur))
            self.length +=1
            self.empty = False
            return self.liste
        
            

    def contains(self, valeur):
        for i in range (len(self.liste)):
            if valeur == self.liste[i][1]:
                return True
        return False

    def getIDinsert(self,importance):
        indice = 0
        for i in range (len(self.liste)):
            temp = self.liste[i]
            if int(temp[0]) > importance :
                if(indice == 0):
                    self.min = importance
                return indice
            indice += 1

    def priorities_of(self,value):
        liste = []
        for i in range (len(self.liste)):
             temp =self.liste[i]
             if temp[1] == value:
                 liste.append(temp[0])
        return liste
             
    def pop(self):
        self.liste.remove(self.liste[len(self.liste)-1])
        temp = self.liste[len(self.liste)-1]
        self.prio_max = temp[0]
        self.length -=1
        self.empty =  True if len(self.liste) == 0 else False
        return self.liste

    def items(self):
        return self.liste[0:]

    def vals(self):
        for i in range (len(self.liste)):
            yield self.liste[i][1]

    def at(self, index):
        return self.liste[index]

    def delete(self, index):
        self.liste.remove(self.liste[index])
        return self.liste
