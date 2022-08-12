#energy bill calculator problem
pr = int(input())
cr = int(input())
cv = int(input())
u = cr - pr

kwh = (u * 1.022) * (cv / 3.6)
energy = kwh * 2.48
print(energy)
