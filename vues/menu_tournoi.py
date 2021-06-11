from time import sleep as sl
from os import system as sys
from vues.outils_vues import OutilsVues
from controleurs.outils_controleurs import OutilsControleurs
from modeles.tournoi import Tournoi
from controleurs.gestion_tournoi import GestionTournoi


def menu_tournoi():
    valeur_quitter = 0
    while valeur_quitter != 1:
        sys(OutilsControleurs.which_os())
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
            print("\n---------------------------\n")
            x = 1
            liste_tounois = Tournoi.tournois_liste()
            if liste_tounois == 0:
                print("Il n'y a aucun tournois d'enregistrer, veuillez ajouter un tournoi via le menu.")
                input("\nAppuyer sur entrer pour continuer")
                return
            for arg in liste_tounois:
                print("Indice tournoi : {}\n{}".format(x, arg))
                x += 1
            choix_tournoi_reprise = 0
            while choix_tournoi_reprise == 0:
                try:
                    choix_tournoi_reprise = int(input("\nSelectionnez un tournoi : "))
                except ValueError:
                    print("\nVous n'avez pas saisi un chiffre.")
            data_tournoi_reprise = Tournoi.get_data_tournoi(choix_tournoi_reprise)
            joueurs_tournoi_reprise = Tournoi.get_joueurs_tournoi_reprise(data_tournoi_reprise)
            # nb de tours
            gestion_tournoi = GestionTournoi(1, joueurs_tournoi_reprise, choix_tournoi_reprise)
            gestion_tournoi.gestion_tournoi()
        if choix_menu_tournoi == 3:
            return
        if choix_menu_tournoi == 4:
            instance_class = OutilsVues()
            instance_class.quitter()
