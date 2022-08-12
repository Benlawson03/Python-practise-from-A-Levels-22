#ROT13 Problem

global alphabet
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#subroutine to run ROT13 Algorithm
def ROT13(input,output):

  file = open(input,"r")
  text_file = open(output,"w")
  text_file.write("")
  text_file.close()

  for text in file:
    for x in range(0,len(text),1):
      if text[x] == "":
        new_char = ""
      elif text[x].isupper() == True:
        char_pos = alphabet.index(text[x])
        new_char_pos = char_pos + 13
        if new_char_pos > 25:
          new_char_pos -= 26
        new_char = alphabet[new_char_pos]
      else: 
        new_char = text[x]
      text_file = open(output,"a")
      text_file.write(new_char)
      text_file.close()

  file.close()
  print("Text converted")
ROT13("input.txt","output.txt")