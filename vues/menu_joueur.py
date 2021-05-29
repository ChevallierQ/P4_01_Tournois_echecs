from time import sleep as sl
from os import system as sys
from vues.outils_vues import OutilsVues
from vues.menu_joueur_liste import menu_joueur_liste
from modeles.joueur import Joueur


def menu_joueur():
    valeur_quitter = 0
    while valeur_quitter != 1:
        sys("clear")
        print("\nMenu joueurs: ")
        print("\n1 - Liste des joueurs\n2 - Ajout d'un joueur\n3 - Retour\n4 - Quitter")
        try:
            choix_menu_joueur = int(input("\nVotre choix: "))
        except ValueError:
            print("\nVous n'avez pas saisi un chiffre.")
            sl(2)
            continue
        if choix_menu_joueur == 1:
            menu_joueur_liste()
        if choix_menu_joueur == 2:
            Joueur()
        if choix_menu_joueur == 3:
            return
        if choix_menu_joueur == 4:
            instance_class = OutilsVues()
            instance_class.quitter()
