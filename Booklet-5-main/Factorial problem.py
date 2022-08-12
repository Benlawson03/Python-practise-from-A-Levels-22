# Factorial problem
# Subroutine to output the X times table
def Fact(X):
	fact1 = 1
	for Counter in range(1,X+1):
		fact1 = fact1 * Counter
	return fact1
# Main program
X = int(input("Enter a number: "))
fact1 = Fact(X)
print("Factorial of ", X,'! = ',fact1,sep="")