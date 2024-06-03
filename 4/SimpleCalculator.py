import math

# Greet the user
print("Welcome to the Simple Calculator!\n")

# Ask the user for two numbers and print the sum
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
print("Sum: " + str(num1 + num2))

# Ask the user for two numbers and print the difference
num1 = float(input("\nPlease enter the first number: "))
num2 = float(input("Please enter the second number: "))
print("Difference: " + str(num1 - num2))

# Ask the user for two numbers and print the product
num1 = float(input("\nPlease enter the first number: "))
num2 = float(input("Please enter the second number: "))
print("Product: " + str(num1 * num2))

# Ask the user for two numbers and print the quotient
num1 = float(input("\nPlease enter the first number: "))
num2 = float(input("Please enter the second number: "))
if num2 != 0:
    print("Quotient: " + str(num1 / num2))
else:
    print("Quotient: Division by zero is not allowed.")

# Ask the user for two numbers and print the first number raised to the second number
num1 = float(input("\nPlease enter the base number: "))
num2 = float(input("Please enter the exponent: "))
print("Exponentiation: " + str(math.pow(num1, num2)))

# Ask the user for one number and print the absolute value
num = float(input("\nPlease enter a number to find its absolute value: "))
print("Absolute Value: " + str(math.fabs(num)))

# Ask the user for one number and print the square root
num = float(input("\nPlease enter a number to find its square root: "))
if num >= 0:
    print("Square Root: " + str(math.sqrt(num)))
else:
    print("Square Root: Cannot compute square root of a negative number.")
