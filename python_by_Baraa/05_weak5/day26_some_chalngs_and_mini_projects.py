# CHALLENGE 1 — PRODUCT PRICE ANALYSIS

products = {
 "Laptop":1200,
 "Phone":800,
 "Tablet":450,
 "Monitor":300,
 "Keyboard":150
}

# TASKS
# 1) Find MOST EXPENSIVE PRODUCT
# 2) Find CHEAPEST PRODUCT
# 3) Calculate TOTAL INVENTORY VALUE


def most_expensive_product(data):
    return max(data, key=data.get)

def cheapest_product(data):
    return min(data, key=data.get)

def total_inventory_value(data):
    return sum(data.values())

# ▶ EXECUTION
print("========== CHALLENGE 1 ==========")
print("Most expensive:", most_expensive_product(products))
print("Cheapest:", cheapest_product(products))
print("Total inventory value:", total_inventory_value(products))



# CHALLENGE 2 — WORD FREQUENCY ANALYSIS

text = "python is easy and python is powerful and python is fun"

# TASKS
# 1) Count TOTAL WORDS
# 2) Count UNIQUE WORDS
# 3) Find MOST COMMON WORD


def word_count(text):
    return len(text.split())

def unique_word_count(text):
    return len(set(text.split()))

def most_common_word(text):
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return max(freq, key=freq.get)

# ▶ EXECUTION
print("\n========== CHALLENGE 2 ==========")
print("Total words:", word_count(text))
print("Unique words:", unique_word_count(text))
print("Most common word:", most_common_word(text))



# MINI PROJECT 1 — WEBSITE VISITOR ANALYSIS

"""
PROJECT DESCRIPTION:
This project analyzes website traffic data.
It helps understand total views, page popularity, and user behavior.
"""

visits = [
 {"page":"Home","views":150},
 {"page":"Products","views":120},
 {"page":"Home","views":100},
 {"page":"Contact","views":60},
 {"page":"Products","views":80},
]

def total_views(data):
    return sum(v["views"] for v in data)

def views_per_page(data):
    result = {}
    for v in data:
        result[v["page"]] = result.get(v["page"], 0) + v["views"]
    return result

def most_visited_page(data):
    pages = views_per_page(data)
    return max(pages, key=pages.get)

# ▶ EXECUTION
print("\n========== WEBSITE ANALYSIS ==========")
print("Total views:", total_views(visits))
print("Views per page:", views_per_page(visits))
print("Most visited page:", most_visited_page(visits))



# MINI PROJECT 2 — STUDENT SCORE ANALYSIS

"""
PROJECT DESCRIPTION:
This project analyzes student exam scores.
It identifies top performers, average performance, and passed students.
"""

students = [
 {"name":"Ali","score":85},
 {"name":"Sara","score":92},
 {"name":"John","score":78},
 {"name":"Mike","score":88},
 {"name":"Lina","score":95},
]

def average_score(data):
    return sum(s["score"] for s in data) / len(data)

def top_student(data):
    return max(data, key=lambda x: x["score"])

def passed_students(data):
    return [s for s in data if s["score"] >= 80]

# ▶ EXECUTION
print("\n========== STUDENT ANALYSIS ==========")
print("Average score:", average_score(students))
print("Top student:", top_student(students))
print("Passed students:", passed_students(students))



# MINI PROJECT 3 — MOVIE RATING ANALYSIS

"""
PROJECT DESCRIPTION:
This project analyzes movie ratings.
It finds the best movie, average rating, and high-rated movies.
"""

movies = [
 {"title":"MovieA","rating":4.5},
 {"title":"MovieB","rating":3.8},
 {"title":"MovieC","rating":4.9},
 {"title":"MovieD","rating":4.2},
]

def average_rating(data):
    return sum(m["rating"] for m in data) / len(data)

def best_movie(data):
    return max(data, key=lambda x: x["rating"])

def movies_above_4(data):
    return [m for m in data if m["rating"] > 4]

# ▶ EXECUTION
print("\n========== MOVIE ANALYSIS ==========")
print("Average rating:", average_rating(movies))
print("Best movie:", best_movie(movies))
print("Movies above 4:", movies_above_4(movies))