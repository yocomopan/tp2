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
    print("Le nombre que j'ai choisi est entre 10 et 30")
    while guessing:
        players_try = int(input("Quel nombre tu penses que j'ai en tête?  "))

        if players_try > number:
            print("Tu devrais sous-estimer mon pouvoir! ")

        elif players_try < number:
            print("C'est fini Anakin, j'ai la haute main! ")

        else:
            guessing = True
            print("Bravo, je vous applaudis")
            decisions = str(input("Voulez-vous rejouer? y/n "))
            if decisions == "n":
                guessing = False

            else:
                pass
    # Demander au joueur s'il veut jouer encore.
    # Si non, play_game = False
"""
# print(f"To make it more challenging, guess it in {attempts_required}")


if 30 < players_try < 10:
    print("Between 10 and 30")
    attempts += 1

elif players_try != number:
    attempts += 1
    print("Nope! Try again.")

    while number != players_try:
        attempts += 1
        players_try = float(input("The number you're thinking of is : "))
        if players_try == number:
            print("Nice Work!")
            print(f"You did it in {attempts} attempts.")
        else:
            print("Nope!")

else:
    print("Nice work!")
    print(f"You did it in {attempts} attempts.")


# input(int("Type 1234 to end"))
# deciding_to_end = input(int("Type 1234 to end"))
# END(deciding_to_end)
# difficulty = input("choose your difficulty, easy medium hard")
"""
