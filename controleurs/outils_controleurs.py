from tinydb import TinyDB
from time import sleep as sl
import re


class OutilsControleurs:

    def __init__(self, compteur_joueurs_serialiser=0, compteur_tournois_serialiser=0):
        self.compteur_joueurs_serialiser = compteur_joueurs_serialiser
        self.compteur_tournois_serialiser = compteur_tournois_serialiser

    def serialiser_instance_joueur(self, nom, prenom, date_de_naissance, sexe, classement):
        serialized_player = {
            'nom': nom,
            'prenom': prenom,
            'date de naissance': date_de_naissance,
            'sexe': sexe,
            'classement': classement
        }

        db = TinyDB('data/joueurs.json')
        table_joueurs = db.table('Joueur')
        table_joueurs.insert(serialized_player)
        self.compteur_joueurs_serialiser += 1

    def serialiser_instance_tournoi(self, nom, lieu, date, nb_tours, tournees, joueurs, temps, note):
        serialized_tournoi = {
            'nom': nom,
            'lieu': lieu,
            'date': date,
            'nombre de tours': nb_tours,
            'tournees': tournees,
            'joueurs': joueurs,
            'temps': temps,
            'note': note
        }

        db = TinyDB('data/tournoi.json')
        table_tournoi = db.table('Tournoi')
        table_tournoi.insert(serialized_tournoi)
        self.compteur_tournois_serialiser += 1

    def test_date(date):
        if len(date) > 10:
            return 0
        if len(date) < 10:
            return 1
        test_date = re.match(r'[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]', date)
        if test_date:
            return 2
        else:
            return 3
        sl(2)
