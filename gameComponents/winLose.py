from gameComponents import gameVars

# define a win or lose function
def winorlose(status):
	#print("inside winorlose function; status is: ", status)

	if status == "won":
		pre_message = "you are the yuuuuuuugest winner ever! \n"
	else:
		pre_message = "you done trumped it loser! "

	print(pre_message + "Would you like to play again?")

	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":
		#reset the game and start over again
		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False

	elif choice == "N" or choice == "n":
		# exit message and quit
		print("you chose to quit! Better luck next time!")
		exit()
	else:
			print("Make a valid choice - Y or N")
			#this will generate a bug that we will fix later
			choice = input("Y / N: ")
