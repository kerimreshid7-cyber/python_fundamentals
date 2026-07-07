# finall day in list and i will cover tuple,set, and dictionary in this day. and i will differntiate the characterstics of all and then i will be smart enough to chooese data structure for every single real life tasks.

# tuple:is ordered data structure or multiple data type. and moslty it share the characterstics of list
#  but differ from list by it doesn't allow to change values mean it's fixed once created.
#  Tuple → accepts everything
# Tuples can store any data too.

data = (
    10,
    "hello",
    [1,2,3],     # even list allowed inside tuple
    {"age":21}
)

point = (3, 7)
print(point[0])   # x value
print(point[1])   # y value

students = [
    ("Abel", 85),
    ("Sara", 92),
    ("John", 78)
]

for name, score in students:
    print(name, score)


# Challenge 1 — Football Match Scores ⚽
# You have match results stored as tuples.
# Tasks
# Print only teams that won the match.
# Count how many matches ended in a draw.

matches = [
    ("Arsenal", "Chelsea", 2, 1),
    ("Barcelona", "Real Madrid", 3, 3),
    ("PSG", "Bayern", 0, 2)
]

for team1, team2, score1, score2 in matches:
    if score1 > score2:
        print(team1, "won")
    elif score2 > score1:
        print(team2, "won")

draws = 0

for team1, team2, score1, score2 in matches:
    if score1 == score2:
        draws += 1

print("Draw matches:", draws)


# Challenge 2 — Student Ranking System 🎓
# You receive student results:
# Tasks
# Print students who scored above 90.
# Find the top scorer.

students = [
    ("Bilal", 88),
    ("Ibrahim", 95),
    ("Abel", 70),
    ("Sara", 91)
]
# 1) Students who scored above 90
for name, score in students:
    if score > 90:
        print(name, score)



#2) Find the top scorer
top_student = students[0]

for student in students:
    if student[1] > top_student[1]:
        top_student = student

print("Top scorer:", top_student[0], top_student[1])



# Challenge 3 — Shop Receipt System 🛒
# Each item is stored as tuple (item, price, quantity)
# Tasks
# Calculate total cost of each item.
# Calculate the final bill.

cart = [
    ("Bread", 20, 2),
    ("Milk", 30, 1),
    ("Egg", 5, 12)
]

final_bill = 0

for item, price, qty in cart:
    total = price * qty
    final_bill += total
    print(item, "total =", total)

print("Final bill =", final_bill)



# set: is unorderd collection collection of unique values
# set :charaterstics 
# it's not orderd: mean what ever we have in set but when we print it we will get sorted out put(ascd)
# its not indexed:we can't access specific item using index bc it use hash function to  store values and that is why sets are fast to find values.
# it's unique data strucutre: it doesn't allow duplication.
# it's mutuable: we can update or change values. and this is the only characterstics it have what list have.

# 3) Set → only immutable items allowed
# Set items must be hashable.
# Allowed:
{10, "hi", 3.5, True, (1,2)}

# Not allowed:

# {[1,2,3]}      # list ❌    
# {{"a":1}}      # dict ❌
# {{1,2,3}}      # set ❌


set_sample={20,47,'hi','set','3.83'}   # i realized that we can store different data type in one set but we can't store list, tuple, and dictionaories in set.
print(set_sample)     #{'hi', 'set', '3.83', 20, 47} we got this in the out put this is why we say set is unorderd.
  
set_sample.add(50)
set_sample|={'wow set','it is amazing'}   # it's special method to add multiple values (set) in set.  but it's not allowed to add the other data structures.
print(set_sample)   #it look like it added new value randomly.


set_sample.remove(50)
#set_sample.remove(500)  # if we try to remove values that don't appear in set then we will get an error to fix this isssue we can use discard.
set_sample.discard(500)  #if the value is in set then it will remove it. unless, It will do nothing. we won't get an error.


# lets practice set oprations
candidate_A = {
    "Python", "SQL", "Excel", "PowerBI",
    "Pandas", "NumPy", "Git", "Linux",
    "Data Cleaning", "Data Visualization"
}

candidate_B = {
    "Python", "SQL", "Tableau", "Statistics",
    "Machine Learning", "Deep Learning",
    "Git", "Linux", "Big Data",
    "Data Visualization"
}

candidate_C = {
    "Excel", "PowerBI", "Communication",
    "Business Analysis", "SQL",
    "Project Management", "Presentation",
    "Data Visualization"
}
# find:   union
# A ∪ B
# A ∪ C
# A ∪ B ∪ C
print(candidate_A.union(candidate_B))
print(candidate_A|candidate_B)

print(candidate_A.union(candidate_C))
print(candidate_A.union(candidate_B.union(candidate_C)))
print(candidate_A|candidate_B|candidate_C)

