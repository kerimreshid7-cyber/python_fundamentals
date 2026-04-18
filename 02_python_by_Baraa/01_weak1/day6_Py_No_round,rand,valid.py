
# round, random and validation
# round    today i will cover floor and ceil rounding since i had covered normal rounding in yesterday's session.

import math       # this is library in python to use mathematical operations (advanced).

gpa = 3.83436778
print(math.floor(gpa))    # we will get 3 because we didn't define after decimal. 
print(math.floor(gpa*1000)/1000)  # advanced  # further the video I practicing with chat GPT so this is how we can round to floor by expressing the digits after decimal we want using a method from chat GPT.

print(math.ceil(gpa*100)/100)  # advanced # to round to ceil the value by defining how many digits we want after decimal.
print(math.ceil(gpa))          # to round to next no (ceil) with no decimals. (no more decimals like int(), trunc) but it's rounding and differs from others.

print(math.trunc(gpa))   # again we will get 3. But the difference is trunc is used to cut the no after decimal. There is no need 
# to import math for only trunc; we can use int(). But when we should use trunc is when we already imported math for another purpose because "using int might confuse us ohh I am using int() so the value was str just like confusion."  Barra said.

# random   used to generate random numbers in float   
# randint   used to generate random numbers in integer.
import random
print(random.random())      # we got 0.something (it will never go out of 0-1) and anytime we run it it will generate different no. and its float.

print(random.randint(1,6))  # now we want to get random integer whenever we run the code and we define boundary so, we will never get out of these numbers. I think Ludo (game) used it.
print(random.randint(1,1000)) # generate random numbers; both boundaries will be included. Unlike slicing which is extracting [-3:-7], starting -3 included but end -7 not included.
# so, how and when we will use it as data analysts? For example, imagine we have a large dataset (customers table) then we want to pick 10 customers. We can use random
# it's not much needed for data analysis, but knowing it is important.

# validation   
n = 23
#print(n.is_integer)           #  This is wrong; is_integer is a method of float objects
#print(n.is_integer())         # works only if n is float
print(isinstance(n, float))     # to validate our value using isinstance we will get True or False
print(isinstance(n, int))

c = 3
print(c)
# print(c.is_integer())        # won't work because c is int, not float
print(isinstance(c, float))     # False
print(isinstance(c, int))       # True

# 14. Round KPI
kpi = float(input("KPI: "))
print(round(kpi, 2))

