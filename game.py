#import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint

#[] => this is an array. an array is a special type of container that can hold multiple items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0



choices = ["rock","paper","scissors"]

player_lives = 5
ai_lives = 5

total_lives = 5

player = False # True and flase are booleans - date types can be true or false

# define a win or lose function
def winorlose(status):
	#print("inside winorlose function; status is: ", status)

	if status == "won":
		pre_message = "you are the yuuuuuuugest winner ever! "
	else:
		pre_message = "you done trumped it loser! "

	print(pre_message + "Would you like to play again?")

	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":

		global player_lives
		global ai_lives
		global player
		#reset the game and start over again
		player_lives = 5
		ai_lives = 5
		player = False

		elif choice =="N" or choice == "n":
			# exit message and quit
			print("you chose to quit! Better luck next time!")
			exit()
		else:
			print("Make a valid choice - Y or N")
			#this will generate a bug that we will fix later
			choice = input("Y / N: ")
	
# set up our game loop
while player is False:
	# this is the player choice
	print("================>/ RPS GAME /<================")
	print("Computer Lives:	", ai_lives, "/", total_lives)
	print("Player Lives:	", player_lives, "/", total_lives)
	print("==============================================")
	print("Choose your weapon! or type quit to exit\n")
	player = input("choose rock, paper or scissors: \n")

	# if the player chose to quit, then exit the game
	# just exit the process (kill python) and quit the game
	if player == "quit":
		print("you chose to quit")
		exit()

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
			player_lives -= 1
			print("you lose! player lives: ", player lives)
		else:
			print("you win!")
			ai_lives -= 1

	elif (computer == "paper"):
		if (player == "rock"):
			print("you lose! player lives: ", player lives)
			player_lives -= 1
		else:
			print("you win!")
			ai_lives -= 1


	elif (computer == "scissors"):
		if (player == "paper"):
			print("you lose! player lives: ", player lives)
			player_lives -= 1
		else:
			print("you win!")
			ai_lives -= 1

	# check player lives and ai lives
	if player_lives <= 0:
		winorlose("lost")

	elif ai_lives <= 0:
		winorlose("won")

	else:
		player = False
