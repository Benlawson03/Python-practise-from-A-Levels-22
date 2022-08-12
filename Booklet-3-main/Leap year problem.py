#Leap year problem
year = int(input())
def Parameter():
  if year % 4 == 0:
    return ("True")
  elif year % 100 == 0:
    return ("false")
  elif year % 400 == 0:
    return ("True")
  else:
    return ("False")
print(Parameter())