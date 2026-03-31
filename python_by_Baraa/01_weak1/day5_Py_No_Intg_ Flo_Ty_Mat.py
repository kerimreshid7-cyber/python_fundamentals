 
    #  python numbers

#type is built in function in python
# 1 type to know the type of the value,2 int we can use to change the value in to integer fro ex. from string,
# 3 float to change to float and 4 complex to change to complex. these  are python built in functions.
x=12 
print(type(x))
salary="3400"
print(int(salary)*1.10)     #here we are changing the str to int and apply opratore * to increase the salary by 10%.
phone="092863339"
print(int(phone))          # i got the no starting from 9 it doesn't include 0 i thing 0 is not valid value for int class.

gpa='3.83'
print(float(gpa))          # we will show float which is the data type of the value. then to see  the data type we can apply type(gpa).

adv_math=3-2j
print(type(adv_math))      # we can realize the data type of this value is complex

print(complex(x))            # now we have changed the value of x in to complex no.


# math opratores  +,-,/,*,%,//,**   we will see one one

a=34
b=20
c=54
d=38

# d=d+7        # we are increasing d by 7  there is anothe simple way let me show you.
print(d)
d+=7 
print(d)         # the same calculation to the above. but a litttle bit smart.

total=a-b+c           # python do every thing in order that we put.
print(total)

print(7*3-(2/4)+23)      # we applied four basic opratores once here. pyhton will gonna do by follow BODMAS rule.
print(7*3-2/4+23)         # there is no difference in the out put.

print(a*c/b*a-b)      # agin python will follow BODMAS to solve this problem. if division and mult comes once they have the sme priority so calculate left to right.
print(c/a)

average=(a+b+c)/3         # since python will apply BODMAS first calclate values in side brace the divide to 3 
print("the average of the values is ",average)      
# Here I appleid four basic oprators in different way.

print(a//b)              # it got 1.7 but round to 1 so, // is used to get int value not decimal or fraction. so, after calculation python gonna round to the previous(floor rounding) whole number regardless of rounding rule which is(if>5 then round to previous  else>=0.5 then round to next).
total_value=a**4          # (to apply orders like sqr,cube,the power of 4 or 7...)we will get a*a*a*a  this is how exaclty apply square roots in python.
print("the power of 4 of 34 is ",total_value)

print("the erminder when 7 divided by 2 is ",7%2)        #to get reminder  only (in this case oupt put is 1) we usually  use it to check whethre this no is even or not .
print(7%3.5)     # here we get reminder 0 but 7 is not even and this is another importance of %.



# rounding  in python they are built in functions
# abs    absoulute and we typically use it to measure distance regardless of direction

print(2-17)  # which is -15 it's not distance bc dis can't be -ve 
print('the distance covered is',abs(2-17))   # absolute no are  +ve any time.

result=3.83436778
print(round(result))     # I got 4 bc I didn't defined the decimal then python round it to ceil 

print(round(result,2))    #I got 3.83 this is how can we get rounded int value what ever we want from python. by the way it's my fresh man result.

rou_res=3.83436778.__round__(2)  # agian I got 3.83. this is another way to print the above code.and i realize we can't pass int round function with out integer.
print(rou_res)

d=2.5
e=3.5
f=4.5
y=5.5
u=6.5
print(round(y))
print(round(f))
print(round(u))
print(round(e))
print(round(d))
#python rounding with .5 situation always it will round the value to even (it may be floor or ceil) but one simple rule
# is looking for even then round to it 3.5 to 4 again 4.5 to 4


dnce=2-6
print(abs(dnce))
grade=3.965273674
print(round(grade,2))
print(round(grade))




