#  intersaction
# A ∩ B
# A ∩ C
# B ∩ C
# A ∩ B ∩ C (skills ALL candidates share)

print(candidate_A.intersection(candidate_B))
print(candidate_A & candidate_B)

# print(candidate_A.intersection(candidate_B).intersection(candidate_C))
# print(candidate_A & candidate_B & candidate_C)

#difference
# Skills only A has (A − B)
# Skills only B has (B − A)
# Skills only C has (C − A)
# Skills A has but C doesn’t (A − C)

print(candidate_A.difference(candidate_B))
print(candidate_A-candidate_B)

#symetric diffence
# Skills not shared between A and C
# Skills not shared between B and C

print(candidate_A.symmetric_difference(candidate_C))
print(candidate_A ^ candidate_C)

# now lets practice relationships in set
# PART 5 — Subset & Superset Checks
# Job requirement:
job_requirements = {"Python", "SQL", "Git", "Linux"}

# Check:
# Who qualifies for the job?


print("is candidate A is ready for job",job_requirements.issubset(candidate_A)) # we are checking all cources in job requirments are apppear in candidate_A?
print("is candidate B is ready for job",job_requirements.issubset(candidate_B)) 
print("is candidate C is ready for job",job_requirements.issubset(candidate_C))

# # then we can easily hire the employee by checking their skills using relation ship in set

# lets go depper in relations in set
python_dev = {"Python", "Git", "SQL"}
data_scientist = {"Python", "Git", "SQL", "Statistics", "Machine Learning"}
frontend_dev = {"HTML", "CSS", "JavaScript"}
backend_dev = {"Python", "SQL", "API", "Git"}

# challenge 1: (supper set)
# Check if data_scientist is a superset of python_dev

print("have data_scintists all skills that pyhton developers have",data_scientist.issuperset(python_dev))

#challenge 2:  (proper sub set and proper supersubset)
# is python_dev a proper subset of data_scientist
# Use operators:
# <   proper subset
# >   proper superset
print('is python_dev a proper subset of data_scientist',python_dev<data_scientist)

# # challenge 3:  (proper sub set and proper  super subset))
# # # is python_dev a proper supersubset of data_scientist.
# # print('is python_dev a proper supersubset of data_scientist',python_dev>data_scientist)

# # # Check if frontend_dev and python_dev are disjoint.

# # print("are frontend_dev and python_dev absolutly differnt?" ,frontend_dev.isdisjoint(python_dev))



# # # dictioanries:are  power full data structures in python
# # # variable={'key':'value',key:value,'key',value,key:"value"}  these are possible ways to create dict.

# # # dictionariy characterstics:
# # # 1 orderd
# # # 2 unique for keys but allow duplication for values
# # # 3 not indexed(it's keyed) : which means we can acces the value by the key not index no.
# # # 4 mutable

# # # special methods for dictionaries
users={'name':'kerim','age':23,'roll':'BI analyst'}
print(users['name'])  # but the problem is if key name not in dict. so it better to use .get
#print(users.get['name'])  # if there is no name then return None

# checking keys and values in dict
print('name' in users)
print(23 in users)
print('country' not in users)

# to access  only key and only value.
print(users.keys())    #to get all keys
print(users.values())  # to get all values
print(users.items())   # to get all keys and values in set of tuple so it makes easy to itrate,loop,transform and so on...
print(users.get("city"))
print(users.get("city", "Not provided"))

profile = {
    "username": "kerim",
    "email": "kerim@gmail.com"
}
phone = profile.get("phone", "No phone number")
print(phone)
print()

# itration and loop in dictionary.
for u in users:
    print(u)    # we will get only keys

for u in users:
    print(u,users[u])    # doon't confused here bc it seems to indexing but its not actually indexing  dict is keyed not indexed.
 
for key,value in users.items():    # the best recomended way to loop and itrate.
    print(key,value)


# # update, add remove in dict
users['age']=23
users['residence']='haramaya'
users.update({'name':'kerim','country':'ethiopia'})


users.pop('name')
users.popitem()         # to remove the last key and value    .pop() is to remove the last item in list.
#users.pop('salary')      # if we don't have key(salary)  then return error and stop excution it's somehting like annoooying so we can use 
users.pop('salary',None)   #now evrything fine when we debt about somthing we have or havn't in list then we had better to use key comma None.
#users.clear()
# print(users)

#real life uses of dictionary
# to map abbrevation with there actual name
# to use for meta data    like this {'id':{'type':'int','nulleble':False}}
# for configuration....

# dict comprehensions
users={'name':'kerim','age':23,'roll':'BI analyst'}

# challenge 
# print the string values only out of the dict
users={key:value.upper() for key,value in users.items() if  isinstance(value,str)}
print(users)

