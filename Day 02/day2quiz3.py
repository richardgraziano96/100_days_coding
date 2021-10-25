# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

## Calculates the new age minus the max age
new_age = 90 - int(age)

## The math between months, weeks and days
months = new_age * 12
weeks = new_age * 52
days = new_age * 365

## prints everything out using an F string
print(f"You have {days} days, {weeks} weeks, and {months} months left to live.")