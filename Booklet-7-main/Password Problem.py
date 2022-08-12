import re
def validation():
  while True:
    password = input("Enter your password: ")
    if len(password) < 8:
      print("passowrd need to be at least 8 characters long")
    elif re.search ('[0-9', password) is None:
      print("make sure you have at least one number in the password")
    elif re.search ('[A-Z]', password) is None:
      print("make sure you have at least one upper case letter in your password")
    elif re.search ('[a-z]', password) is None:
      print("make sure you have at least one lower case letter in your password")
    else:
      print("your password is good")

validation()