"""
name: Courtney

Runs a find the number game
"""

import random


answer = random.randint(1, 100)

while True:
    guess = input('Enter your number: ')
    guess = int(guess)

    is_correct = answer == guess

    if is_correct:
        print('you won')
        exit()

    is_higher = answer < guess

    if is_higher:
        print('guess lower')
    else: 
        print('guess higher')
