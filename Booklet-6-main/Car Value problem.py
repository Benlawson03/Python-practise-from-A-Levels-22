#subroutine to calculate the depreciation in the value of a car
def depreciation(year, value, min_resale):
  print("Starting value = £{:.2f}".format(value))
  year=1
  value = value*0.7
  print("Year {}: value = £{:.2f}".format(year, value))
  year = year+1
  while value>= min_resale:
    value = value*0.8
    print("Year {}: value = £{:.2f}".format(year, value))
    year = year+1
  

#main program:
depreciation(2020, 10000, 2000)