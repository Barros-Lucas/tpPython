from Document import Document

class Audio(Document):
    def __init__(self, auteur=None, titre=None, copyright=False, duree=None, contenu=None):
        Document.__init__(self,auteur, titre, copyright);
        self.duree = duree;
        self.contenu = contenu;