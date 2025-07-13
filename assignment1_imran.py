# Task 1: Perform Basic Mathematical Operations

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Different operations
addition = num1 + num2
substraction = num1 - num2
multiplication = num1 * num2

# Checking num2 is not zero
if num2 != 0:
    division = num1 / num2
else:
    division = "unidentified"

# Display results
print("add", addition)
print("subtraction", substraction)
print("multiplication", multiplication)
print("division", division)
print("num 1 is", num1, "and num 2 is", num2)

# ------------------------------------------------------

# Task 2: Personalized Greeting

# Input first and last name
name1 = str(input("Enter your first name: "))
name2 = str(input("Enter your last name: "))

# Full name
name = name1 + name2

# Greet with message
print("hello,", name + " welcome to the python program")
