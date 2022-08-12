#Temperature converter problem
#Main program
def Ctof(C):
  return(C * 1.8) + 32

def Ftoc(F):
  return (F / 1.8) - 32

C = 30
F = Ctof(C)

#Subroutine to convert Fahrenheit to Centigrade
print (C,"degrees C is",F,"degrees F")