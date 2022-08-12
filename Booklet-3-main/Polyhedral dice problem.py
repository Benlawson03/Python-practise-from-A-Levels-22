#Polyhedral dice problem
#Number data types
import random

a = int(input())
#Subroutine to generate a random number
def RollDice():
  return random.randint(1,a)

#Main program
random.seed()
Dice = RollDice()
print("Rolled a {}".format(Dice))