### Scope ###

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies inside function: {enemies}")

## Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

## Global Scope

# player_heatlh = 10


# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_heatlh)

#     drink_potion()

# print(player_heatlh)

## Block Scope

# game_level = 3
# def create_enemy():
#     enemies = ["Zombie", "Skeleton", "Vampire"]

#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

# create_enemy()

#NOTE you can use Global to make a variable/constant GLOBAL but its not advised as
# there could be an instance where you used it somewhere else in your code
## Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@rickygraziano"