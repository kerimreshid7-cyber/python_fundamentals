
# loop (wow very intersting and important lesson it is.) it's the way of control our code we can say it it'logic to itrate while the condition is true insted of writing a code again again and again. 

# before that i want have to some revision on if statment again to practice "if not" . after that i'll start the new concept 
# here after if it's god's will i'll do so many real life practical challenges in the next allso the privioous concepts. it'll help me to have strong foundation.
# i hope i'll turn the set back into a come back. cause i am full of life right now. my deacline happens once in a blue moon.


# Challenge: Number Analyzer
# Write a program that receives a variable called value and prints one of the following:

value = 10  # change and test

if not isinstance(value, int):
    print("invalid")
elif value == 0:
    print("zero")
elif value < 0:
    print("negative number")
else:
    result = "positive even" if value % 2 == 0 else "positive odd"
    if value % 5 == 0:
        result += " & multiple of 5"
    print(result)


# so lelts start todays lesson  
# loops 
# here we'll see two types of loops for loop and while loop we'll focus especially on for loop as my ambition is to be BI analyst.
print("round 1")
print("round 2")
print("round 3")
print("round 4")
print("round 5")  # if we want to print this type of senario we can write like this but it's boring and amater level. 
#even it's fine what if we have to write hundrads or thousand or million times it'll absollutly difficul and imposiblle.
# but we have the concept of loop 


for i in(1,2,3,4,5):
    print(f"round {i}")  # can you look how much it's easy and smart. this logic will do the same thing as the first one.

# then lets see for loop with variable taht is already assigned.
items=(1,2,3,4,5)
for item in items:
    print(f"item {item}")


















































































