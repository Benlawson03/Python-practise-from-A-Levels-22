while True!=False:
  notebook=["Example Note"]
  while len(notebook)<10:
    choice = input("Would you like to show your list of notes, add or delete a note? (show/add/delete) ")
    if choice == "add":
      note = str(input("Enter a note you'd like to add: "))
      notebook.append(note)
    elif choice == "show":
      print(notebook)
    else:
      print(notebook)
      delete_choice = int(input("Enter a number for a note you'd like to delete: "))
      notebook.pop(delete_choice-1)
  print("You've reached the maximum number of notes (10).")
  print(notebook)
  delete_choice = int(input("Enter a number for the note you'd like to delete: "))
  notebook.pop(delete_choice-1)