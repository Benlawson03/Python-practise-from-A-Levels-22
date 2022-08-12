#Cookie Problem
def Preference(filename):
  text_file = open(filename,"r")
  Theme = text_file.readline()
  text_file.close()
  return Theme

def ChangePreference():
  change = input("Would you like to change your theme preference? Yes/No\n")
  if change.lower() == "yes":
    if Preference(filename) == "dark":
      WriteToFile("Theme Light Mode")
    else:
      WriteToFile("Theme Dark Mode")
  else:
    return

def WriteToFile(text):
  text_file = open(filename,"w")
  text_file.write(text)
  text_file.close()

#main program
global filename
filename = "Theme"
print("{}".format(Preference(filename)))
ChangePreference()