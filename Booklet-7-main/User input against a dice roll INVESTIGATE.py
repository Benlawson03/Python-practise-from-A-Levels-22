# Handle user inputs
import random

# Function to return an input
def GetInput():
    print("What do you thiink the dice roll will be?")
    ValidChoice = False
    while not ValidChoice:
      Choice = input("Enter a guess between 1 and 6: ")
      if Choice.isnumeric():
              ValidChoice = True
      if not ValidChoice:
        print("Invalid choice.")
    return Choice

# Main program
random.seed()
Roll