from Texte import Texte

class Livre(Texte):

    def __init__(self, auteur=None, titre=None, copyright=False, editeur=None, annee=None, texte=None):
        Texte.__init__(self,auteur, titre, copyright, texte);
        self.editeur = editeur;
        self.annee = annee;

    def __str__(self):
        return f"" + super().__str__();