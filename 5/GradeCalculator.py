print("Welcome to your Letter Grade Calculator\n")

# Ask the user to enter their grades
math = float(input("What's your grade in Math: "))
science = float(input("What's your grade in Science: "))
english = float(input("What's your grade in English: "))
history = float(input("What's your grade in History: "))
worldLanguage = float(input("What's your grade in World Language: "))
physicalEducation = float(input("What's your grade in Physical Education: "))

# Store the average of all the grades into the averageGrade variable
averageGrade = (math + science + english + history + worldLanguage + physicalEducation) / 6

# Print the user's letter grade average based on their averageGrade
if averageGrade >= 90:
    letterGrade = 'A'
elif averageGrade >= 80:
    letterGrade = 'B'
elif averageGrade >= 70:
    letterGrade = 'C'
elif averageGrade >= 60:
    letterGrade = 'D'
else:
    letterGrade = 'F'

print(f"\nYour average grade is: {averageGrade:.2f}")
print(f"Your letter grade is: {letterGrade}")

# BONUS: Determine if the user can play sports
if averageGrade >= 70:
    print("You can play sports.")
else:
    print("You cannot play sports.")
