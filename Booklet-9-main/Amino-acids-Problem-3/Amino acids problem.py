#amino acids problem
def print_data():
  file_name = "dna.txt"
  text_file = open(file_name, "r")
  global data
  data = " "
  while(data):
    data = text_file.readline()
    if data: 
      print("\n"+data)
      return(data)
  text_file.close()

sequence = str(input("Enter the amino acid sequence you would like to search for: ""\n"))
sequence = sequence.upper()
print_data()
count=0
i=0
for i in range((len(data))-2):
  current_3 = data[i:i+3]
  i+=1
  if current_3[0] == sequence[0] and current_3[1] == sequence[1] and current_3[2] == sequence[2]:
    count+=1
  else:
    count=count

print("\n"+"Your sequence {} appeared {} times in the sequence above: \n".format(sequence, count))