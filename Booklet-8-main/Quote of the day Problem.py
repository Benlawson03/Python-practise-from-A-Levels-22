#quote of the day problem
import random

#initialize data:
quote = [["" for x in range(2)] for y in range(3)]

quote[0][0] = "Any fool can write code that computers can understand. Good programmers write code that humans can understand."
quote[0][1] = "Martin Fowler"

quote[1][0] = "Code is like humour. When you have to explain it, it's bad."
quote[1][1] = "Cory House"

quote[2][0] = "Simplicity is the soul of efficiency."
quote[2][1] = "Austin Freeman"

#function to output a random quote:
def ran_quote():
  index = random.randint(0,2)
  return quote[index][0], quote[index][1]

#main program:
quote, author = ran_quote()
print("{} - {}".format(quote, author))
  