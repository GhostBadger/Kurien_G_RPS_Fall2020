#import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint

# re-import our game variables
from gameComponents import gameVars, competition, winLose
	

want_to_play = randint(0, 10)
	


# Rules to play by
if want_to_play <= 8:
	print("It seems that you would like to challenge me, THE ALMIGHTY COMPUTER to a game of chance.")
	print("Very well, I accept.")
	print("Here are the rules!")
	print("Rock loses to Paper, wins to Scissors")
	print("Paper loses to Scissors, wins to Rock")
	print("Scissors loses to Rock, wins to Paper")
	print("And should we both choose the same option we duel again")
	print("To make it interesting we will each have 5 lives.")
	print("The Person who loses has to give georgey 5 percent extra marks for this assignment")
	print("Alright, Lets begin\n")

	#The main game loop
	while gameVars.player is False:

		# this is the player choice
		print("================>/ RPS GAME /<================")
		print("Computer Lives:	", gameVars.computer_lives, "/", gameVars.total_lives)
		print("Player Lives:	", gameVars.player_lives, "/", gameVars.total_lives)
		print("==============================================")
		print("\nChoose your weapon! or type quit to exit\n")
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
		print("\n+~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
		print("user chose: " + gameVars.player)

		#validate that the random choice worked for the AI
		print("AI chose: " + computer)
		print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")

		#this was where the code is taken from
		competition.fight(gameVars.player, computer)



		# check player lives and ai lives
		if gameVars.player_lives <= 0:
			winLose.winorlose("lost")

		elif gameVars.computer_lives <= 0:
			winLose.winorlose("won")

		else:
			gameVars.player = False

else:
	print("I have other things to do human. I may indulge you at another time.")
