from time import sleep as sl
from controleurs.outils_controleurs import OutilsControleurs


class Tours:

    def __init__(self, nom="", date_debut="", heure_debut="", date_fin="", heure_fin=""):
        self.nom = nom
        self.date_debut = date_debut
        self.heure_debut = heure_debut
        self.date_fin = date_fin
        self.heure_fin = heure_fin

        valide = False
        while not valide:
            print("\n---------------------------")
            while len(nom) == 0:
                try:
                    nom = str(input("\nNom du tour : "))
                except ValueError:
                    print("\nVous n'avez pas saisi un nom valide.")
                    sl(2)
                    continue

            print("\n---------------------------")
            while len(date_debut) == 0:
                try:
                    date_debut = str(input("\nDate de debut\nFormat : jj/mm/aaaa : "))
                except ValueError:
                    print("\nVous n'avez pas saisi une date valide.")
                    sl(2)
                    continue
                test_date = OutilsControleurs.test_date(date_debut)
                if test_date == 0:
                    print("\nVous avez saisi une valeur trop grande.")
                    date_debut = ""
                if test_date == 1:
                    print("\nVous avez saisi une valeur trop petite.")
                    date_debut = ""
                if test_date == 2:
                    break
                if test_date == 3:
                    print("\nVous avez saisi un format de date incorrect.")
                    date_debut = ""

            print("\n---------------------------")
            while len(heure_debut) == 0:
                try:
                    heure_debut = str(input("\nHeure de debut\nFormat : hh:mm : "))
                except ValueError:
                    print("\nVous n'avez pas saisi une heure valide.")
                    sl(2)
                    continue
                test_heure = OutilsControleurs.test_heure(heure_debut)
                if test_heure == 0:
                    print("\nVous avez saisi une valeur trop grande.")
                    heure_debut = ""
                if test_heure == 1:
                    print("\nVous avez saisi une valeur trop petite.")
                    heure_debut = ""
                if test_heure == 2:
                    break
                if test_heure == 3:
                    print("\nVous avez saisi un format d'heure incorrect.")
                    heure_debut = ""

            print("\n---------------------------")
            validation = 0
            print("\n{}\n{}\n{}".format(nom, date_debut, heure_debut))
            while validation == 0:
                try:
                    validation = int(input("\nVoulez-vous valider ?\
                        \n\n1 - Valider\n2 - Recommencer\n\nVotre choix : "))
                except ValueError:
                    print("\nVous n'avez pas saisi une valeur valide.")
                    sl(2)
                    continue
                if validation == 1:
                    print("\n---------------------------")
                    valide = True
                else:
                    nom = ""
                    date_debut = ""
                    heure_debut = ""
