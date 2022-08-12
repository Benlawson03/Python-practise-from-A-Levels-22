from random import randint
#Subroutine to simulate a lottery involving three random numbers
def lottery(A, B, C):
  Week = 1
  ballA = randint(1,30)
  ballB = randint(1,30)
  ballC = randint(1,30)
  while (A!=ballA or B!=ballB or C!=ballC):
    ballA = randint(1,30)
    ballB = randint(1,30)
    ballC = randint(1,30)
    print("Week {}: The player chose {}, {} and {}. The correct numbers were {}, {} and {}!\n".format(Week, A, B, C, ballA, ballB, ballC))
    Week = Week + 1
  print("Week {}: The player chose {}, {} and {}. All their choices were correct!\n".format(Week, A, B, C))
# Main program
lottery(1,13,14)
