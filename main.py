"""
2025-09-29
Ivan Zheryakov
Guessing the number
"""

import random

# Variables
number = random.randint(10, 100)

"""
def END(exiting_game):
    return exiting_game 
"""

print("Guess the number I'm thinking of")
print("I've chosen a number between 10 and 100")
players_try = float(input("The number you're thinking of is : "))
if players_try != number:
    print("Nope! Try again.")
    while number != players_try:
        players_try = float(input("The number you're thinking of is : "))
        if players_try == number:
            print("Nice Work!")
        else:
            print("Nope!")
else:
    print("Nice work!")
# input(int("Type 1234 to end"))
# deciding_to_end = input(int("Type 1234 to end"))
# END(deciding_to_end)
# difficulty = input("choose your difficulty, easy medium hard")
# input("Press any key to start")
