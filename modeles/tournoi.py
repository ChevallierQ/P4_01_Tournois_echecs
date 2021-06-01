from time import sleep as sl
from vues.outils_vues import OutilsVues
from controleurs.outils_controleurs import OutilsControleurs
from modeles.joueur import Joueur
import json


class Tournoi:

    def __init__(self, nom="", lieu="", date="", nb_tours=4, tournees=0, joueurs=[], temps="", note=""):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nb_tours = nb_tours
        self.tournees = tournees
        self.joueurs = joueurs
        self.temps = temps
        self.note = note

        print("\n---------------------------")
        while len(nom) == 0:
            try:
                nom = str(input("\nNom : "))
            except ValueError:
                print("\nVous n'avez pas saisi un nom valide.")
                sl(2)
                continue

        print("\n---------------------------")
        while len(lieu) == 0:
            try:
                lieu = str(input("\nLieu : "))
            except ValueError:
                print("\nVous n'avez pas saisi un lieu valide.")
                sl(2)
                continue

        print("\n---------------------------")
        while len(date) == 0:
            try:
                date = str(input("\nDate\nFormat : jj/mm/aaaa : "))
            except ValueError:
                print("\nVous n'avez pas saisi une date valide.")
                sl(2)
                continue
            test_date = OutilsControleurs.test_date(date)
            if test_date == 0:
                print("\nVous avez saisi une valeur trop grande.")
                date = ""
            if test_date == 1:
                print("\nVous avez saisi une valeur trop petite.")
                date = ""
            if test_date == 2:
                break
            if test_date == 3:
                print("\nVous avez saisi un format de date incorrect.")
                date = ""

        print("\n---------------------------")
        nb_tours_modif = ""
        while nb_tours_modif != 2 or nb_tours_modif != 1:
            try:
                nb_tours_modif = int(input("\nNombre de tours\nPar default le nombre est de 4\
                    \nVoulez-vous modifier cette valeur ?\n\n1 - Oui\n2 - Non\n\nVotre choix: "))
            except ValueError:
                print("\nVous n'avez pas saisi un nombre valide.")
                sl(2)
                continue
            if nb_tours_modif == 1:
                while nb_tours == 4:
                    try:
                        nb_tours = int(input("\nNombre de tours : "))
                    except ValueError:
                        print("\nVous n'avez pas saisi un nombre valide.")
                        sl(2)
                        continue
                    if nb_tours == 4:
                        break
                break
            if nb_tours_modif == 2:
                break

        print("\n---------------------------")
        # while tournees == 0 :
        #     try:
        #         tournees = str(input("\nListe des instances rondes : "))
        #     except ValueError:
        #         print("\nVous n'avez pas saisi une valeur valide.")
        #         sl(2)
        #         continue

        print("\n---------------------------\n\nListe des joueurs :\n")
        liste_joueurs_tournois = Joueur.joueurs_tournoi()
        if liste_joueurs_tournois == 0:
            print("Il n'y a pas ou pas suffisament de joueurs pour organiser un tounois\
                , veuillez ajouter des joueurs via le menu.")
            input("\nAppuyer sur entrer pour continuer")
            return
        for arg in liste_joueurs_tournois:
            print(arg)
        x = 8
        while x != 0:
            try:
                joueurs.append(int(input("Saisir encore {} indice de joueurs : ".format(x))))
            except ValueError:
                print("\nVous n'avez pas saisi un indice valide.")
                sl(2)
                continue
            x -= 1
        joueurs = Joueur.get_joueurs_tournoi(joueurs, Joueur.joueurs_alpha())

        print("\n---------------------------")
        temps_choix = 0
        while temps_choix != 1 or temps_choix != 2 or temps_choix != 3:
            try:
                temps_choix = int(input("\nContrôle de temps\n1 - Bullet\
                    \n2 - Blitz\n3 - Coup rapide\n\nVotre choix : "))
            except ValueError:
                print("\nVous n'avez pas saisi une valeur valide.")
                sl(2)
                continue
            if temps_choix == 1:
                temps = "Bullet"
                break
            if temps_choix == 2:
                temps = "Blitz"
                break
            if temps_choix == 3:
                temps = "Coup rapide"
                break

        print("\n---------------------------")
        while len(note) == 0:
            try:
                note = str(input("\nDescription : "))
            except ValueError:
                print("\nVous n'avez pas saisi une valeur valide.")
                sl(2)
                continue
            if len(note) == 0:
                break

        instance_class = OutilsVues()
        if instance_class.sauvegarde(nom, lieu, date, nb_tours, tournees, joueurs, temps, note) == 1:
            instance_class_serialiser = OutilsControleurs()
            instance_class_serialiser.serialiser_instance_tournoi(nom, lieu, date,
                                                                  nb_tours, tournees, joueurs, temps, note)

    def tournois_liste():
        with open('data/tournoi.json', 'r') as tournois_data:
            data_dict = json.load(tournois_data)
            tournoi_list = []
            nom = ''
            lieu = ''
            date = ''
            for tournoi in data_dict.values():
                for num_tournoi in tournoi.values():
                    for cle, valeur in num_tournoi.items():
                        if cle == 'nom':
                            nom = valeur
                        if cle == 'lieu':
                            lieu = valeur
                        if cle == 'date':
                            date = valeur
                    nom_lieu_date = nom + '\n' + lieu + '\n' + date + '\n'
                    tournoi_list.append(nom_lieu_date)
                    tournoi_list.sort()
            if len(tournoi_list) < 2:
                return 0
            if len(tournoi_list) >= 1:
                del tournoi_list[0]
                return tournoi_list
