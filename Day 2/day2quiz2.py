# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = (float(weight) / float(height) ** 2)

if bmi <= 18.4 :
    print("You are underweight.\n")
elif 18.5 <= bmi <= 24.9 :
    print("You are a normal weight.\n")
elif 25.0 <= bmi <= 29.9 :
    print("You are overweight.\n")
elif bmi > 30.0 :
    print("You are obese.\n")

bmi = int(bmi)

print("Your BMI is: " + str(bmi))