import random 

limit = int(input("Choose the limit for our guessing game: "))
def guess(x):
  random_number = random.randint(1, x)
  guessed = 0
  while guessed != random_number:
    guessed = int(input(f"Guess a number between 1 and {x}: "))
    if guessed < random_number:
      print("You need a bigger number!")
    elif guessed > random_number:
      print("You need a smaller number")
    #else:
  print(f"Congrats!! You guessed the number {random_number} correctly ")

# guess(limit)        

def computer_guess(upper_limit):
  high = upper_limit
  low = 0
  user_info = ""
  while high != low and user_info != 'c':
    computer = int(random.randint(low, high))
    print(computer)
    user_info = input(f"Is the number {computer} lower (L), higher (H) or equal (C) than the number to guess: ").lower()
    if user_info == "l":
      low =computer+1
    else:
      high =computer-1
  print(f"The computer guessed the number {computer}" )

computer_guess(limit)


