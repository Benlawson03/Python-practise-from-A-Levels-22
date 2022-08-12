def numToBinary(num):
  "This Function converts decimal number to binary and prints it"
  if num > 1:
        numToBinary(num // 2)
  print(num % 2, end='')

# decimal number
numToBinary(11)