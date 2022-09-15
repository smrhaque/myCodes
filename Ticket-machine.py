# initial variables & greetings
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# conditions for ticket is height which must be greater than or equal to 120cm
if height >= 120:
    print("You can ride the rollercoaster!")
    # determining age for ticket price and setting the new bill
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    # determining if wants a photo taken
    wants_photo = input("Do you want a photo taken? Y or N. ").lower()
    if wants_photo == "y":
        bill += 3
    # printing final bill
    print(f"Your final bill is ${bill}")

# Apologize for not meeting minimum requirements.
else:
    print("Sorry, you have to grow taller before you can ride.")
