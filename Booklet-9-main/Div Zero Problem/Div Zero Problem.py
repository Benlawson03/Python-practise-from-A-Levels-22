# Div zero problem
def div(n1, n2):
  try:
    result = n1/n2
    return result
  except:
    return("E")

print(div(12, 3))