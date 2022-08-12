from random import randint
#subroutine to play guess the number
def number():
  #generate random integers:
  n = 0
  players_guess = 0
  guess_count = 0
  n = randint(1,100)
  while players_guess != n:
    player_guess = int(input("Enter your guess: "))
    guess_count += 1
    if player_guess < n:
      print("Too Low!")
    elif player_guess > n:
      print("Too High!")
    else:
      print("Correct! I chose {}. It took you {} guesses.".format(n, guess_count))
    
#main program:
number()