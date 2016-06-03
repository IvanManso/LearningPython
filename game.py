import random

comGuess = random.randint(0, 100)

while True:
	#Int to transform the string to int and compare int values
	userGuess = int(input("Guess a number between 0-100: "))
	if userGuess < 0:
		print("Enter a number higher than 0")
	elif userGuess > 100:
		print("Enter a number lower than 100")
	elif userGuess > comGuess:
			print("Guess lower")
	elif userGuess < comGuess:
			print("Guess higher")
	else:
		print("Congrats, you've guessed the correct number")
		break
