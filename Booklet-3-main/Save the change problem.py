#Save the change problem
#Subroutine to calculate difference to nearest 1
def SaveTheChange(Amount):
  NearestPound = Amount
  NearestPound = int(Amount) + 1
  price = 1.20
  Savings = SaveTheChange(price)
  if int(Amount) != Amount:
    return NearestPound - Amount
  else:
    print("Debit - purchase: £{:.2f}".format(price))
    print("Debit - Save the change: £{:.2f}".format(Savings))
    print("Credit - Save the changes: £{:.2f}".format(Savings)) 