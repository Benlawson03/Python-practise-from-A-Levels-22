# Attributes Problem
def attributes(name, attack, defence):
  file_name = "attributes"
  text = open(file_name, "a")
  text.write(name+" ")
  text.write(attack+" ")
  text.write(defence+"\n")
  text.close()

def user_input():
  global name
  name = str(input("Whats your characters name? "))
  global defence
  global attack
  attack = 1000
  defence = 1000
  while attack > 100 or attack < 0:
    attack = int(input("Enter your character's attack capability (0 - 100)? "))
  while defence > 100 or defence < 0:
    defence = int(input("Enter your character's defence capability (0 - 100)? "))
  attack = str(attack)
  defence = str(defence)

user_input()
attributes(name, attack, defence)