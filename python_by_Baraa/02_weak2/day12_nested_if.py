
# nested if these are if statments inside another if statments to check multiple conditions once then to 
# give appropriate respond

# to i got to do real life practical challenges. lets continue

#Challenge 1: Login system
#Task:
# Ask for username and password
# If username is "admin":
# If password is "1234" → “Login successful”
# Else → “Wrong password”
# Else → “User not found”

username = input("Enter your name: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")


# Challenge 2: Even/Odd + Positive/Negative
# Task:
# Ask for a number:
# First check if it's valid (number)
# Then:
# If number ≥ 0:
# If even → “Positive Even”
# Else → “Positive Odd”
# Else:
# If even → “Negative Even”
# Else → “Negative Odd”


try:
    num = int(input("Enter a number: "))

    if num >= 0:
        if num % 2 == 0:
            print("Positive Even")
        else:
            print("Positive Odd")
    else:
        if num % 2 == 0:
            print("Negative Even")
        else:
            print("Negative Odd")

except:
    print("Invalid input")     # i used error handling here i know it before.




# revision challenges
# 1. Full Data Cleaning + Validation Pipeline
raw = input("Enter customer name: ")

clean = raw.strip().title()

if clean and clean.replace(" ", "").isalpha():
    print("Clean Name:", clean)
else:
    print("Invalid data")



#i will master this concept through time over many practical challenges.



















































































