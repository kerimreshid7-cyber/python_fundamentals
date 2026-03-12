
# first let's see what is control flow is 
# control flow is a logic we write to control how our code runs
# lets classify code in to two 
# 1 straight line code    it just python gonna understand line by line no itration,no loop so we can say the Code we have written up to 
# day 6 was streight forward codes.
# 2 control flow code is a code that is we can command python how we want to run it by writing the logic(control flow).
# so from now on i think i will prctice more control flow codes.
# conditioal statments,loops and functions are good examples of CF

#  I will see one by one. I will gonna master python like Baraa.   so, now lets see logic and oprators
# logic and oprators in this topic we gonna see values(true false),functions(type,bool,all,any,isinstance),comparision oprators(<,=,>...), membership like(in and not in) and identity oprators(is and is not).

# values
print(True)                      
print(False)

# functions(type,bool,all,any,isinstance)               

#type
print(type(True))    # type used to know the type of the value as we saw last weak.

# bool
print(True)
print(bool(123))
print(bool("2y346"))      # the function bool is used to get true or false by passing parameter
print(bool(754.73))     # in these 4 condithions wwe will get True bc we have known values

print(False)
print(bool())
print(bool(0))   #special case i need to understand further 
print(bool(None))          
print(bool(""))        # but, In these 5 conditions we will get false bc we have unknown values.

# all and any   these built functions are used to check miltiple values on
# all to get True all values must be True
# any if there is atleast one  True value the out put put also True
name='kerim'
email='ke77@gmail.com'
phone=''                       # it's empty string and differ from None which is unknown or nothing or no value.
print(any([name,email,phone]))   # oviously it's True bc  we have two true values that satisfy the condition to be true in function any.
print(all([name,email,phone]))   # False bc there is one false value. to be True all values must be true.

s_name='kerim'
s_email='ke77@gmail.com'
s_phone='0976863826' 

print(all([s_name,s_email,s_phone]))   # true bc  the values here are true
print(any([s_name,s_email,s_phone]))  # true bc 'any' get true if atleast one condition is true. 


# isinstance
print(isinstance(23.45,float))    # isinstance(buikt in function) first check the data type of value then return true or false, in htis case we'll get True.
print('kerim'.endswith('m'))       # we can evaluate statments like this
print("SWE".startswith('s'))      # false bc of the case (it's starts with S not s)


