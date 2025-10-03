"""
2025-09-29
Ivan Zheryakov
Guessing the number
"""

import random

# Variables
number = random.randint(10, 11)
attempts = 0
"""
def END(exiting_game):
    return exiting_game 
"""

print("Guess the number I'm thinking of")
print("I've chosen a number between 10 and 100")
players_try = float(input("The number you're thinking of is : "))
if players_try != number:
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
# input("Press any key to start")
