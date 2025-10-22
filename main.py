"""
2025-09-29
Ivan Zheryakov
Guessing the number
"""
# On est import la module de random
import random

# =-=-=-= Variables =-=-=-=
number = random.randint(0, 100)  # Generateur de nombre

# Les boucles du jeu. Si faux = Programme termine
play_game = True
guessing = True

# Le nombre d'essaie que le joueur fera.
attempts = 0
players_try = 0

# Les bornes maximales et minimales
lower_bounds = 0
higher_bounds = 100


# =-=-=-= Definitions =-=-=-=
def mini():  # La definition mini() permet de changer la borne minimale
    # lower_bounds = global, sinon le programme pensera que c'est une nouvelle varaible
    global lower_bounds
    lower_bounds = int(input("chiffre minimale SVP: "))
    if lower_bounds < 0:  # Si c'est plus petit que 0, forcer d'utiliser 0 .
        print("OOPS! Desole, pas moins que 0")
        lower_bounds = 0
    return lower_bounds  # nouvelle information retourne au "number"


def maxi():  # La definition maxi() permet de changer la borne maximale
    # higher_bounds = global, sinon le programme pensera que c'est une nouvelle varaible
    global higher_bounds
    higher_bounds = int(input("chiffre maximale SVP: "))
    if higher_bounds > 100:  # Si c'est plus grand que 100, forcer d'utiliser 100 .
        print("OOPS! Desole, pas plus que 100")
        higher_bounds = 100
    return higher_bounds  # nouvelle information retourne au "number"


# =-=-=-= Code Principal =-=-=-=
while play_game:  # La boucle qui permet a l'usager de rejouer.
    input("Appuyer pour commencer")

    # Choix de changer les bornes
    choice = input("Voulez-vous changer les bornes? y/n ")

    if choice == "y":
        # Si oui, les bornes sont envoyees aux def() pour recevoir de la nouvelle information
        # L'ordinateur choisi son chiffre entre les bornes modifiees.
        number = random.randint(mini(), maxi())
        print(f"J'ai choisi un nombre entre {lower_bounds} et {higher_bounds} ")

    else:
        # Si non, l'ordinateur choisi son chiffre entre les bornes originaux.
        number = random.randint(lower_bounds, higher_bounds)
        print(f"J'ai choisi un nombre entre {lower_bounds} et {higher_bounds} ")

    guessing = True  # Reactive le jeu pour laisser l'usager jouer. Plus de details a la ligne 91

    # >>> Jeu <<<
    while guessing:

        # L'usager essaie de deviner le chiffre choisi.
        players_try = int(input("Votre reponse? "))
        attempts += 1

        if players_try < lower_bounds or players_try > higher_bounds:
            print(f"entre {lower_bounds} et {higher_bounds}.")
            continue

        if players_try > number:
            print("Je n'en voudrais plus de brownie special")

        elif players_try < number:
            print("C'est fini Anakin, j'ai la haute main! ")

        else:
            guessing = True
            print(f"Bravo, vous avez reussis en {attempts} essaies")
            decisions = input("Voulez-vous rejouer? y/n ")
            if decisions == "n":
                print("Merci et bon soir.")
                guessing = False
                play_game = False

            else:
                lower_bounds = 0
                higher_bounds = 100
                guessing = False
                Play_game = True
                attempts = 0

