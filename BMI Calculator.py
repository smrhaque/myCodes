# initial variables need for calculation of BMI
print("Welcome to BMI Calculator!")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# calculating BMI
BMI = round((weight / (height ** 2)))
# variables to print
U = "underweight"
N = "normal weight"
SO = "slightly overweight"
O = "obese"
CO = "clinically obese"
# logic to determine BMI and giving an output
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are {U}.")
elif 18.5 < BMI < 25:
    print(f"Your BMI is {BMI}, you have a {N}.")
elif 25 < BMI < 30:
    print(f"Your BMI is {BMI}, you are {SO}.")
elif 30 < BMI < 35:
    print(f"Your BMI is {BMI}, you are {O}.")
else:
    print(f"Your BMI is {BMI}, you are {CO}.")
