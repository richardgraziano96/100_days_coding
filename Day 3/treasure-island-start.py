print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# direction = input("Which way would you like to turn? Left or Right? \n").lower()

while True:
    direction = input("Please choose LEFT or RIGHT \n").lower()
    if direction != "left" or "right":
        direction = input("Please enter LEFT or RIGHT \n").lower()
    else:
        break

if direction == "right":
    print("Game over.")
    exit()
else:
    print("You traverse down a long hallway until...")
    print("You find yourself before a pool of water. \n")

while True:
    choice = input("Do you swim, or wait? \n").lower()
    if choice != "swim" or "wait":
        print("Please enter SWIM or WAIT.")
    else:
        break

if choice == "swim":
    print("You choose to swim and ultimately get swept away by the current.")
    print("Game over.")
    exit()
else:
    print("You decide to wait it out, the water rushes away from the island and...")
    print("You find yourself between three doors. Blue, Yellow and Red. \n")

door = input("Which door do you choose to go through? \n").lower()

while True:
    door = input("Please enter BLUE, RED or YELLOW \n").lower()
    if door != "blue" or "red" or "yellow":
        print("Please enter BLUE, RED or YELLOW")
    else:
        break

if door == "blue":
    print("You win!")
else:
    print("Game over.")
    exit()