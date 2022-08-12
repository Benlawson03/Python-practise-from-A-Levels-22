# Condition-controlled iterations
# Subroutine to use trial and error to calculate LCD
def LCD(Number1, Number2):
  Counter = 1
  while Counter % Number1 != 0 or Counter % Number2 != 0:
    Counter = Counter + 1
  return Counter

# Main program
Number1 = 20
Number2 = 7
Result = LCD(Number1, Number2)
print("The LCD of {} and {} is {}".format(Number1, Number2, Result))