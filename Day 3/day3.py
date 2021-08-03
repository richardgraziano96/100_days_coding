print("Welcome to the rollercoaster!")
## Asks for the user to input their height in cm
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
''' Throws a condition that if the user is not EQUAL TO or GREATER THAN 120 they cannot
ride this ride. '''
if height >= 120:
    print("You can ride this ride.")
    if age < 12:
        print("You must pay $5.")
    elif age <= 18:
        print("You must pay $7.")
    else:
        print("You must pay $12.")
else:
	print("You cannot ride this ride.")