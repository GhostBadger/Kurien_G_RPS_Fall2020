#import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint

#[] => this is an array. an array is a special type of container that can hold multiple items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock","paper","scissors"]

player_lives = 5
ai_lives = 5


#True and false are boolean data types -> they are the equivalent of on or off, 1 or 0
player = False

while player == False:

	#this is the player choice
	player = input("choose rock, paper or scissors: ")

	#this will be the AI choice -> a random pick from the choices in the array
	computer = choices[randint(0, 2)]

	#check to see what the user input

	#print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
	print("user chose: " + player)

	#validate that the random choice worked for the AI
	print("AI chose: " + computer)

	if (computer == player):
		print("tie")

	# always check for nagative conditions first (the losing case)
	elif (computer == "rock"):
		if (player == "scissors"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			ai_lives -= 1

	elif (computer == "paper"):
		if (player == "rock"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			ai_lives -= 1

	elif (computer == "scissors"):
		if (player == "paper"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			ai_lives -= 1

	print("player lives:", player_lives)
	print("ai lives:", ai_lives)
