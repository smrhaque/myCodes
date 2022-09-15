# initial variables need for calculation of BMI
print("Welcome to Leap year finder!")
year = int(input("Which year do you want to check? "))
# setting starter value for leap year
leap_year = 0
not_leap_year = 0
# conditions for leap_year
if year % 4 == 0:
  leap_year += 1
  if year % 100 ==0:
    not_leap_year += 1
  else:
    leap_year +=1
if year % 400 ==0:
  leap_year += 1
else:
  not_leap_year +=1
# printing output
if leap_year>not_leap_year:
  print("Leap year.")
else:
  print("Not leap year.")