#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

##Nice welcome message
print("Welcome to the tip calculator.\n")

##Start a loop until people follow the rules.
##must be a positive number NOT equal to 0
while True:
    total_bill = float(input("How much was the total bill? $"))
    if total_bill <= 0:
        print("Please enter a positive number not equal to 0.")
    else:
        break

##Must be a positive number NOT equal to 0
while True:
    total_people = int(input("How many people are splitting the bill? "))
    if total_people <= 0:
        print("Please enter a positive number not equal to 0.")
    else:
        break

##Must be a positive number OR 0
while True:
    tip_percent = int(input("What percent tip would you like to give? "))
    if tip_percent < 0:
        print("Please enter a positive number OR 0")
    else:
        break

##Calculate the way to split the bill equally according to the participants
final_payment = round((total_bill + (total_bill * (tip_percent / 100))) / total_people , 2)

##Print the final result
print(f"Each person must pay: ${final_payment}")
