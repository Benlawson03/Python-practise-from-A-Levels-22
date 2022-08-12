#Days of Christmas problem
#Array
days = (('first', 'A Partridge in a Pear Tree'), ('second', 'Two Turtle Doves'), ('third', 'Three French Hens'), ('fourth', 'Four Calling Birds'), ('fifth', 'Five Golden Rings'), ('sixth', 'Six Geese a Laying'), ('seventh', 'Seven Swans a Swimming'), ('eighth', 'Eight Maids a Milking'), ('ninth', 'Nine Ladies Dancing'), ('tenth', 'Ten Lords a Leaping'), ('eleventh', 'Eleven Pipers Piping'), ('twelfth', '12 Drummers Drumming'))


for i in range(12):
  print("On the {} day of christmas, my true love gave to me, {}".format(days[i][0], days[i][1]))
  