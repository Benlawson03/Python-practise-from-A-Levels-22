inventory = ["shield","sword","mana booster","bow","arrow"]

# Subroutine to print inventory
def search():
  print(inventory)

def choice():
  choice = int(input("Would you like to Drop an item(1), Pick up an item(2), Hold an item(3) or Hold all current items(4) ? "))
  return(choice)

# Subroutine for dropping an item
def drop():
  print("Your inventory is currently: ")
  print(inventory)
  Drop = (input("Which item would you like to drop? "))
  inventory.remove(Drop)
  print(inventory)

# Subroutine for picking up an item
def pick():
  pick = input("Which item would you like to add to your inventory? ")
  inventory.append(pick)
  print("Your inventory is now: ")
  print(inventory)
  inventory.append(pick)
  print(inventory)

# Subroutine for Outputing an item
def pull():
  Pull = input("Which slot would you like to view? ")
  print(inventory[Pull-1])
  print(inventory)

def search():
  print(inventory)

action = choice()
if action == 1:
  drop()
elif action == 2:
  pick()
elif action == 3:
  pull()
elif action == 4:
  search()
