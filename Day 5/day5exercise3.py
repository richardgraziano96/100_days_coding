even_numbers = 0

for numbers in range(2, 101, 2):
    if numbers % 2 == 0:
        even_numbers += numbers

print(even_numbers)