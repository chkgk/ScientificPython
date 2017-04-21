#Guess the number game: The computer thinks up a number between 0 and 1000. You have 10 chances to guess the number. 
# After every guess the computer tells you whether your guess was higher or lower than the number he thinks of.

import random

randomInt = random.randint(0,1000)

userGuess = ""

for i in range(10):
	print("This is your %i. trial!" % (i+1))
	userGuess = input("Which number do I have in mind? ")
	if userGuess.isnumeric():
		userGuess = int(userGuess)
		if userGuess > randomInt:
			print("That's too high! Try again!")
		elif userGuess < randomInt:
			print("Your guess is too low! Try again!")
		else:
			print("That's right! You win!")
			break

print("The game is over.")