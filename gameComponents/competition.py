from gameComponents import gameVars
# a function that finds out whether or not you won, lost or tied
def fight(player, computer):

	if (computer == player):
		print("\nIt seems we were thinking the same thing that time! But no matter, you will lose!\n")

	# always check for nagative conditions first (the losing case)
	elif (computer == "rock"):
		if (player == "scissors"):
			gameVars.player_lives -= 1
			print("\nHAH!! you lose this round!\n")
		else:
			print("\nFINE, you win this round!\n")
			gameVars.computer_lives -= 1

	elif (computer == "paper"):
		if (player == "rock"):
			print("\nHAH!! you lose this round!\n")
			gameVars.player_lives -= 1
		else:
			print("\nFINE, you win this round!\n")
			gameVars.computer_lives -= 1


	elif (computer == "scissors"):
		if (player == "paper"):
			print("\nHAH!! you lose this round!\n")
			gameVars.player_lives -= 1
		else:
			print("\nFINE, you win this round!\n")
			gameVars.computer_lives -= 1
