#import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint

#[] => this is an array. an array is a special type of container that can hold multiple items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock","paper","scissors"]

#this is the player's choice
my_choice = input("Choose rock, paper or scissors: ")

#this will be the AI choice -> a random pick from the choices in the array
computer = choices[randint(0, 2)]

#check to see what the user input

#print outputs whatever is in the round brackets -> in this case it outputs my_choice to the command prompt window
print("user chose: " + my_choice)

#validate that the random choice worked for the AI
print("AI chose: " + computer)
