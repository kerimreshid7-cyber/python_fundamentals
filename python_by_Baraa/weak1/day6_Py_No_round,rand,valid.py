

#    round,random and validation
# round    today i will cover floor and ceil roudning since i had covered normal rounding in yesterdays sesssion.

import math       # this is library in python to use mathimathical oprations(advanced) .

gpa=3.83436778
print(math.floor(gpa))    # we will get 3 bc we didn't defined after decimal. 
print(math.floor(gpa*1000)/1000) #advanced  # further the video i practicing with chat gpt  so this is how we can round to floor by expressing the digits after decimal we want using a method from chat gpt.

print (math.ceil(gpa*100)/100) #advanced # to round to ceil the value by definig how many digits we want   after decimal.
print(math.ceil(gpa))          # to round to neaxt no(ceil) with no decimals.(no more decimals like int(),trunc) but it's rounding and differ from others.


print(math.trunc(gpa))   # again we will get 3.but the dnce is trunc is used to cut the no after deciaml. there is no need 
# to import math for only trunc we can use int() but when we should to use trunc is when we already imported math for another purpose bc "using int might confused us ohh i am using int() so the value was str just like confusion."  Barra said.


# random   used to generate random numbers in float   
# randint   used to generate random numbers in integer.
import random
print(random.random())      # we got 0.something(it will never out of o.bla bla ) and any time when run it it will generate different no. and its float.

print(random.randint(1,6))  # now we want to get random integer whenever we run the code and we define boundary so, we will never get out of these no. i think ludo(game) used it.
print(random.randint(1,1000)) #  generate random numbers both boundaries will included. unlike slicing which is extracting[-3:-7] starting -3 included but end -7 not included.
# so, how and when we will use it as data anlysts for ex. imagine we have a large data set(customers table) then we want to pick 10 customers. we can use random


# # validation   
n=23
print(n.is_integer)           # to validate our value using .is_integer.  herre we will get brief explanation instade of true or false

print(isinstance(n,float))     # to validate our value using isinstance we will get True or false
print(isinstance(n,int))


# c=3
# print(c)
# print(c.is_integer)

# print(isinstance(c))





















































