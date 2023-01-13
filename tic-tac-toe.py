import random

# Plateau
plateau = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

partie_en_cours = True

# Aucun gagnant définie
gagnant = None

# Le joueur des X commence
joueur_actuel = "X"


# Lance une partie
def jouer():
    # Annonce des score totaux
    score_totaux()
    # Choix du type de partie
    nombre_joueur = input("Taper 1 pour jouer avec un joueur ou taper 2 pour jouer avec une IA:")
    # Partie contre un Joueur
    if nombre_joueur == "1":
        # Affiche le plateau de jeu
        plateau_jeu()
        while partie_en_cours:
            # Le joueur actuel joue
            tour(joueur_actuel)
            # Vérifie si la partie est fini durant ce tour
            partie_terminer()
            # La main passe au joueur suivant
            joueur_suivant()
        # Annonce du gagnant ou égalité en partie contre joueurs
        if gagnant == "X":
            print("Le joueur des", gagnant, "à gagné.")
            historique = open("Historique.txt", "a")
            score = "\nPartie joueurs: Victoire X"
            historique.write(score)
            historique.close()
        elif gagnant == "O":
            print("Le joueur des", gagnant, "à gagné.")
            historique = open("Historique.txt", "a")
            score = "\nPartie joueurs: Victoire O"
            historique.write(score)
            historique.close()
        elif gagnant is None:
            print("Égalité.")
            historique = open("Historique.txt", "a")
            score = "\nPartie joueurs: Égalité"
            historique.write(score)
            historique.close()
    # Partie contre IA
    elif nombre_joueur == "2":
        # Affiche le plateau de jeu
        plateau_jeu()
        while partie_en_cours:
            # Le joueur actuel joue
            tour(joueur_actuel)
            # Vérifie si la partie est fini durant ce tour
            partie_terminer()
            # La main passe au joueur suivant
            joueur_suivant()
            partie_terminer()
            # L'IA joue automatiquement
            ia()
            partie_terminer()
        # Annonce du gagnant ou égalité en partie en contre IA
        if gagnant == "X":
            print("Vous avez gagné.")
            historique = open("Historique.txt", "a")
            score = "\nPartie Solo: Victoire Humain"
            historique.write(score)
            historique.close()
        elif gagnant == "O":
            print("L'IA a gagné")
            historique = open("Historique.txt", "a")
            score = "\nPartie Solo: Victoire IA"
            historique.write(score)
            historique.close()
        elif gagnant is None:
            print("Égalité.")
            historique = open("Historique.txt", "a")
            score = "\nPartie Solo: Égalité"
            historique.write(score)
            historique.close()


def score_totaux():
    # Annonce des score totaux
    score = open("Historique.txt", "rt")
    historique_score = score.read()
    score_ia = historique_score.split("IA")
    print("Score de l'IA :", len(score_ia) - 1)
    score_o = historique_score.split("O")
    print("Score du joueur des O :", len(score_o) - 1)
    score_x = historique_score.split("X")
    print("Score du joueur des X :", len(score_x) - 1)
    score_x_vs_ia = historique_score.split("Humain")
    print("Score du joueur contre l'IA :", len(score_x_vs_ia) - 1)


# Affiche le plateau de jeu et un exemple pour savoir à quel chiffre correspond à chaque emplacement
def plateau_jeu():
    print("\n")
    print(plateau[0] + " | " + plateau[1] + " | " + plateau[2] + "     0 | 1 | 2")
    print(plateau[3] + " | " + plateau[4] + " | " + plateau[5] + "     3 | 4 | 5")
    print(plateau[6] + " | " + plateau[7] + " | " + plateau[8] + "     6 | 7 | 8")
    print("\n")


# IA qui joue de façon aléatoire
def ia():
    global plateau
    global partie_en_cours
    global joueur_actuel
    if gagnant == "X":
        partie_terminer()
    else:
        while joueur_actuel == "O":
            ia_placement = int(random.randrange(0, 8))
            if "-" not in plateau:
                partie_terminer()
                break
            elif plateau[ia_placement] == "-":
                print("Tour de l'IA")
                plateau[ia_placement] = "O"
                partie_terminer()
                joueur_actuel = "X"
                break
            else:
                continue

    return plateau_jeu()


