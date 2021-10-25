# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#Sets our variables to  0
student_count = total_height = average_height = 0

# For loop to count how many students we have
for height in student_heights:
    student_count += 1

# For loop to add ALL the heights
for student in range(student_count):
    total_height += student_heights[student]

# Calculate the average
average_height = total_height / student_count

#Round the average height
whole_height = round(average_height)

#Prints results
print("The total number of the student is: " , student_count
, "\n The total height of the whole class is: " , total_height
, "\n The average height of the student is: " , whole_height)
