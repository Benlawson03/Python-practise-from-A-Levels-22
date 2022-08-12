#Teacher code problem
def initials(fn, mn, ln):
  #if middle name exists then returns code as fn,mn and ln
  if mn is not None:
    code = (fn[0]+ mn[0]+ ln[0])
    code = code.upper()
  else:
    #if middle name doesnt exist then returns code as fn,Z and ln
    code = (fn[0]+ "Z"+ ln[0])

  
  return (code)
#fn, mn, ln equals = 
fn = "John"
mn = None  
ln = "Smith"
print (initials(fn, mn, ln))