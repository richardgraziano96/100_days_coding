program_dictionary = {
    "Bug": "An error in a program that prevents the program from running", 
    "Function": "A piece of code that you can easily call over and over again", 
}

# print(program_dictionary["Bug"])

#TODO Adding new items to dictionary
program_dictionary["Loop"] = "The action of doing something over and over"

# print(program_dictionary)

empty_dictonary = {}

#TODO wipe an existing dictonary
# program_dictionary = {}

# print(program_dictionary)

#TODO edit item in a dictionary
# program_dictionary["Bug"] = "A insect inside a computer"
# print(program_dictionary)

#TODO loop through a dictionary
for key in program_dictionary:
    print(key)
    print(program_dictionary[key])