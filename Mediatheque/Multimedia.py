from Document import Document

class Multimedia(Document):
    def __init__(self, auteur=None, titre=None, copyright=False, type=None):
        Document.__init__(self,auteur, titre, copyright);
        self.type = type

    def imprime(self):
        if(self.type == "Texte"):
            print("L'impression du document {self.titre} est lancée")
