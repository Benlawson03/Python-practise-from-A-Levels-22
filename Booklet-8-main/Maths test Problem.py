# Maths test problem
from random import randint
# Subroutine for maths test
def maths_test(questions):
  while True:
    test = [["" for y in range(3)] for x in range(questions)]

    for i in range(0,5):
      answer = randint(20,99)
      num1 = answer-randint(10,answer-10)
      num2 = answer-num1
      test[i][0] = num1
      test[i][1] = num2
      test[i][2] = answer

    total = 0
    test_active = True
    test_scores = []
    while test_active == True:
      total = 0
      student_name = input("Please enter your name: ")
      for x in range (0,questions):
        print("What is {} + {}".format(test[x][0],test[x][1]))
        while True:
          try:
            user_answer = input("")
            user_answer = int(user_answer)
            break
          except ValueError:
            print("Please enter an integer.")
        if user_answer == test[x][2]:
          print("Correct!")
          total += 1
        else:
          print("Incorrect")
      print("You scored {} out of {}\n".format(total, questions))

maths_test(5)