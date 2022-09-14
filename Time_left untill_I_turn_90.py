# user's current age
age = input("What is your current age?\n")
# years left till user turn 90years
years_left = 90- int(age)
# days left
days_left = years_left * 365
# weeks left
weeks_left = years_left * 52
# months left
months_left = years_left * 12
# output
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")