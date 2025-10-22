"""
2025-09-29
Ivan Zheryakov
Guessing the number
"""

import random

number = random.randint(0, 100)

play_game = True
guessing = True

attempts = 0
players_try = 0

lower_bounds = 0
higher_bounds = 100


def mini():
    """
    La definition mini() permet de changer la borne minimale
    :return: La borne minimale.
    """
    global lower_bounds
    lower_bounds = int(input("chiffre minimale SVP: "))
    if lower_bounds < 0:
        print("OOPS! Desole, pas moins que 0")
        lower_bounds = 0
    return lower_bounds


def maxi():
    """
    La definition maxi() per,et de retourner la borne maximale
    :return: La borne maximale
    """
    global higher_bounds
    higher_bounds = int(input("chiffre maximale SVP: "))
    if higher_bounds > 100:
        print("OOPS! Desole, pas plus que 100")
        higher_bounds = 100
    return higher_bounds


while play_game:

    input("Appuyer pour commencer")
    choice = input("Voulez-vous changer les bornes? y/n ")

    if choice == "y":
        number = random.randint(mini(), maxi())
        print(f"J'ai choisi un nombre entre {lower_bounds} et {higher_bounds} ")

    else:
        number = random.randint(lower_bounds, higher_bounds)
        print(f"J'ai choisi un nombre entre {lower_bounds} et {higher_bounds} ")

    guessing = True

    while guessing:
        players_try = int(input("Votre reponse? "))
        attempts += 1

        if players_try < lower_bounds or players_try > higher_bounds:
            print(f"entre {lower_bounds} et {higher_bounds}.")
            continue

        if players_try > number:
            print("C'est trop! (Diminue)")

        elif players_try < number:
            print("C'est fini Anakin, j'ai la haute main! (Augmente) ")

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
