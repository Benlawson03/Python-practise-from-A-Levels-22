#States of water problem
#Subroutine to return state of water

def Parameters(SoW):
  if SoW > 100:
    return ("Gaseous")
  elif SoW > 1:
    return ("liquid")
  else:
    return ("Solid")
print (Parameters(37.2))