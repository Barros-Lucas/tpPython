from Document import Document

class Texte(Document):
    def __init__(self, auteur=None, titre=None, copyright=False, texte=None):
        Document.__init__(self,auteur, titre, copyright);
        self.texte = texte;


    def imprime(self):
       retour = f"L'impression du document {self.titre} est lancée"
       print(retour)
    def __str__(self):
        return  super().__str__();