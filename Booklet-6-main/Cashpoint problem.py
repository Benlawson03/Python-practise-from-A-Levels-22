def cashpoint(amount):
  while amount >= 20:
    print("Dispense 20")
    amount = amount - 20

  if amount >= 10:
    print("Dispense 10")
    amount = amount - 10

  if amount >= 5:
    print("Dispenes 5")
    amount = amount - 5
cashpoint(110)