from Mediatheque import Mediatheque
from Document import Document
from Livre import Livre
from Audio import Audio
from Article import Article
from Multimedia import Multimedia
from Video import Video
import pickle

med = None

def creationMed():
    print('\n')
    print("Création d'une nouvelle Médiathèque")
    nom = input("Veuillez renseignez le nom de votre médiathèque")
    med = Mediatheque(nom)
    return med

def menu():
    print("\n")
    print("Vous voilà dans le menu, choisissez une action à réaliser")
    print("1: Ajouter un document")
    print("2: Imprimer un document")
    print("3: Afficher les documents présents")
    print("4: Supprimer un document")
    print("5: Quitter")
    while True:
        user_input = input("Votre choix: ")
        try:
            val = int(user_input)
            return val
        except ValueError:
            print("Renseignez un entier svp")
def addSousDoc(entier, med):

    auteur = input("Nom de l'auteur : ")
    titre = input("Titre du document : ")
    while True:
        copy = input("Copyright? (1-oui, 2-non): ")
        try:
            val = int(copy)
            if val ==1 or val == 2:
                break
        except ValueError:
            print("Renseignez un entier svp")
    copy = val
    if entier == 1:
        editeur = input("Editeur de l'article : ")
        titreRevu = input("Titre de la revue : ")
        numEdition = input("Numéro de l'édition : ")
        texte = input("Ecrire le texte : ")
        article = Article(auteur, titre, copy, editeur, titreRevu, numEdition, texte)
        med.ajouter(article)
        print("Article ajouté")
        return
    if entier == 2:
        duree = input("Duree de l'audio : ")
        contenu = input("Contenu de l'audio : ")
        audio = Audio(auteur, titre, copy, duree, contenu)
        med.ajouter(audio)
        print("Audio ajouté")
        return
    if entier == 3:
        editeur = input("Editeur du livre : ")
        annee = input("Annee de parution : ")
        texte = input("Contenu du livre : ")
        livre = Livre(auteur, titre, copy, editeur, annee, texte)
        med.ajouter(livre)
        print("Livre ajouté")
        return
    if entier == 4:
        type = input("Type de multimedia : ")
        multi = Multimedia(auteur, titre, copy, type)
        med.ajouter(multi)
        print("Multimedia ajouté")
        return
    if entier == 5:
        duree = input("Duree de la video : ")
        contenu = input("Contenu de la video : ")
        video = Video(auteur, titre, copy, duree, contenu)
        med.ajouter(video)
        print("Video ajouté")
        return

def addDoc(med):
    print("\n")
    print("Ajout d'un document, choisissez un type de document à ajouter")
    print("1: Ajouter un Article")
    print("2: Ajouter un Audio")
    print("3: Ajouter un Livre")
    print("4: Ajouter un Multimedia")
    print("5: Ajouter une Vidéo")
    print("6: Quitter")
    while True:
        user_input = input("Votre choix: ")
        try:
            val = int(user_input)
            if val > 0 and val <=6:
                if val == 6:
                    print("Aucun document ajouté")
                    return
                addSousDoc(val,med)
                return
        except ValueError:
            print("Renseignez un entier svp")

    doc1_Livre = Livre("lucas", "evian", True, "editeur1", "2018", "Voici le texte de mon livre")
    med.ajouter(doc1_Livre)
    print("Ajout effectué")

def quit(med):
    while True:
        user_input = input("Voulez-vous sauvgarder les modifications? (1-oui, 2-non): ")
        try:
            val = int(user_input)
            break
        except ValueError:
            print("Renseignez un entier svp")
    if val == 1:
        with open('Mediatheque_save.dat', 'wb') as f:
            pickle.dump(med, f)
            exit(0)
    else:
        exit(0)

def afficherMed(med):
    print(med)

def imprimer(med):
    afficherMed(med)
    while True:
        user_input = input("Choisissez le document à imprimer: ")
        try:
            val = int(user_input)
            break
        except ValueError:
            print("Renseignez un entier svp")

    try:
        if val >= 0 and val < len(med.docs):
            med.docs[val][1].imprime()
            return
        else:
            print("Ce document n'est pas présent")
    except AttributeError:
        print("Ce document n'est pas imprimable")
        return

# doc1_Livre.imprime();

def action(entier,med):
    if entier == 1:
        addDoc(med)
    if entier ==2:
        imprimer(med)

    if entier == 3:
        afficherMed(med)

    #if entier == 4:

    if entier == 5:
        quit(med)


print("Bienvenue dans le gestionnaire de votre Médiathèque")
try:
    with open('Mediatheque_save.dat', 'rb') as f:
        med = pickle.load(f)
except FileNotFoundError:
    med = None

if med is None:
    print("## Aucune sauvgarde ne semble existée dans le fichier \'Mediatheque_save.dat\' ##")
    med = creationMed();



while True:
    print(med.each_livre())
    val = menu()
    action(val,med)




