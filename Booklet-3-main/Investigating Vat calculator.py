#Vat calculator
#Number data types

#Subroutine to calculate VAT
def Vat(Totatl):
  return Total * 0.05

#Main program
Total = 100.12
ValueAddedTax = Vat(Total)
ToPay = Total + ValueAddedTax
print("Total £{:.2f} VAT £{:.2f} To pay £{:.2f}".format(Total, ValueAddedTax, ToPay))




#Number data types

#Subroutine to calculate VAT
def Vat(Totatl):
  return Total * 0.2

#Main program
Total = 99.99
ValueAddedTax = Vat(Total)
ToPay = Total + ValueAddedTax
print("Total £{:.2f} VAT £{:.2f} To pay £{:.2f}".format(Total, ValueAddedTax, ToPay))




#Number data types

#Subroutine to calculate VAT
def Vat(Totatl):
  return Total * 0.2
def Vat(rate):
  if Vat > (0.2):
    return ("Standard")
  elif rate > (0.05):
    return ("Reduced")
  else:
    return ("Zero")

#Main program
Total = 99.99
ValueAddedTax = Vat(Total)
ToPay = Total + ValueAddedTax
print("Total £{:.2f} VAT £{:.2f} To pay £{:.2f}".format(Total, ValueAddedTax, ToPay))