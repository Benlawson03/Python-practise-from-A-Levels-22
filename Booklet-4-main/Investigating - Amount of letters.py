#String data types

#Subroutine to count characters
def ShowLen(Surname):
  StringLength = len(Surname)
  print("There are {} letters in your surname, {}.".format(StringLength,Surname))

# Main program
Surname = "Lawson"
ShowLen(Surname)