from modeles.joueur import Joueur


class Paires:

    def __init__(self, joueurs, score={}):
        self.joueurs = joueurs
        self.score = score

    def generation_paires_tour_1(self):
        classement_joueurs_reprise = []
        for joueur in self.joueurs:
            classement_joueurs_reprise.append(Joueur.get_classement_joueur(joueur))
        dict_classement_joueurs = {}
        x = 0
        while x <= len(self.joueurs) - 1:
            dict_classement_joueurs[self.joueurs[x]] = classement_joueurs_reprise[x]
            x += 1
        dict_classement_joueurs = sorted(dict_classement_joueurs.items(), key=lambda t: t[1])
        dict_classement_joueurs_1 = dict_classement_joueurs[:4]
        dict_classement_joueurs_2 = dict_classement_joueurs[4:]
        dict_paires_genere = {}
        x = 0
        while x <= len(dict_classement_joueurs_1) - 1:
            dict_paires_genere[dict_classement_joueurs_1[x]] = dict_classement_joueurs_2[x]
            x += 1
        return dict_paires_genere

    def generation_paires(self):
        return
