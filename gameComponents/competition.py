from gameComponents import gameVars
# a function that finds out whether or not you won, lost or tied
def fight(player, computer):

	if (computer == player):
		print("tie")

	# always check for nagative conditions first (the losing case)
	elif (computer == "rock"):
		if (player == "scissors"):
			gameVars.player_lives -= 1
			print("you lose! player lives: ", gameVars.player_lives)
		else:
			print("you win!")
			gameVars.computer_lives -= 1

	elif (computer == "paper"):
		if (player == "rock"):
			print("you lose! player lives: ", gameVars.player_lives)
			gameVars.player_lives -= 1
		else:
			print("you win!")
			gameVars.computer_lives -= 1


	elif (computer == "scissors"):
		if (player == "paper"):
			print("you lose! player lives: ", gameVars.player_lives)
			gameVars.player_lives -= 1
		else:
			print("you win!")
			gameVars.computer_lives -= 1