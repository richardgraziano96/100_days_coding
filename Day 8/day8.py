# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Hello")
#     print("Thank you for watching")
#     print("Goodbye")
# greet()

# #Function that allows for input

# def greet_with_name(name):
#     print(f"Hello, {name}")
#     print(f"Thank you for watching, {name}")
#     print(f"Goodbye, {name}")

# greet_with_name("Ricky")

def greet_with(name, location):
    print(f"Hello {name}?")
    print(f"What is it like in {location}?")

user_name = input("What is your name? ")
user_location = input("What is your location? ")
greet_with(user_name, user_location)