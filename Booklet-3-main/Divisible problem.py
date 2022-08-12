#Divisible problem
a = float(input())
b = float(input())
def Parameters():
  if b == 0:
    return ("False")
  if a % b == 0:
    return ("True")
  else:
    return ("False")
print (Parameters())