# Handle user inputs

# Function to return an input
def GetInput():
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    Choice = input("Enter an option number:")
    return Choice

# Main program
Choice = GetInput()
print("You choose option {}".format(Choice))