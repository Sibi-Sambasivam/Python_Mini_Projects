import random
import math

print("Welcome to the lucky number generator!\n")

fName = input("Enter your first name: ")
lName = input("Enter your last name: ")
age = int(input("Enter your age: "))

x = abs(len(fName) + len(lName))
y = random.randint(1, 100)

luckyNum = math.ceil(x + y + age)

print("Your lucky number is: " + str(luckyNum))
