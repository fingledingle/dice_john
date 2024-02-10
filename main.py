import random
from game_data import data


def changing_values(which_option, A, B):
  if which_option == "A":
    answer = A['follower_count']
  elif which_option == "B":
    answer = B['follower_count']
  return answer


def choose_value():
  random_number = random.randint(0, len(data) - 1)
  value = data[random_number]
  return value


def compare_followers():
  from replit import clear
  from art import logo
  from art import vs
  correct_answer = True
  points = 0
  A = choose_value()
  while correct_answer:
    

    print(f"{logo}")
    
    if correct_answer and points > 0:
      print(f"You're right! Current score: {points}")
      
    B = choose_value()
    print(
      f"Compare A: {A['name']}, a {A['description']}, from {A['country']} {A['follower_count']} "
    )
    print(f"{vs}")
    print(
      f"Against B: {B['name']}, a {B['description']}, from {B['country']} {B['follower_count']} "
    )

    which_option = input(
      "Who has more followers? Type 'A' or 'B': ").capitalize()

    answer = changing_values(which_option, A, B)
    clear()
    

    if answer == A['follower_count']:

      if A['follower_count'] > B['follower_count']:
        points += 1

      elif A['follower_count'] < B['follower_count']:
        print(f"{logo}")
        print("You got it wrong buddy, nice try tho!")
        break

    elif answer == B['follower_count']:

      if B['follower_count'] > A['follower_count']:
        points += 1
        A = B

      elif B['follower_count'] < A['follower_count']:
        print(f"{logo}")
        print("You got it wrong buddy, nice try tho!")
        break
  
      


compare_followers()
