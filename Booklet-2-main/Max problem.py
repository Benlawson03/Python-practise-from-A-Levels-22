#Max problem
#Subroutine to return the highest out of 2 number parameters
a = int(input())
b = int(input())
def Parameters():
  if a < b:
    return b
  else:
    return a
print(Parameters())