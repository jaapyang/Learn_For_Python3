#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" this is a guess the number game
    test for contributions
"""
import random

secrectNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess:')
    guess = int(input())

    if guess < secrectNumber:
        print('Your guess is too low.')
    elif guess > secrectNumber:
        print('Your guess is too high.')
    else:
        break  # this condition is the correct guess!

if guess == secrectNumber:
    print('Good job! You guessed my number in %s guesses!' % guessesTaken)
else:
    print('Nope. The number I was thinking of was %s' % secrectNumber)
