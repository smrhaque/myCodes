# Greeting
print("welcome to the Tip-Calculator!")
# Total Bill for the party
bill = float(input("Please enter the total bill for the party: $"))
# Tip percentage
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
# number of people in the party
number_of_people = float(input("How many people to split the bill? "))
# ammount each person have to pay
ammount_for_each_person = round((bill*((100+tip_percentage)/100)/number_of_people),2)
print(f"Each person should pay: ${ammount_for_each_person}")