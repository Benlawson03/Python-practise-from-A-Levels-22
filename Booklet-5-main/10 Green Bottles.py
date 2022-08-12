def Song(X):
  for Counter in range(X,0,-1):
    print("{} green bottles hanging on the wall,\n{} green bottles hanging on the wall,".format(Counter,Counter))
    print("And if one green bottle should accidently fall,\nThere'll be {} green bottles hanging on the wall.".format(Counter-1))
# Main program
Song(10)