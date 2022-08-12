#subroutine to calculate the square root of a number using the Newton Method
def SqRoot(x):
  root=x
  print(root)
  while (root**2)!=x:
    root = 0.5*(root+(x/root))
    print(root)

#main program:
SqRoot(65)