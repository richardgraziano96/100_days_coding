print("Welcome to the rollercoaster!")
## Asks for the user to input their height in cm
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
''' Throws a condition that if the user is not EQUAL TO or GREATER THAN 120 they cannot
ride this ride. '''
cost = 0
if height >= 120:
    print("You can ride this ride.")
    if age < 12:
        cost = 5
        print(f"You must pay ${cost}")
    elif age <= 18:
        cost = 7
        print(f"You must pay ${cost}")
    elif age >= 45 and age <= 55:
        cost = 0
        print(f"You must pay ${cost}")
    else:
        cost = 12
        print(f"You must pay ${cost}")
    photos = input("Do you want photos? Please enter 'yes' or 'no' ").lower()
    if photos == "yes":
        cost = cost + 3
        print(f"Your total cost is ${cost}")
    else:
        print(f"Your total cost is ${cost}")
else:
	print("You cannot ride this ride.")