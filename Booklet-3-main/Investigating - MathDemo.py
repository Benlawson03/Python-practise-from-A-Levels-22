# Number data types
import random

# Subroutine to demonstrate casting and operators
def MathsDemo(X, Y):
    DivisionResult = X / Y
    print("{} divided by {} is {}".format(X, Y, DivisionResult))
    IntDivisionResult = X // Y
    print ("{} integer division by {} is {}".format(X, Y, IntDivisionResult))
    Modresult = X % Y
    print("{} modulus {} is {}".format(X, Y, Modresult))
    ExpResult = X ** Y
    print("{} to the power of {} is {}".format(X, Y, ExpResult))

#Main program
MathsDemo(10,7)