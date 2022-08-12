#Driving  test problem
#Subroutine to output pass or fail for driving test
def PassFail(MinorFaults):
  if MinorFaults < 16:
    return "pass"
  else:
    return ("fail")
print(PassFail(16))
