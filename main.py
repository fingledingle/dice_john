import random
from game_data import data


def changing_values(which_option):
  if which_option == "A":
    answer = A['follower_count']
  elif which_option == "B":
    answer = B['follower_count']
  return answer


def choose_value():
  random_number = random.randint(0, len(data) - 1)
  value = data[random_number]
  return value

# A = choose_value()
# print(A)
# B = choose_value()
# print(B)

points = 0
correct_answer = True
while correct_answer == True:
  A = choose_value()
  B = choose_value()
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")

  which_option = input(
    "Which one of them has the highest number of followers? A or B"
  ).capitalize()

  answer = changing_values(which_option)
  
  if answer == A['follower_count']:
    if A['follower_count'] > B['follower_count']:
      points += 1
    elif A['follower_count'] < B['follower_count']:
      print("You lost")
      correct_answer == False
  elif answer == B['follower_count']:
    if B['follower_count'] > A['follower_count']:
      points += 1
    elif B['follower_count'] < A['follower_count']:
      print("You lost")
      correct_answer == False
