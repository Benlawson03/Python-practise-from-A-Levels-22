#Inventory problem
inventory = str(input("Inventory: "))
def exists():
  if inventory == ("Shield"):
    return ("Shield")
  elif inventory == ("Potion"):
    return ("Potion")
  elif inventory == ("Charm"):
    return ("Charm")
  elif inventory == ("Bow"):
    return ("Bow")
  elif inventory == ("Sword"):
    return ("Sword")
  elif inventory == ("Amulet"):
    return ("Amulet")
  else:
    return("Nothing in Inventory")
print(exists())