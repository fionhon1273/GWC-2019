from random import *

aRandomNumber = randint(1, 20)

tries = 3

while tries > 0:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric():
        print("That's not a positive whole number, try again!")
    else:
        tries -= 1
        guess = int(guess)
    if (guess == aRandomNumber):
        print("Correct")
        break
    elif (guess > aRandomNumber):
        print("Guess lower")
    else:
        print("Guess higher")
print("Number of tries: (tries)")
