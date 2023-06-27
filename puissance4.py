# Définition des variables globales, ces variables vont sérvir à gérer le plateau de jeu

# Une ligne est représentée par les bords : "| ", " |" et des cases vides : "_" (on met un caractère pour les cases vide 
# pour plus de lisibilité.
ligne = "| " + ("_" * 7) + " |"
# On construit le plateau avec ce qu'on appelle en Python une liste par compréhension. Cette notation permet de dire : 
# Pour chaque itération allant de 0 à 6, on ajoute une ligne dans la liste. La variable "plateau" est donc une liste de
# chaîne de caractère. Chaque élément de la liste représente une ligne.
plateau = [ligne for _ in range(6)]
# Pour un peu plus d'esthétique, on ajoute une ligne à la fin du tableau, cette ligne marque la base du jeu.
derniere_ligne = "|" + ("-" * 9) + "|"

JETON_JOUEUR_1 = "X"
JETON_JOUEUR_2 = "O"


def afficher_plateau():
    """
    Affiche l'état actuel du plateau.
    :return: null
    """

    for l in plateau:
        print(l)
    print(derniere_ligne)


def poser_jeton(colonne: int, jeton: str = JETON_JOUEUR_1):
    """
    Pose le jeton du joueur sur la première ligne disponible dans la colonne choisie.
    Par exemple, si on demande de poser le jeton X dans la colonne 0 on obtient :
    | _______ |
    | _______ |
    | _______ |
    | _______ |
    | _______ |
    | X______ |
    |---------|
    Si on demande de poser le jeton O dans la colonne 1, on obtient :
    | _______ |
    | _______ |
    | _______ |
    | _______ |
    | _______ |
    | XO_____ |
    |---------|
    Si on demande de poser le jeton X dans la colonne 0 on obient :
    | _______ |
    | _______ |
    | _______ |
    | _______ |
    | X______ |
    | XO_____ |
    |---------|
    et ainsi de suite.

    :param colonne: Numéro de colonne à affecter
    :param jeton: Jeton à poser sur la colonne choisie. (Par defaut, on prendra le jeton du joueur 1 (X)
    :return: null
    """
    if colonne < 0 or colonne > 7:
        print("la colonne doit être entre 0 et 7")
        return

    colonne += 2

    for indice in range(len(plateau) - 1, -1, -1):
        ligne_courante = plateau[indice]
        if ligne_courante[colonne] != "_":
            continue
        else:
            plateau[indice] = ligne_courante[:colonne] + jeton + ligne_courante[colonne + 1:]
            break


def est_ligne_gagnante(jeton: str):
    """
    Vérifie qu'une ligne est gagnante. Pour rappel, une ligne est gagnante si et seulement si 4 jetons identiques
    se suivent CONSECUTIVEMENT.
    Exemples :
    | _______ |
    | _______ |
    | _______ |
    | _______ |
    | _______ |
    | XXXX___ |
    |---------|
    La ligne 0 est gagnante (le joueur 1 remporte la partie)

    | _______ |
    | _______ |
    | _______ |
    | _______ |
    | _______ |
    | XXXOX__ |
    |---------|
    La ligne 0 n'est pas gagnante, un O vient couper la chaine de 4 X

    :param jeton: Jeton pour lequel on veut une ligne gagnante.
    :return: True si la ligne est gagnante, False sinon.
    """
    for indice in range(len(plateau) - 1, -1, -1):
        nombre_successif = 0
        ligne_courante = plateau[indice]
        for caractere in ligne_courante:
            if caractere == jeton:
                nombre_successif += 1
            elif nombre_successif > 0:
                nombre_successif = 0

            if nombre_successif == 4:
                return True
    return False


