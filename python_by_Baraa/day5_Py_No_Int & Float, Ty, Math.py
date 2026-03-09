 
    #  pyhon numbers
#types are built in functions in python
# 1 type to know the type of the value,2 int we can use to change the value in to integer fro ex. from string,
# 3 float to change to float and 4 complex to change to complex. these  are python built in functions.
x=12 
print(type(x))
salary="3400"
print(int(salary)*1.10)     #here we are changing the str to int and apply opratore * to increase the salary by 10%.
gpa='3.83'
gpa='3.83'
print(float(gpa))          # we will show float which is the data type of the value. then to see  the data type we can apply type(gpa).

adv_math=3-2j
print(type(adv_math))      # we can realize the data type of this value is complex

print(complex(x))            # now we have changed the value of x in to complex no.


# math opratores  +,-,/,*,%,//,**   we will see one one

a=34
b=20
c=54

total=a-b+c           # python do every thing in order that we put.
print(total)

print(7*3-(2/4)+23)      # we applied four basic opratores once here. pyhton will gonna do by follow BODMAS rule.
print(7*3-2/4+23)         # there is no difference in the out put.

print(a*c/b*a-b)      # agin python will follow BODMAS to solve this problem. if division and mult comes once they have the sme priority so calculate lefrt to right.
print(c/a)

average=(a+b+c)/3         # since python will apply BODMAS first calclate values in side brace the divide to 3 
print("the average of the values is ",average)      
# Here I appleid four basic oprators in different way.

print(a//b)              # it got 1.7 but round to 1 so, // is used to don't get float value so, after calculation python gonna round to the previous whole number regardless of rounding rule which is(if>5 then round to previous  else>=0.5 then round to next).
total_value=a**4          # (to apply orders like sqr,cube,the power of 4 or 7...)we will get a*a*a*a  this is how exaclty apply square roots in python.
print("the power of 4 of 34 is ",total_value)

print("the erminder when 7 divided by 2 is ",7%2)        #to get reminder  only (in this case oupt put is 1) we usually  use it to check whethre this no is even or not .
print(7%3.5)     # here we get reminder 0 but 7 is not even and this is another importance of %.



# rounding  in python they are built in functions
# abs    absoulute and we typically use it to measure distance regardless of direction

print(2-17)  # which is -15 it's not distance bc dis can't be -ve 
print('the distance covered is',abs(2-17))   # absolute no are  +ve any time.



# # floar and ceil
# gpa=3.8345376
# print(gpa.__floor__())









































































