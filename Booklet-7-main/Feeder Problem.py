# Feeder Problem
def feeder(meal, amount):
  if meal == "breakfast":
    print("Hopper," * amount)
  elif meal == "lunch":
    print("Hopper2," * amount)
  elif meal == "dinner":
    print(" Hopper1,\n Hopper2,\n" * amount)
feeder("dinner", 10)