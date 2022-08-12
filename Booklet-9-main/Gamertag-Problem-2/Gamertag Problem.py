#gametag problem

def Gamertag_Creater():
  while True:
    email = input("Enter your email:  ")
    file = open("accounts.txt", "r")
    emails = file.read().split()[0::2]
    file.close()

    if email in emails:
      print("\nThis email is already in use.")
    else:
      break
  while True:
    username = input("Enter your username: ")
    file = open("accounts.txt", "r")
    usernames = file.read().split()[1::2]
    file.close()

    if username in usernames:
      print("This username is already in use.")
    else:
      break
  
  file = open("accounts.txt", "a")
  file.write(email + " " + username+"\n")

Gamertag_Creater()