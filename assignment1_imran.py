# Task 1: Perform Basic Mathematical Operations

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Num 1 is", num1, "and Num 2 is", num2)

# Task 2: Personalized Greeting

first_name = input("\nEnter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
full_name = first_name + " " + last_name
print("Hello,", full_name + "! Welcome to the Python program.")
