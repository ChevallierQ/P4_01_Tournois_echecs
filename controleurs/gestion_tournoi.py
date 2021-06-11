from modeles.paires import Paires
from vues.affichage_tournois import AffichageTournois
from modeles.match import Match


class GestionTournoi:

    def __init__(self, nb_tours, joueurs, num_tournoi):
        self.nb_tours = nb_tours
        self.joueurs = joueurs
        self.num_tournoi = num_tournoi

    def gestion_tournoi(self):
        scores = {}
        x = 1
        while x <= self.nb_tours:
            if x == 1:
                paires = Paires(self.joueurs)
                paires_genere = paires.generation_paires_tour_1()
            if x > 1:
                paires = Paires(self.joueurs, scores)
                paires_genere = paires.generation_paires()
            # tour = Tours()
            nom_joueurs_match = []
            y = 1
            for arg in paires_genere:
                affichage = AffichageTournois("\n")
                affichage.affichage()
                affichage = AffichageTournois("Match {} :".format(y))
                affichage.affichage()
                affichage = AffichageTournois(arg[0])
                affichage.affichage()
                affichage = AffichageTournois(paires_genere[arg][0])
                affichage.affichage()
                nom_joueurs_match.append(arg[0])
                nom_joueurs_match.append(paires_genere[arg][0])
                y += 1
            affichage = AffichageTournois("\nAppuyer sur entrer pour continuer")
            affichage.affichage_input()
            a = 0
            z = 1
            while z <= y - 1:
                match = Match(nom_joueurs_match[a], nom_joueurs_match[a+1])
                affichage = AffichageTournois("\nLe score du match {} : {}".format(z, match.get_tulpe()))
                affichage.affichage()
                z += 1
                a += 2
            input("eeeeeeeeeeee")
            x += 1
