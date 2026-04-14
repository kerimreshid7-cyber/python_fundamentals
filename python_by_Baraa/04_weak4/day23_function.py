
# hi every one today i will cover the basics of function in pyhton. 

# what is function?
# function is a block of code that perform  a specific task.so we can reuse it what ever we want.

# why we need function?
# once we use function for some specific problem then if we face (have to fix) the problem then simply copy and paste.
# and function allows modularity which mean  breaking down the complex and larg systems then we can easily do it step by step.


# types of functions:  there are four types of functions 
# 1 built in function:built by pyhton devs and offer directly with python the simplest one.
# 2 standard library: the offer not default like print() but we can easily import  and use them ex. math and random
# 3 external library: built by another community not pyhton devs so we have to install them import and then use them simply.    ex panda, matplotlip and numpy.
# 4 user defined fun f(x): this what we can build from the scrutch then we can use what ever we want so today i will cover this one. 


# golden rule: cheack if it is in built in fun then in standard libraries then check your team user defined fun f(x) and  after that go and build the function in your own.


# how function works

# 1 definition:it's just defining the function.
print('wow pyhton')       # pyhton will excute this authomatically

def greeting():           # oh the user is commanding me to create function named greeting i to have to do it.
    print('wow function')  # python won't give us out put rather i craete object and put the value then when we call it it returns. 
print(greeting)             # this is how we can exactly call a function.


#lets startby this brain storming code   what is this?
x = 100

def test(x):
    x = x + 50
    print("Inside:", x)

test(10)
print("Outside:", x)



# PART 1 — What is a Function (Real Life First)

# Imagine a coffee machine ☕

# You press a button → machine makes coffee → you get coffee.

# You don’t care how it works inside.
# You just use it whenever you want.

# A function is exactly like that.

# A function is a reusable block of code that performs a task.

# Instead of writing the same code again and again, we put it inside a function and reuse it.

# PART 2 — Why Functions Exist (The Problem They Solve)

# Without functions:

print("Welcome Bilal")
print("Welcome Ahmed")
print("Welcome Sara")
print("Welcome John")

# You repeat code again and again.

# With function:

def welcome():
    print("Welcome")

welcome()
welcome()
welcome()

# We write once → use many times.

# Benefits:
# • Saves time
# • Reduces errors
# • Makes code readable
# • Makes big projects possible

# Think of functions as tools in a toolbox.

# PART 3 — Function Syntax (Structure)

# The skeleton:

# def function_name():
#     code

# Example:

def say_hello():
    print("Hello!")

# Break it down:

# Part	Meaning
# def	tells Python we create a function
# say_hello	function name
# ()	place for inputs
# :	start of function body
# indentation	code inside the function

# Calling the function:

say_hello()

# Output:

# Hello!

# Important rule:
# Function runs ONLY when called.

# PART 4 — Parameters (Function Inputs)

# Real life analogy:
# Coffee machine needs inputs:
# • Water
# • Coffee beans
# • Sugar

# Functions also need inputs → called parameters.

# Example:

def greet(name):
    print("Hello", name)

# Call it:

greet("Bilal")
greet("Sara")

# Output:

# Hello Bilal
# Hello Sara

# The function becomes flexible.

# PART 5 — Multiple Parameters
def add(a, b):
    print(a + b)

add(3, 5)
add(10, 2)

# Output:

# 8
# 12

# Think of calculator:
# Input → numbers
# Output → result

# PART 6 — return vs print (VERY IMPORTANT)

# Most beginners confuse this.

# print → shows result
# return → gives result back

# Real life analogy:

# Chef:
# • print → shows food in restaurant
# • return → gives takeaway box to customer

# Example using print:

def add(a, b):
    print(a + b)

result = add(3,5)
print(result)

# Output:

# 8
# None

# Why None?
# Because function didn’t return anything.

# Now with return:

def add(a, b):
    return a + b

result = add(3,5)
print(result)

# Output:

# 8

# Rule:
# Use return when you want to reuse the result.

# PART 7 — Why return is Powerful
def add(a,b):
    return a+b

def multiply(x,y):
    return x*y

answer = multiply(add(2,3), 10)
print(answer)

# Flow:
# add(2,3) → 5
# multiply(5,10) → 50

# Functions can work together.

# This is how big systems are built.

# PART 8 — Default Parameters

# Sometimes we want default values.

# Example:

def greet(name="Friend"):
    print("Hello", name)

greet()
greet("Bilal")

# Output:

# Hello Friend
# Hello Bilal

# Like YouTube volume default = 50.

# PART 9 — Keyword Arguments
def student(name, age):
    print(name, age)

student(age=22, name="Bilal")

# Order doesn’t matter when using keywords.

# PART 10 — Positional vs Keyword
# student("Bilal",22)        # positional
# student(age=22,name="Bilal")  # keyword
# PART 11 — Arbitrary Arguments (*args)

# When you don’t know how many inputs.

# Pizza shop analogy 🍕

# Customer: "Add toppings… many toppings"

def toppings(*items):
    print(items)

toppings("cheese","meat","olives")

# Output:

# ('cheese','meat','olives')

# It becomes a tuple.

# Example sum:

def total(*numbers):
    return sum(numbers)

print(total(1,2,3,4,5))
# PART 12 — Arbitrary Keyword Arguments (**kwargs)

# Unknown named inputs.

def profile(**info):
    print(info)

profile(name="Bilal", age=22, job="Student")

# Output:

# {'name':'Bilal','age':22,'job':'Student'}

# This becomes a dictionary.

# PART 13 — Scope (Local vs Global)

# This part is HUGE.

# Local variable → inside function
# Global variable → outside function
x = 10

def test():
    x = 5
    print(x)

test()
print(x)

# Output:

# 5
# 10

# Inside function → separate world.

# Function is like a room.
# Outside variables cannot be changed inside unless you allow it.

# PART 14 — Nested Functions

# Function inside function.

def outer():
    def inner():
        print("Inner function")
    inner()

outer()

# Used in advanced programming.

# PART 15 — Lambda Functions (Mini Functions)

# Tiny one-line functions.

# Normal:

def square(x):
    return x*x

# Lambda:

square = lambda x: x*x
print(square(5))

# Used for quick tasks.

# Example with sorting:

students = [("Bilal",80),("Sara",95),("Ali",70)]
students.sort(key=lambda x:x[1])
print(students)

# Sort by score.

# PART 16 — Functions Calling Functions
def greet():
    return "Hello"

def message():
    return greet() + " Bilal"

print(message())

# Functions can build on each other.

# PART 17 — Recursion (Function calling itself)

# Real life: mirror facing mirror.

# Example: factorial.

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# Flow:
# 5×4×3×2×1

# PART 18 — Docstrings (Function Description)
def add(a,b):
    """This function adds two numbers"""
    return a+b

# Used in professional projects.

# PART 19 — Why Functions Matter in Real Projects

# Without functions:
# • 10,000 lines messy code
# • Impossible teamwork

# With functions:
# • Organized modules
# • Reusable components
# • Easier debugging
# • Cleaner code

# Large apps = thousands of functions.

































































