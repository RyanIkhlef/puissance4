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
    # Cette fonction est offerte, elle n'est pas intéressante à créer. C'est pourquoi je laisse l'implémentation.
    # En théorie, elle ne devrait pas être modifiée.
    for ligne_courante in plateau:
        print(ligne_courante)
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

    :param colonne : Numéro de colonne à affecter
    :param jeton : Jeton à poser sur la colonne choisie. (Par defaut, on prendra le jeton du joueur 1 (X)
    :return: null
    """
    # On vérifie que l'input est bon.
    if colonne < 0 or colonne > 6:
        print("la colonne doit être entre 0 et 6")
        return

    # Cela nous permet de travailler directement sur les cases que nous voulons (on abstrait les caractères qui
    # définissent le bord du plateau ("| ").
    colonne += 2

    # On veut lire le plateau à l'envers ici, afin d'ajouter les jetons du bas vers le haut.
    # Le but de cette boucle sera de vérifier que le caractère courant est différent d'une case vide ("_")
        # Si on est dans le cas où la case est vide, il faut remplacer le "_" par le jeton.
            # TIP : Reprendre la fonction de remplacement d'une chaîne de caractère du projet pendu.
        # Si on est dans le cas où la case correspond à un jeton, il faut alors passer à la ligne du dessus et refaire le test.
            # TIP : On peut utiliser le mot-clé "continue" dans ce cas :).
    for :


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
    # On souhaite avoir une boucle qui lit le plateau du bas vers le haut puisque vérifier les cases du haut vers le bas
    # serait une perte de temps.
    # Cette boucle va devoir parcourir toutes les lignes du plateau.
    for :
        # Ici, il faut trouver un moyen de compter le nombre de jetons successifs (une variable par exemple ?)

        # Cette boucle va permettre de parcourir chaque "colonne" de la ligne, c'est-à-dire, chaque caractère de la ligne courante.
        # Dans cette boucle on va vérifier que le jeton correspond au caractère.
            # Si c'est le cas, on compte +1
            # Si ce n'est pas le cas et que notre compteur est déjà à 0, on ne fait rien.
            # Si le caractère courant n'est pas égal au jeton courant ET que le compteur n'est pas à 0, il faut le remettre à 0
        # Dans cette boucle, il faut penser à vérifier que le compteur soit égale à 4.
            # Si il est égal à 4, la partie est gagné ! on peut renvoyer True
            # Sinon, on continue de parcourir les lignes/colonnes.
        for :

    # TIP : Si tu as besoin d'aide pour cette fonction, essaye de faire "est_colonne_gagnante". Il y'a plus d'explication et
    # les deux fonctions sont semblables.
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
    # On souhaite parcourir l'ensemble des colonnes possibles. Pour chaque colonne, il faut vérifier que le jeton du dessus
    # est égal au jeton courant. Si une suite de 4 jetons identique est trouvé, on peut renvoyer True.
    for :
        # Je conseille de stocker dans une variable le nombre de jetons successifs, identique.

        # Cette boucle va parcourir l'ensemble des lignes du tableau du bas vers le haut.
        for :
            # Pour chaque ligne, on regarde le caractère présent au numéro de colonne courant (celui qui correspond à ce que
            # la première boucle fournie).
            caractere = plateau[indice_ligne][colonne]
            if caractere == jeton:
                # Dans ce cas, on incrémente notre compteur
            # Ici, on doit pouvoir remettre à 0 notre compteur si on tombe sur un caractère qui n'est pas le jeton du joueur
            # Car, dans ce cas, cela veut dire qu'on a plus de suite consécutives
            #elif ou else ?

            # Si on a 4 jetons identiques consécutifs, on peut retourner True
            if :
                return True

    return False


def est_gagnant(jeton: str):
    """
    Vérifie qu'une partie est gagnante, c'est-à-dire, que le jeton passé en paramètre est présent 4 fois consécutivement
    sur une ligne OU sur une colonne.

    :param jeton: Jeton pour lequel on veut vérifier la victoire.
    :return: True si la partie est gagnante, False sinon.
    """
    # Je te laisse trouver l'opérateur booléen entre "or" et "and" pour savoir si une partie est gagnée ! :)
    return est_ligne_gagnante(jeton) #or #and ? \
        est_colonne_gagnante(jeton)


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
    # Ici, il suffit de vérifier que pour chaque caractère de la première ligne, il est différent du caractère vide ("_")
    # Si on tombe sur au moins 1 caractère vide, on peut retourner False. Si on ne retourne jamais False dans cette boucle,
    # alors, on a une égalité.
    for :

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
    
    # Tant que personne n'a gagné et que ce n'est pas une égalité.
    while :
        afficher_plateau() 
        # Déterminer le tour du joueur (voir les modulos "%", ça peut aider ;) ).
        if :
            numero_colonne = int(input("[Joueur 1] Entrez le numéro de colonne sur laquelle vous voulez jouer :"))
            if numero_colonne < 0 or numero_colonne > 6:
                print("le numero de ligne doit être compris entre 0 et 6.")
                continue

            poser_jeton(numero_colonne, JETON_JOUEUR_1)
        else:
            numero_colonne = int(input("[Joueur 2] Entrez le numéro de colonne sur laquelle vous voulez jouer :"))
            if numero_colonne < 0 or numero_colonne > 6:
                print("le numero de ligne doit être compris entre 0 et 6.")
                continue

            poser_jeton(numero_colonne, JETON_JOUEUR_2)

    afficher_plateau()

    # Le joueur 1 a-t-il gagné ?
    if :
        print("Bravo joueur 1, vous avez gagné en", tour, "tours !")
    # Le joueur 2 a-t-il gagné ?
    elif :
        print("Bravo joueur 2, vous avez gagné en", tour, "tours !")
    # est-ce une égalité ?
    :
        print("Dommage, la partie se termine sur une égalité ! Vous avez jouer", tour, "tours !")


play()


# A savoir que cette solution ne gère pas le gain par diagonale. On peut également dépasser la taille du puissance 4 en ligne
# Sans que cela ne créer d'erreur (ce qui ne devrait pas arriver)
