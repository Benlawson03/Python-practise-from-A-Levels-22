# Conversion Utility Program
# Feet to meters
def Utility(unit, amount):
  if unit == "feet":
    amount1 = amount * 0.3048
    print("{} feet is {} meters".format(amount, amount1))
# Stone to kilograms
  elif unit == "stone":
    amount1 = amount * 6.35029
    print("{} stone is {} kilograms".format(amount, amount1))
# Meters to feet
  elif unit == "Meters":
    amount1 = amount * 3.281
    print("{} meters is {} feet".format(amount, amount1))
# Kilograms to stone
  elif unit == "kilograms":
    amount1 = amount * 6.35
    print("{} kilograms is {} stone".format(amount, amount1))

Utility("feet", 10000)