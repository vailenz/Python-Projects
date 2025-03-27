# Hello, this is a BMI calculator

#we're taking the input from user
weight = float(input("Please enter your weight (kg): "))
height = float(input("Please enter your height (m): "))

#formula to get the bmi
bmi = weight / height ** 2

#now checking the bmi
if bmi < 18.5:
    print("You're underweight!")
elif 18.5 <= bmi <= 24.9:
    print("Your weight is normal!")
elif 25 <= bmi <= 29.9:
    print("You're overweight")
else:
    print("You're obese")