# Gestion du tour des tours
def tour(joueur):
    # Annonce du joueur qui doit jouer
    print(joueur, "doit jouer son tour")
    emplacement = input("Choisi un emplacement entre 0 et 8: ")

    # Vérifie que l'emplacement
    valide = False
    while not valide:

        # Vérifie que l'emplacement choisi est valide
        while emplacement not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            emplacement = input("Choisi un emplacement entre 0 et 8 : ")

        emplacement = int(emplacement)

        # Vérifie que l'emplacement n'est pas déjà choisi
        if plateau[emplacement] == "-":
            valide = True
        else:
            print("Emplacement déjà pris ou invalide. Choisi un emplacement entre 0 et 8 : ")

    # Place le X ou le O selon le joueur a l'emplacement choisi
    plateau[emplacement] = joueur

    # Affiche le plateau avec les changements
    plateau_jeu()


# Vérifie si la partie est gagné ou à égalité
def partie_terminer():
    partie_gagner()
    partie_egaliter()


# Vérifie s'il y a un gagnant
def partie_gagner():
    global gagnant
    # Verifie si une des 3 conditions est remplie
    victoire_ligne = ligne()
    victoire_colonne = colonne()
    victoire_diagonale = diagonale()
    # Valide la victoire si une des conditions précédentes est remplie
    if victoire_ligne:
        gagnant = victoire_ligne
    elif victoire_colonne:
        gagnant = victoire_colonne
    elif victoire_diagonale:
        gagnant = victoire_diagonale
    else:
        gagnant = None


# Vérifie si la condition de victoire en ligne est remplie
def ligne():
    global partie_en_cours
    #  Verfie si la condition de victoire en ligne est remplie
    ligne_1 = plateau[0] == plateau[1] == plateau[2] != "-"
    ligne_2 = plateau[3] == plateau[4] == plateau[5] != "-"
    ligne_3 = plateau[6] == plateau[7] == plateau[8] != "-"
    # Stop la partie quand 3 symboles sont aligné
    if ligne_1 or ligne_2 or ligne_3:
        partie_en_cours = False
    # Vérifie si l'une des lignes commençant par l'index 0 ou 3 ou 6 remplie les conditions
    if ligne_1:
        return plateau[0]
    elif ligne_2:
        return plateau[3]
    elif ligne_3:
        return plateau[6]
        # Si aucun gagnant la partie continue
    else:
        return None


# Vérifie si la condition de victoire en colonne est remplie
def colonne():
    global partie_en_cours
    # Verfie si la condition de victoire en colonne est remplie
    colonne_1 = plateau[0] == plateau[3] == plateau[6] != "-"
    colonne_2 = plateau[1] == plateau[4] == plateau[7] != "-"
    colonne_3 = plateau[2] == plateau[5] == plateau[8] != "-"
    # Stop la partie quand 3 symboles sont aligné
    if colonne_1 or colonne_2 or colonne_3:
        partie_en_cours = False
    # Vérifie si l'une des colonnes commençant par l'index 0 ou 1 ou 2 remplie les conditions
    if colonne_1:
        return plateau[0]
    elif colonne_2:
        return plateau[1]
    elif colonne_3:
        return plateau[2]
        # Si aucun gagnant la partie continue
    else:
        return None


# Vérifie si la condition de victoire en diagonale est remplie
def diagonale():
    global partie_en_cours
    # Vérifie si la condition de victoire en diagonale est remplie
    diagonale_1 = plateau[0] == plateau[4] == plateau[8] != "-"
    diagonale_2 = plateau[2] == plateau[4] == plateau[6] != "-"
    # Stop la partie quand 3 symboles sont aligné
    if diagonale_1 or diagonale_2:
        partie_en_cours = False
    # Vérifie si l'une des diagonales commençant par l'index 0 ou 2 remplie les conditions
    if diagonale_1:
        return plateau[0]
    elif diagonale_2:
        return plateau[2]
    # Si aucun gagnant la partie continue
    else:
        return None


# Vérifie s'il y a une égalité
def partie_egaliter():
    global partie_en_cours
    # Vérifie que il n y a plus de case libre
    if "-" not in plateau:
        partie_en_cours = False
        return True
    # Sinon il n y a pas d'égalité
    else:
        return False


# Changement de joueur après chaque input
def joueur_suivant():
    global joueur_actuel
    # Si les X ont joué le joueur devient O
    if joueur_actuel == "X":
        joueur_actuel = "O"
    # Si les O ont joué le joueur devient X
    elif joueur_actuel == "O":
        joueur_actuel = "X"


jouer()
