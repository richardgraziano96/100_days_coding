# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

'''If your number is even like 8 you get 2 + 2 + 2 + 2 with NO remainder.
while if you have a number like 9 you get 2 + 2 + 2 + 2 + 1 which gives you a 1 as 
remainder. Thus we can see that 0 is even and 1 is odd. '''
if number % 2 == 0:
    print("Your number is EVEN.")
else:
    print("Your number is ODD.")