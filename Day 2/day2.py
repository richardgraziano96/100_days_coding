##Takes user input and places it into a variable "num_char" for later use
num_char = len(input("What is your name? "))

##Recalls num_char to a string for it to be printed later
new_num_char = str(num_char)

##Prints how many letters are in your name (or whatever work you input)
print("Your name has " + new_num_char + " chars.")

###~~~~~~ Information under this line is commented out as they aren't needed. ~~~~~~
##Checks the variable type and prints it
#print(type(num_char))

##Assigns float to a number
#a = float(123)
##Prints the variable type
#print(type(a))

##Converts the string "100.5" to a float and adds it to the other int
#print(70 + float("100.5"))
##Literally prints the strings 70 and 100 as text
#print(str(70) + str(100))
