from time import sleep as sl
from os import system as sys
from vues.outils_vues import OutilsVues
from modeles.tournoi import Tournoi


def menu_tournoi():
    valeur_quitter = 0
    while valeur_quitter != 1:
        sys("clear")
        print("\nMenu gestion des tournois: ")
        print("\n1 - Liste des tournois\n2 - Reprise d'un tournoi\n3 - Retour\n4 - Quitter")
        try:
            choix_menu_tournoi = int(input("\nVotre choix: "))
        except ValueError:
            print("\nVous n'avez pas saisi un chiffre.")
            sl(2)
            continue
        if choix_menu_tournoi == 1:
            print("\n---------------------------\n")
            liste_tounois = Tournoi.tournois_liste()
            if liste_tounois == 0:
                print("Il n'y a aucun tournois d'enregistrer, veuillez ajouter un tournoi via le menu.")
                input("\nAppuyer sur entrer pour continuer")
                return
            for arg in liste_tounois:
                print(arg)
            input("\nAppuyer sur entrer pour continuer")
        if choix_menu_tournoi == 2:
            print("Reprise")
            sl(3)
        if choix_menu_tournoi == 3:
            return
        if choix_menu_tournoi == 4:
            instance_class = OutilsVues()
            instance_class.quitter()
