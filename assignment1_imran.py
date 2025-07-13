# Task 1: Perform Basic Mathematical Operations
# Problem Statement:
# 1. Takes two numbers as input from the user.
# 2. Performs Addition, Subtraction, Multiplication, and Division.
# 3. Displays the results of each operation.

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"

# Display results
print("\n--- Math Operations Results ---")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print(f"Num 1 is {num1} and Num 2 is {num2}")

# -------------------------------------------------------------

# Task 2: Create a Personalized Greeting
# Problem Statement:
# 1. Takes a user's first and last name as input.
# 2. Concatenates them into a full name.
# 3. Prints a personalized greeting.

# Input first and last name
first_name = input("\nEnter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Create full name and greet
full_name = first_name + " " + last_name
print(f"Hello, {full_name}! Welcome to the Python program.")
