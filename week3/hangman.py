
import random

# A list of words that
potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)
# print(word)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()


# Make it a list of letters for someone to guess
# current_word = "_" * len(word)
current_word = list(word)
# print(current_word)
#
# # Some useful variables
#
guesses = [] #holds all previously guessed letters
maxfails = 7
fails = 0
#
while fails < maxfails:
	display = ""
	winning = ""
	for i in current_word:
		if i in guesses:
			display += i + " "
			winning += i
				# print(i)
		else:
			display += "_ "
				# print("_")
	print(display)
	if winning == word:
		print("You won!")
		exit(0)
	guess = input("Guess a letter: ").lower()

#check if it is a single letter and has not been previously guessed
	if guess.isalpha() and len(guess) == 1 and guess not in guesses:
		guesses.append(guess)
		print(guesses)
		if guess in current_word:
			print("You guessed a letter correctly.")
		else:
			fails += 1
			print("You guessed incorrectly.")
	else:
		print("Not valid input.")




	# print(current_word)


	print("You have " + str(maxfails - fails) + " tries left!")
	#display status of our word



print(f"You have lose, the word was {word}")
