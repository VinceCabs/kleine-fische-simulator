# -*-coding:utf8;-*-
# TODO switch all to English
# TODO plot # of turns distribution
# TODO DocStrings

import random

# Simulator params
taille = 11  # standard board size
pos_poissons = 6  # standard fish position
nb_parties_simul = 10000  # nb of games to simulate


# Simulator
# TODO set those lists as Partie class attributes
tours_win_pe = []
tours_win_po = []


class Partie:
    def __init__(self):
        self.tour = 0
        self.tranches = 0
        self.pecheurs = {"rouge": 0, "vert": 0}
        self.poissons = {
            "bleu": pos_poissons,
            "rose": pos_poissons,
            "orange": pos_poissons,
            "gu": pos_poissons,
        }

        self.mer = []
        self.bateau = []

    def de(self) -> str:
        """tir au de, renvoie une couleur

        Returns : 
            couleur (str): couleur tiree au de
        """

        d = ["bleu", "vert", "rouge", "rose", "orange", "gu"]
        couleur = random.choice(d)
        return couleur

    def mouv_poisson(self, couleur: str):
        """fait avancer un poisson de la couleur qu'on veut.
        S'il arrive dans la mer, on l'ajoute à la liste mer.
        S'il est déjà dans la mer, on fait avancer un autre poisson (appel d'une autre fonction) 

        Parameters :
            couleur (str): couleur du poisson a faire avancer

        Returns : 
            null
        """

        self.tour += 1
        if couleur not in self.poissons:
            self.mouv_poisson_alea()
            # self.mouv_poisson_opt()
        else:
            pos = self.poissons[couleur]
            if pos < taille:
                self.poissons[couleur] = pos + 1
            else:
                self.mer.append(couleur)
                self.poissons.pop(couleur)

    def mouv_poisson_alea(self):
        # fait avancer un poisson de manière aléatoire
        poisson = random.choice(list(self.poissons))
        self.mouv_poisson(poisson)

    def mouv_poisson_opt(self):
        # fait avancer le poisson le plus avancé (=le plus proche de la mer)
        max = 0
        poisson_max = ""
        for poisson in list(self.poissons.keys()):
            if self.poissons[poisson] > max:
                poisson_max = poisson

        self.mouv_poisson(poisson_max)

    def print_partie(self):
        print(
            "{0}:     poissons:{1}    pecheurs:{2}    mer:{3}     bateau:{4}".format(
                self.tour, self.poissons, self.tranches, self.mer, self.bateau
            )
        )

    def partie_finie(self) -> bool:
        if len(self.mer) > 1:
            # Poissons gagnent !
            tours_win_po.append(self.tour)
            return True
        elif len(self.bateau) > 2:
            # pêcheurs gagnent !
            tours_win_pe.append(self.tour)
            return True
        else:
            return False

    def mouv_pecheurs(self):
        self.tour += 1
        self.tranches += 1
        # les poissons peches sont mis dans le bateau
        for poisson in list(self.poissons.keys()):
            if self.poissons[poisson] == self.tranches:
                self.bateau.append(poisson)
                del self.poissons[poisson]

    def lancer_de(self):
        c = self.de()
        if c in ["vert", "rouge"]:
            self.mouv_pecheurs()
        else:
            self.mouv_poisson(c)

    def jouer_partie(self):
        while True:
            self.lancer_de()
            if self.partie_finie():
                break


def print_parties_gagnees(
    parties_gagnees_poissons: list, parties_gagnees_pecheurs: list
):

    nb_gagnees_poissons = len(parties_gagnees_poissons)
    nb_gagnees_pecheurs = len(parties_gagnees_pecheurs)
    print(
        "poissons: {0}    pecheurs: {1}    chance poissons: {2}".format(
            nb_gagnees_poissons,
            nb_gagnees_pecheurs,
            nb_gagnees_poissons / (nb_gagnees_poissons + nb_gagnees_pecheurs),
        )
    )
    print(
        "nb tours moyen: {2}    nb tours moy poissons: {0}  nb tours moyen pecheurs: {1}".format(
            sum(parties_gagnees_poissons) / nb_gagnees_poissons,
            sum(parties_gagnees_pecheurs) / nb_gagnees_pecheurs,
            (sum(parties_gagnees_poissons) + sum(parties_gagnees_pecheurs)) /
            (nb_gagnees_poissons + nb_gagnees_pecheurs),
        )
    )


def main():
    for _ in range(nb_parties_simul):
        p = Partie()
        p.jouer_partie()
    print_parties_gagnees(tours_win_po, tours_win_pe)


if __name__ == "__main__":
    main()
