#Name separator problem
def NameSeparator(FullName):
  #locating what separates the 2 names (space)
  space = FullName.find(" ")
  FirstName = FullName[:space]
  Surname = FullName[space + 1:]
  print(FirstName)
  print(Surname)
#FullName equals
FullName = "Ben Lawson"
NameSeparator(FullName)