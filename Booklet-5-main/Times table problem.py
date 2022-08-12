# Times table problem
# Subroutine to output the X times table
def TimesTable(X):
  for Counter in range(1,13):
    print("{} x {} = {}".format(Counter, X, Counter * X))

#Main program
TimesTable(6)