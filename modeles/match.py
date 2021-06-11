from time import sleep as sl


class Match:
    def __init__(self, joueur_a, joueur_b):
        self.joueur_a = joueur_a
        self.joueur_b = joueur_b

        score_joueur_a = 2
        score_joueur_b = 2
        print("\n---------------------------")
        while score_joueur_a == 2:
            try:
                score = int(input("\nScore du joueur {}\n\n1 - Gagnant 1p\
                    \n2 - Perdant 0p\n3 - Match nul 1/2p\n\nVotre choix : ".format(joueur_a)))
            except ValueError:
                print("\nVous n'avez pas saisi une valeur valide.")
                sl(2)
                continue
            if score == 1:
                score_joueur_a = 1
                score_joueur_b = 0
                break
            if score == 2:
                score_joueur_a = 0
                score_joueur_b = 1
                break
            if score == 3:
                score_joueur_a = 0, 5
                score_joueur_b = 0, 5
                break
        self.score_joueur_a = score_joueur_a
        self.score_joueur_b = score_joueur_b

    def get_tulpe(self):
        liste_joueur_a = ()
        liste_joueur_b = ()
        tuple = []
        liste_joueur_a = self.joueur_a, self.score_joueur_a
        liste_joueur_b = self.joueur_b, self.score_joueur_b
        tuple.append(liste_joueur_a)
        tuple.append(liste_joueur_b)
        return tuple
