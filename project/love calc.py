# Greetings and init variables
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# combing names to a string and making them lowercase so its easier to count
name_combined = (name1 + name2).strip()
name_combined_lower = name_combined.lower()
# counting
t = name_combined_lower.count("t")
r = name_combined_lower.count("r")
u = name_combined_lower.count("u")
e = name_combined_lower.count("e")
true = str(t + r + u + e)
l = name_combined_lower.count("l")
o = name_combined_lower.count("o")
v = name_combined_lower.count("v")
e = name_combined_lower.count("e")
love = str(l + o + v + e)
#combining and converting strings for comparison
score = int(true + love)
# displaying results
if score < 10 or score > 90:
	print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
	print(f"Your score is {score}, you are alright together.")
else:
	print(f"Your score is {score}.")
