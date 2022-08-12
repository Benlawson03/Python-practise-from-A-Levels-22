# Pin Problem
Pin = 1234
Input = 0
attempts = 0

while Input != Pin:
  if attempts < 3:
    Input = int(input("Enter your Pin: "))
    if Input == Pin:
      print("Correct Pin entered")
      break
    else:
      print("Incorrect Pin")
      attempts += 1
  else:
    print("You have exceeded the amount of attempts allowed.")
    print("Your account has been successfully locked.")
    break