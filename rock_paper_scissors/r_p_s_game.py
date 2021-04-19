import random
user_choice=input("Choose between r for rock, p for paper or s for scissors: ")
computer_choice = random.choice(['s', 'r', 'p'])
print(f"Computer's choice is:{computer_choice}")

def game():
  if user_choice == computer_choice:
    return 'Tie'
  elif you_win():
    return 'You win'
  return 'You lost'

def you_win():
  if(user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
    return True

print(game())
    