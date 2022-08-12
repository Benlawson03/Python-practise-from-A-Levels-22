#Initial and Surname problem
#inputs
Forename = str(input())
Surname = str(input())
#turns the names to upper case
F1 = Forename.upper()
S1 = Surname.upper()
#gets only the first initial of the firstname
F1_l = F1[0:1]
print(F1_l, S1)