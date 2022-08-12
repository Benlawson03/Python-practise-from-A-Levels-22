# Compound interest problem
# Subroutine to output the interest growth on a balance
Year = 1
def Compound(Balance, InterestRate, TargetBalance):
  # Interate until the balance matches the target balance
    while Balance < TargetBalance:
      Interest = Balance * InterestRate
      Balance = Balance + Interest
    print("Year {}: New balance = £{:.2f}".format(Year, Balance))
# Main program
Year = Year + 1
Compound(100, 0.04, 200)