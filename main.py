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

while play_game:
    input("Appuyer pour commencer")
    # Variable minimale
    a = int(input("chiffre minimale SVP: "))
    # limite du plus petit nombre possible, donc pas moins que 0
    if a < 0:
        print("OOPS! Desole, pas moins que 0")
        continue
    # Variable maximale
    b = int(input("chiffre maximale SVP: "))
    # limite du plus grand nombre possible, donc pas plus que 100
    if b > 100:
        print("OOPS! Desole, pas plus que 100")
        continue
    # Ordinateur choisi son chiffre entre la valeur maximale et minimale choisi.
    number = random.randint(a, b)
    print(f"J'ai choisi un nombre entre {a} et {b} ")
    while guessing:

        players_try = int(input("une autre essaie? "))
        attempts += 1

        if players_try < a or players_try > b:
            print(f"entre {a} et {b}.")
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
                guessing = True
                attempts = 0
                a = int(input("chiffre minimale SVP: "))
                # limite du plus petit nombre possible, donc pas moins que 0
                if a < 0:
                    print("OOPS! Desole, pas moins que 0")
                    exit(guessing)

                b = int(input("chiffre maximale SVP: "))
                # limite du plus grand nombre possible, donc pas plus que 100
                if b > 100:
                    print("OOPS! Desole, pas plus que 100")
                    exit(guessing)

                number = random.randint(a, b)
                print(f"J'ai choisi un nombre entre {a} et {b} ")

# Demander au joueur s'il veut jouer encore.
# Si non, play_game = False
