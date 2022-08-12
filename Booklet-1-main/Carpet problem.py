#Carpet cost problem
width = int(input())
length = int(input())
carpet_size = int(input())
underlay = length * width * 3
room = length * width * carpet_size
grippers = (width * 2) + (length * 2)
fitting_fee = 50
print (room + underlay + grippers + fitting_fee)