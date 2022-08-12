def passcode(words):
  vowels = ("a","e","i","o","u")
  space = words.find(" ")
  word1 = words[:space]
  word2 = words[space + 1:]
  for index,item in enumerate(words):
   if item in vowels:
       print(index)

words = "Computer Science"
passcode(words)
