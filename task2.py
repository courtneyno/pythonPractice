"""
name: Courtney

Runs a find the number game
"""

import random

# number is chosen
answer = random.randint(1, 100)

while True:

    # number is guessed
    guess = input('Enter your number: ')
    guess = int(guess)

    # either correct or number is higher or lower
    is_correct = answer == guess

    # if number is correct game is finished: tell them they won, and exit
    if is_correct:
        print('you won')
        exit()

    # if number is wrong then say if higher or lower
    is_higher = answer < guess

    if is_higher:
        print('guess lower')

    else: 
        print('guess higher')
