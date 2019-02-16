class Document:
    def __init__(self, auteur=None, titre=None, copyright=False):
        self.auteur = auteur;
        self.titre = titre;
        self.copyright = copyright;

    def __str__(self):
        res=""
        if self.copyright:
            res = " (soumis au Copyright)"
        return f"{self.titre} ecrit par {self.auteur}" + res

