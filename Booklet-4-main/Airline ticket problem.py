#Airline ticket problem
city_1 = str(input("Enter a city: "))
city_2 = str(input("Enter another city: "))
#making the city names in upper case
CITY_1 = city_1.upper()
CITY_2 = city_2.upper()
#making the city names only the first letter
c_1 = CITY_1[0:4]
c_2 = CITY_2[0:4]
print(c_1 + "-" + c_2)