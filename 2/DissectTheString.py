print("Welcome to Dissect that String!\n")

# Capture user input
user_string = input("Please enter a string: ")

# Calculate and print the length of the user-inputted string
print("Word Count: " + str(len(user_string)))

# Transform the user_string to all uppercase letters and print
print("In upper case: " + user_string.upper())

# Transform the user_string to all lowercase letters and print
print("In lower case: " + user_string.lower())

# Retrieve and print the first letter of the user_string
print("The first letter of the string is: " + user_string[0])

# Retrieve and print the last letter of the user_string
print("The last letter of the string is: " + user_string[-1])