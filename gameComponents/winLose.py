from gameComponents import gameVars

# define a win or lose function
def winorlose(status):
	#print("inside winorlose function; status is: ", status)

	if status == "won":
		pre_message = "You have defeated me HUMAN! but I will learn for our next match. BEWARE!!! \n"
	else:
		pre_message = "I TOLD YOU HUMAN. I AM SUPERIOR!!!\n"

	print(pre_message + "Would you like to play again?")

	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":
		#reset the game and start over again
		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False
		
	elif choice == "N" or choice == "n":
		# exit message and quit
		print("awww... you don't wanna play anymore? Come on don't go, play with me!")
		exit()
	else:
		print("Make a valid choice - Y or N")
		print("we can stay here all day")
		#this will generate a bug that we will fix later
		choice = input("Y / N: ")
