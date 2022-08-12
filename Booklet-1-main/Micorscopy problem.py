#Microscopy problem
micrometres = int(input("Input micrometres: "))
cm = int(input("Input centimetres: "))

conversion = cm * 10000
magnification = conversion / micrometres
print ("Magnification =" , magnification)