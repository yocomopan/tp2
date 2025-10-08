"""
2025-09-29
Ivan Zheryakov
Guessing the number
"""

import random

# Variables
number = random.randint(10, 30)
# attempts_required = random.randint(10, 30)
attempts = 0

play_game = True
guessing = True
players_try = 0
lower_bounds = 0
higher_bounds = 100


def min():
    # Variable minimale
    lower_bounds = int(input("chiffre minimale SVP: "))
    # limite du plus petit nombre possible, donc pas moins que 0
    if lower_bounds < 0:
        print("OOPS! Desole, pas moins que 0")
    return lower_bounds

def max():
    # Variable maximale
    higher_bounds = int(input("chiffre maximale SVP: "))
    # limite du plus grand nombre possible, donc pas plus que 100
    if higher_bounds > 100:
        print("OOPS! Desole, pas plus que 100")
    return higher_bounds


while play_game:
    input("Appuyer pour commencer")

    choice = input("Voulez-vous changer les bornes? y/n ")
    if choice == "y":
        number = random.randint(max(), min())
        print(f"J'ai choisi un nombre entre {lower_bounds} et {higher_bounds} ")
    else:

        # Ordinateur choisi son chiffre entre la valeur maximale et minimale choisi.
        number = random.randint(lower_bounds, higher_bounds)
        print(f"J'ai choisi un nombre entre {lower_bounds} et {higher_bounds} ")

    while guessing:

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
                guessing = False
                Play_game = True
                attempts = 0

# Demander au joueur s'il veut jouer encore.
# Si non, play_game = False
