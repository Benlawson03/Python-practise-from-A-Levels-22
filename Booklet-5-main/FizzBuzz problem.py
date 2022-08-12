# Fizz Buzz problem
def Multiple(X):
  for Counter in range(1,X+1):
    if Counter % 3 == 0 and Counter % 5 == 0:
        print("FizzBuzz")
    elif Counter % 3 == 0:
        print("Fizz")
    elif Counter % 5 == 0:
        print("Buzz")
    else:
        print(Counter)


# Main program
Multiple(100)
