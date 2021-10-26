############DEBUGGING#####################

# # Describe Problem
# def my_function():
# for i in range(1, 20):
# for i in range(1, 21):
#     if i == 20:
#         print("You got it")


# my_function()
# NOTE it actually STOPS at 20 so it doesn't get to 20

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# # dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# NOTE counting starts at 0

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
# NOTE make sure that there aren't gaps. If nobody gets 1994 it will never be called

# # Fix the Errors
# # age = input("How old are you?")
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")
# NOTE you need f to format a string as well as int before input if you're asking
# for an int from the user

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# NOTE == will return 0 as it is now "true" instead of a number (boolean)

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])
# NOTE make sure to check and make sure things are indented and where you need
# them
