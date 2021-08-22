## Bolds the string to make more emphasis
class color:
    BOLD = '\033[1m'
    END = '\033[0m'

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
while len(two_digit_number) > 2:
    print("Error. Only " + color.BOLD + "TWO" + color.END + " digits are allowed.")
    two_digit_number = input("Type a two digit number: ")
####################################
#Write your code below this line 👇

print(int(two_digit_number[0]) + int(two_digit_number[1]))
