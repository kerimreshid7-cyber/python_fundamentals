# finall day in list and i will start tuple in this day.

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

# point = (3, 7)
# print(point[0])   # x value
# print(point[1])   # y value

# students = [
#     ("Abel", 85),
#     ("Sara", 92),
#     ("John", 78)
# ]

# for name, score in students:
#     print(name, score)


# # Challenge 1 — Football Match Scores ⚽
# # You have match results stored as tuples.
# # Tasks
# # Print only teams that won the match.
# # Count how many matches ended in a draw.

# matches = [
#     ("Arsenal", "Chelsea", 2, 1),
#     ("Barcelona", "Real Madrid", 3, 3),
#     ("PSG", "Bayern", 0, 2)
# ]

# for team1, team2, score1, score2 in matches:
#     if score1 > score2:
#         print(team1, "won")
#     elif score2 > score1:
#         print(team2, "won")

# draws = 0

# for team1, team2, score1, score2 in matches:
#     if score1 == score2:
#         draws += 1

# print("Draw matches:", draws)


# # Challenge 2 — Student Ranking System 🎓
# # You receive student results:
# # Tasks
# # Print students who scored above 90.
# # Find the top scorer.

# students = [
#     ("Bilal", 88),
#     ("Ibrahim", 95),
#     ("Abel", 70),
#     ("Sara", 91)
# ]
# # 1) Students who scored above 90
# for name, score in students:
#     if score > 90:
#         print(name, score)



# #2) Find the top scorer
# top_student = students[0]

# for student in students:
#     if student[1] > top_student[1]:
#         top_student = student

# print("Top scorer:", top_student[0], top_student[1])



# # Challenge 3 — Shop Receipt System 🛒
# # Each item is stored as tuple (item, price, quantity)
# # Tasks
# # Calculate total cost of each item.
# # Calculate the final bill.

# cart = [
#     ("Bread", 20, 2),
#     ("Milk", 30, 1),
#     ("Egg", 5, 12)
# ]

# final_bill = 0

# for item, price, qty in cart:
#     total = price * qty
#     final_bill += total
#     print(item, "total =", total)

# print("Final bill =", final_bill)



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
set_sample.discard(500)  #if the value is in set then it will remove it unless it will do nothing. we won't get an error.


# lets practice relation ships in set
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























