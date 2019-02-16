from Texte import Texte

class Article(Texte):

    def __init__(self, auteur=None, titre=None, copyright=False, editeur=None, titreRevu=None, numEdition=None, texte=None):
        Texte.__init__(self,auteur, titre, copyright, texte);
        self.editeur = editeur;
        self.titreRevu = titreRevu;
        self.numEdition = numEdition;