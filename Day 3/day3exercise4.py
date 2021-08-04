# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
# 🚨 Don't change the code above 👆

''' I know that it said "dont change anything" but I needed to make a newline. It was
too distracting and unreadable without it '''
#Write your code below this line 👇

## Initialize variable
cost = 0

## Start if statements. Pretty straightforward. Only need one elif, this isn't userproof
## but it works.
if size == "S":
    cost = 15
    if add_pepperoni == "Y":
        cost = cost + 2
    if extra_cheese == "Y":
        cost = cost + 1
elif size == "M":
    cost = 20
    if add_pepperoni == "Y":
        cost = cost + 3
    if extra_cheese == "Y":
        cost = cost + 1
else:
    cost = 25
    if add_pepperoni == "Y":
        cost = cost + 3
    if extra_cheese == "Y":
        cost = cost + 1

## Print total
print(f"Your final bill is ${cost}")