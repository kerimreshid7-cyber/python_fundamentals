# deeper copy this is not built in function so we gotto to import the copy module.
matrix=[[1,3,4,7],
        [7,3.83],
        [1,1,0,"",None,False],
        [1,1,7,5,90.98]]

matrix_copy=matrix.copy()     # as we know if we use .copy so there is no more affected original or copy list while we update on of the two but here is some issue    

matrix[2].append('woow')       # its fine the copy one will not affected.
matrix_copy[-1].append('z')    # but now the original list is affected by this change.

print("orignal",matrix)
print("copy",   matrix_copy)


# this is when exactly we need to use copy module by import. by the way it for nested list.

import copy
matrix_copy=copy.copy(matrix)     # so the problem is fixed.
matrix_copy[-1].append("now it won't affect the parent list ") 

print("orignal",matrix)
print("copy",   matrix_copy)


copy1=matrix 
print('are the same',copy1 is matrix )    #true bc python made same  store id for both. that is why when we change the orginal the copy also affectd and vice versa.

copy2=matrix.copy()
print('are the same',copy2 is matrix )     # false bc python made differnt store id for each


# list is itrable which means we can loop through list for may be transformation and so on...
itrable=['k','r','m',]
new_itrable=[]
for l in itrable:
    l= l.upper()
    new_itrable.append(l)
    print(new_itrable)

print()

#   or if we don't want the progres we just want the final answer.
itrable=['k','r','m',]
new_itrable=[]
for l in itrable:
    l= l.upper()
    new_itrable.append(l)
print(new_itrable)

print()

# but we can easily change to upper case with out for loop.
print(list(map(str.upper,itrable)))
numbers=["7","4","3","5"]
print(list(map(int,numbers)))      # to change the string in list to integer. 

stus_name=['  kerim  ','  ebrahim   ']
for name in list(map(str.strip,stus_name)):
    print(name)



# enumerate: to just show the items in list with there index no.

print(list(enumerate(itrable)))            # this is more powerful  and amazing function in python.
print(list(enumerate(itrable, start=1)))   #if we wnat to start fro one cause the diffault is zero.

# Challenge — Compare two football teams match results
# You have two lists:
team_A_goals = [2, 1, 3, 0, 4]
team_B_goals = [1, 2, 1, 0, 2]

# Your task:
# Read the matches from last → first (use reversed())
# Compare goals using zip()
# For each match print result like:

reverse_team_A_goals = reversed(team_A_goals)
reverse_team_B_goals = reversed(team_B_goals)

relation_teamA_teamB = list(zip(reverse_team_A_goals, reverse_team_B_goals))

A_wins = 0
B_wins = 0
draws = 0
match_number = 1

for a, b in relation_teamA_teamB:
    
    if a > b:
        print("Match", match_number, "→ Team A Win")
        A_wins += 1
        
    elif b > a:
        print("Match", match_number, "→ Team B Win")
        B_wins += 1
        
    else:
        print("Match", match_number, "→ Draw")
        draws += 1
        
    match_number += 1

print("\nSummary")
print("Team A wins =", A_wins)
print("Team B wins =", B_wins)
print("Draws =", draws)


# lambda:thiny or simple function it is inline function
sqaure=lambda x:x**2
print(sqaure(3))

sqaure=lambda x,y: x +y
print(sqaure(3,5))

membership=lambda i: i in "python"
print(membership('p'))

# lambda + map 

prices=["$123.45",'$34.56']
print(list(map(lambda p:float(p.replace('$','')),prices)))    # this is how we can clean by replacing using map and lambda


# filter: to filter out the needed items from list 
# real life challenge  using direct filter function

car_brand = ['toyota','marchedise','volvo']
car_prices = ["$123,500.45", "$340,000.56", "$430,000"]

# Convert prices to numbers
numeric_prices = [float(p.replace('$','').replace(',','')) for p in car_prices]

# Zip brand + numeric price
full_info = list(zip(car_brand, numeric_prices))

# Filter expensive cars (>200000)
expensive_cars = list(filter(lambda x: x[1] > 200000, full_info))

# Print results
for car, price in expensive_cars:
    print(car)

# the same challenge with no direct filter function.
car_brand=['toyota','marchedise','volvo']
car_prices=["$123,500.45",'$340,000.56','$430,000']
 
numeric_prices = list(
    map(lambda p: float(p.replace('$','').replace(',','')), car_prices)
)
full_info = list(zip(car_brand, car_prices, numeric_prices))

for car, price_text, price_num in full_info:
    if price_num > 200000:
        print(car, price_text)



# List Comprehension
# A list comprehension is a compact way to create a new list in Python by applying an expression to each 
# item in an existing iterable (like a list, tuple, or range), optionally including a condition.
#lets pracitce with real life examples.

#  1. Squaring numbers
# Easy but very common in data analysis and math problems.
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)


# 2. Filtering even numbers
# Use a condition inside the comprehension to keep only certain elements.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [x for x in numbers if x % 2 == 0]
print(evens)


# 3. Cleaning messy strings
# Perfect for real-world data cleaning (like we did with prices or names).
names = ['  bilal  ', '  ebrahim$$#', ' #kerim #$']
clean_names = [name.strip().replace('#','').replace('$','') for name in names]
print(clean_names)
