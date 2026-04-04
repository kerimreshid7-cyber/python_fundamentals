

# today we will see for loop with else  and nested loop.

for i in range(5):
    print('*'*i)
print("the loop is complited")

# revision on advanced for loop the concepts behind break,continue, and pass
# today i started some thing intersting neted loop and its very important for data enginering and also data analysis.
# and here is the evidence
for i in range(5):
    print('*'*i)
else:
    print("the loop is complited")   # the result is some thing so here using else is useless. so lets see where we had better to use this scenario.

print()


# for else with break. (most of the time we use for else to confirmation,verification and permission)
# challenge 1
# scan email to block un safe data from entering your system. and if it is clear give verification at the end
emails = [
    "samir21@gmail.com",
    "hana.kebede@yahoo.com",
    "abel.tech2024@outlook.com",
    "selamwork12@gmail.com"
]

for email in emails:
    if ";" in email:
        print("warning: here is sql injectiion")
        break
else:
    print("all emails are clear")
        
print()


# challege 2  finding in appropriate file name
files=[
"user_data.csv",
"chapter1.pdf",
"sales_data.csv",
"user_data.csv"
]
seen=[]

for file in files:
    if not file.endswith('csv'):
        print("here i found uncessary file.", file)
        break
else:
    print("all the files are ends with (.csv)")

# challenge 3 check if there is duplication in the emails
for file in files:         
        if file in seen:
            print("duplicate email",file)
            break
        seen.append(file)

# another way to solve the above challlenge using set insteade of list  bc set is more faster than llist to check duplication.
files=[
"user_data.csv",
"chapter1.pdf",
"sales_data.csv",
"user_data.csv"
]
seen=set()
for file in files:
    if file in seen:
        print("duplicated file here!")
        break
    seen.add(file)
else:
    print("there is no duplicated file in files.")

print()

# nested  loop (understanding the logic is get used to it is very importantfor BI and Data analysis.)
#it is a loop inside another loop. the inner loop runs complitly  first.
# we usually use it for combination of two or more lists,sets or (multiple data types and to clear tables

# for ex.
colors=["red","green","blue"]
sizes=["x","xx","xxl","l"]

for color in colors:
    for size in sizes:
        print(f"{color} with {size}")   # no of rows or line in the out put decided by the inner loop. so 4 4 answers for each colors.

print()

# challenge 4 write once all possible way to retrive : select count(*) from (tables_name) where (columns) is Null;

tables=['customers','orders','sales_data']
columns=['id','email']

for t in tables:
    for c in columns:
        print(f"select count(*) from {t} where {c} is Null;")
    # so now we can easily copy and paste then we can retrive what we want using nested loop.









































