def est_colonne_gagnante(jeton: str):
    """
    Vérifie qu'une colonne est gagnante. Pour rappel, une colonne est gagnante si et seulement si 4 jetons identiques
    se suivent CONSECUTIVEMENT.
    Exemple :
    | _______ |
    | _______ |
    | X______ |
    | XO_____ |
    | XO_____ |
    | XO_____ |
    |---------|
    La colonne 0 est gagnante (le joueur 1 remporte la partie).

    | _______ |
    | X______ |
    | O______ |
    | XO_____ |
    | XO_____ |
    | XO_____ |
    |---------|
    La colonne 0 n'est pas gagnante, un O vient couper la chaine de 4 X

    :param jeton: Jeton pour lequel on veut une ligne gagnante.
    :return: True si la ligne est gagnante, False sinon.
    """
    for colonne in range(2, 10):
        nombre_successif = 0
        for indice_ligne in range(len(plateau) - 1, 0, -1):
            caractere = plateau[indice_ligne][colonne]
            if caractere == jeton:
                nombre_successif += 1
            elif nombre_successif > 0:
                nombre_successif = 0

            if nombre_successif == 4:
                return True

    return False


def est_gagnant(jeton: str):
    """
    Vérifie qu'une partie est gagnante, c'est-à-dire, que le jeton passé en paramètre est présent 4 fois consécutivement
    sur une ligne OU sur une colonne.

    :param jeton: Jeton pour lequel on veut vérifier la victoire.
    :return: True si la partie est gagnante, False sinon.
    """
    return est_ligne_gagnante(jeton) or est_colonne_gagnante(jeton)


def est_egalite():
    """
    Fonction qui vérifie s'il y a une égalité.
    Exemple d'égalité :
    | OXOXOXO |
    | XOXOXOX |
    | OXOXOXO |
    | XOXOXOX |
    | OXOXOXO |
    | XOXOXOX |
    |---------|

    :return: True en cas d'égalité, False, sinon
    """
    premiere_ligne = plateau[0]
    for caractere in premiere_ligne:
        if caractere == "_":
            return False

    return True


def play():
    """
    Fonction principale du programme. Cette fonction doit boucler de manière infinie tant que le jeu n'est pas terminé.
    Le jeu est terminé dans 3 cas :
        1. La partie est gagnée par le joueur 1
        2. La partie est gagnée par le joueur 2
        3. Une égalité a été réalisée (une égalité survient quand toutes les cases ont été utilisées).
    Cette boucle doit faire jouer à tour de rôle les deux joueurs (joueur 1 et joueur 2). A chaque tour, elle doit donc
    s'adresser à la bonne personne pour indiquer l'action attendue. Une fois que le joueur à décider où il voulait jouer,
    il faut poser le jeton du joueur à cette position et ensuite.
    On terminera cette fonction par une indication de la personne gagnante.

    :return: null
    """
    tour = 0
    joueur1_a_gagne = False
    joueur2_a_gagne = False
    egalite = False
    while not joueur1_a_gagne and not joueur2_a_gagne and not egalite:
        afficher_plateau()
        if tour % 2 == 0:
            numero_colonne = int(input("[Joueur 1] Entrez le numéro de colonne sur laquelle vous voulez jouer :"))
            if numero_colonne < 0 or numero_colonne > 6:
                print("le numero de ligne doit être compris entre 0 et 6.")
                continue
            tour += 1
            poser_jeton(numero_colonne, JETON_JOUEUR_1)
        else:
            numero_colonne = int(input("[Joueur 2] Entrez le numéro de colonne sur laquelle vous voulez jouer :"))
            if numero_colonne < 0 or numero_colonne > 6:
                print("le numero de ligne doit être compris entre 0 et 6.")
                continue
            tour += 1
            poser_jeton(numero_colonne, JETON_JOUEUR_2)

        joueur1_a_gagne = est_gagnant(JETON_JOUEUR_1)
        joueur2_a_gagne = est_gagnant(JETON_JOUEUR_2)
        egalite = est_egalite()

    afficher_plateau()

    if joueur1_a_gagne:
        print("Bravo joueur 1, vous avez gagné en", tour, "tours !")
    elif joueur2_a_gagne:
        print("Bravo joueur 2, vous avez gagné en", tour, "tours !")
    else:
        print("Dommage, la partie se termine sur une égalité ! Vous avez jouer", tour, "tours !")


play()


# A savoir que cette solution ne gère pas le gain par diagonale. On peut également dépasser la taille du puissance 4 en ligne
# Sans que cela ne créer d'erreur (ce qui ne devrait pas arriver)
