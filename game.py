#import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint

# re-import our game variables
from gameComponents import gameVars, competition, winLose
	
# set up our game loop
while gameVars.player is False:
	# this is the player choice
	print("================>/ RPS GAME /<================")
	print("Computer Lives:	", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:	", gameVars.player_lives, "/", gameVars.total_lives)
	print("==============================================")
	print("Choose your weapon! or type quit to exit\n")
	gameVars.player = input("choose rock, paper or scissors: \n")

	# if the gameVars.player chose to quit, then exit the game
	# just exit the process (kill python) and quit the game
	if gameVars.player == "quit":
		print("you chose to quit")
		exit()

	#this will be the AI choice -> a random pick from the choices in the array
	computer = gameVars.choices[randint(0, 2)]

	#check to see what the user input

	#print outputs whatever is in the round brackets -> in this case it outputs gameVars.player to the command prompt window
	print("user chose: " + gameVars.player)

	#validate that the random choice worked for the AI
	print("AI chose: " + computer)

	#this was where the code is taken from
	competition.fight(gameVars.player, computer)



	# check player lives and ai lives
	if gameVars.player_lives <= 0:
		winLose.winorlose("lost")

	elif gameVars.computer_lives <= 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False
