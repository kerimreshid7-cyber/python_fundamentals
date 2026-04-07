
#       single if statments(only one condition) if the condition is true then go and excute it if it's false just skip  and go to the end
# Challenge 1: Positive Number
# Write a program that checks if a number is positive.
x=34 
if x>0:
    print('yes it is positive')

h=-2
if h>0:
    print('yes it is positive')

k=0
if k>0:
    print('yes it is positive')
#this three are indipendent if statments wc mean there is no thing that reltes them.
# and it's directly assigned varibles. so now what if it's like user input format then in that case pyton gonna excuter one after another with order(1st come 1st served.)
# we got only one out bc the two conditions are false then pyhton just skipped them that we didn't get out put.


# Challenge 2: Adult Check
# Write a program to check if someone is an adult.
# Rule:
# If age is 18 or more, print "You are an adult".

age=int(input("enter your age"))
if age>=18:
    print("you are adult")
#if we enter enter 18 and above with no limite the out put is you are adult 
# and it's not satisfying bc if the user enter <18 then python give us nothing so this is where we actaully need else and also elif.

# rule for if elif and else: if is mandatory comes always first assining condition is mandatory  only one if we can have unless it's nested if
#                            elif is optional comes after if   assigninig con is mandatory       may be multiple elif we have in on if statment.
#                            else optional comes at the last   assigninig con is optional        only one if we can have    


# 1. Even or Odd (%)
# Ask the user to enter a number.
# Rules:
# If the number is divisible by 2 → print "Even number"
# Otherwise → print "Odd number"
number=int(input("enter a number"))
if number%2==0:
    print('the number is even')
else:
    print("the number is odd")
# it's nice but what if the user input 0 or with out string this is exactly we need more explanation using elif(else if)

# Challenge 1 — Even, Odd,Zero,or invalid input
num=int(input('enter a number'))
if num==0:
    print(num,'is nither')
elif num%2==0:
    print(num,'is even')
elif num%2==1:
    print(num,'is odd')
else:
    print("invalid input")



# i just realized that if we have more than one conditional statment(with user input) in our code
# the exucution will be one after another not once. first come come fist seved.


# simple challenges
# 1. Sales category
sales = float(input("Sales: "))
print("High" if sales > 5000 else "Low")
# 2. Check even transaction batch
num = int(input("Transactions: "))
print("Even batch" if num % 2 == 0 else "Odd batch")


# 3. Profit calculation
r = float(input("Revenue: "))
c = float(input("Cost: "))
print("Profit:", r - c) 

# 4. Validate age range
age = int(input("Age: "))
print("Valid" if 0 <= age <= 120 else "Invalid")


#  4. Identity + Equality Check (IMPORTANT)
a = input("Enter value: ")
b = input("Enter value: ")

print("Same value:", a == b)
print("Same object:", a is b)


# 5. Multi-step Data Validation System
data = input("Enter numeric value: ").strip()

if data.replace('.', '', 1).isdigit():
    num = float(data)

    if 0 <= num <= 100:
        print("Valid score:", num)
    else:
        print("Out of range")
else:
    print("Invalid input")

