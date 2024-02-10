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

# A = choose_value()
# print(A)
# B = choose_value()
# print(B)


#Firrst attempt


def compare_followers():
  from art import logo
  from art import vs 
  correct_answer = True
  points = 0
  A = choose_value()
  while correct_answer:

    print (f"{logo}")
    B = choose_value()
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} {A['follower_count']} ")
    print (f"{vs}")
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']} {B['follower_count']} ")

    which_option = input(
      "Who has more followers? Type 'A' or 'B': "
    ).capitalize()

    answer = changing_values(which_option, A, B)

    if answer == A['follower_count']:

      if A['follower_count'] > B['follower_count']:
        points += 1
        A = A

      elif A['follower_count'] < B['follower_count']:
        print("You got it wrong buddy, nice try tho!")
        correct_answer = False
        break

    elif answer == B['follower_count']:

      if B['follower_count'] > A['follower_count']:
        points += 1
        A = B

      elif B['follower_count'] < A['follower_count']:
        print("You got it wrong buddy, nice try tho!")
        correct_answer = False
        break

    if correct_answer and points > 0:
      print(f"You're right! Current score: {points}")


compare_followers()







# game(changing_values, choose_value




# def john_continuation (A, points):
#   B = choose_value()
#   print(f"{points}")
#   print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} {A['follower_count']} ")
#   print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']} {B['follower_count']} ")

#   which_option = input(
#     "Which one of them has the highest number of followers? A or B \n"
#   ).capitalize()

#   answer = changing_values(which_option, A, B)

#   if answer == A['follower_count']:

#     if A['follower_count'] > B['follower_count']:
#       points += 1

#     elif A['follower_count'] < B['follower_count']:
#       print("You got it wrong buddy, nice try tho!")
#       john = False
      


#   elif answer == B['follower_count']:

#     if B['follower_count'] > A['follower_count']:
#       points += 1
#       A = B

#     elif B['follower_count'] < A['follower_count']:
#       print("You got it wrong buddy, nice try tho!")
#       john = False
      
      




# john = False
# points = 0
# A = choose_value()
# B = choose_value()
# print(f"{points}")
# print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} {A['follower_count']} ")
# print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']} {B['follower_count']} ")

# which_option = input(
#   "Which one of them has the highest number of followers? A or B \n"
# ).capitalize()

# answer = changing_values(which_option, A, B)

# if answer == A['follower_count']:

#   if A['follower_count'] > B['follower_count']:
#     john = True
#     points += 1
#     A = A

#   elif A['follower_count'] < B['follower_count']:
#     print("You got it wrong buddy, nice try tho!")
#     john = False
#     correct_answer = False


# elif answer == B['follower_count']:

#   if B['follower_count'] > A['follower_count']:
#     john = True
#     points += 1
#     A = B

#   elif B['follower_count'] < A['follower_count']:
#     print("You got it wrong buddy, nice try tho!")
#     john = False
#     correct_answer = False


# while john == True:
#   print(f"You're right! Current score: {points}")
#   john_continuation(A, points)


# import random
# from game_data import data

# def changing_values(which_option, A, B):
#     if which_option == "A":
#         return A['follower_count']
#     elif which_option == "B":
#         return B['follower_count']

# def choose_value():
#     random_number = random.randint(0, len(data) - 1)
#     value = data[random_number]
#     return value

# def compare_followers():
#     points = 0
#     while True:  # Infinite loop until user decides to quit
#         A = choose_value()
#         B = choose_value()
#         print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} {A['follower_count']} ")
#         print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']} {B['follower_count']} ")

#         which_option = input("Which one of them has the highest number of followers? A or B \n").capitalize()

#         answer = changing_values(which_option, A, B)

#         if answer == A['follower_count']:
#             if A['follower_count'] > B['follower_count']:
#                 points += 1
#                 print("You got it right! Nice one!")
#             else:
#                 print("You got it wrong buddy, nice try tho!")
#                 break  # End the game if the answer is wrong
#         elif answer == B['follower_count']:
#             if B['follower_count'] > A['follower_count']:
#                 points += 1
#                 print("You got it right! Nice one!")
#             else:
#                 print("You got it wrong buddy, nice try tho!")
#                 break  # End the game if the answer is wrong

#         print(f"You're right! Current score: {points}")

# compare_followers()

















