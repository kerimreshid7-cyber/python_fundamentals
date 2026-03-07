      
    #today i am gonna to cover data type,string, and transformation

Name="kerim reshid" 
age=23
email='kerim15.gamil.com'
nicname="7"        #these three are string while having integers but if the no are inside quotes are considered as str.
id=1723                #int stors not in the air but python gonna and connect as an object to class integer.
                        #so, All data types(int,str,flo,bool,None) are classes. and when we store a values python save as object by connecting to classes.
print (Name+str(age))     # data types are case sensetives
print(Name,age)           # these 10 and 11 are how can we print multiple variables once code definatly works bc we are  adding some data type string  
print("your age is: "+str(age))
total_sale=34000.45    #float
                      
is_profitable=True      #boolean 
k=False           # unlike others bool is case sensetive the 1st letter must be capital other must be small letters.
salary=None       # None is no value,nothing or unknown i don't have values for variable. and, it's case sensetive simmilar with bool.
name=""           # str - blank  It's complitly different from None bc python treate this as string,will create memory space and we call it blank.
name="  "         # str - empty space.
                  # and i have realised there are complex,date,time and datetime data types in python.
# python has saved these all values by creating exact memory space. and they are primitive(int,flo,str,bool) daata types.
# python is smart enough  to  knows the data type automatically by seeing the value.
#  unlike java or c++ which we have to declare data type like int id=1723

# why data types are necessary?
#  bc data types help python to  decide what function or business logic is allowed to that value(data) inside variable.
basics={
"function": "do some thing on the data",
  "data":'is raw facts that we are gonna to analyse, change to info or insight even wisdom to solve real life problems.'
}            
print(basics)     # I am just trying to apply  the concept of dictionary from my memory. dictionaries are multiple value data types like tuple,list,array and set.

# the dnce bn function and methode 
# function is a block of codes that perform or do specific task and we can reuse it any time we want
print("something")    #define fun name then pass a value.
print(type(name))     # this is afunction(type) inside another fun(print) and used to see the data type.
print(len(name))      # used to see the length of our data value.
print(name.upper())   # here we used method inside a function  
# and we can create functions to reuse it  we will see it around last days in detail.

# methods belongs to objects/class
# print("SOMETHING".lower())          #first value then function name with parentesis   this is syntax of methode a
# print("letters".upper()) #and this is how method differ from function we usually use it inside function.
# print(id.bit_length())    #so now we can see the length of the id in bit 
 
 # in summery data type is the most fundamental concept in python bc it will store the values in appropriate memory space and 
 # values are  objects that belongs to a class. class(int,str)  values(7,kerim)
 # that decide which opration or function is allowed to data values so when we use inappropriate function it return error with discription.
 # data types are not permament we can change them any time we want.
#  there are 3 types of data types in python
#    1 None  it is to show nothing,unknown,no value
#    2 single or priliminary (int,str,bool,float,complex)
#    3 multiple (set,tuple,array,lists and dictionaries)
#  I will cover these all one by one in detail. the most is string so let me start with string 





 # string  is the most fundamental data type in python bc in companies 80% of data are texts
 # so, we have to proccess analyse transform those datas. understanding string bhnd the sign is 
 # not an option.  that is why i am covering the video word by word.  
              # type and str 
    #  1 types    
             
# print(type(Name))   # we can show what type of data the Name is

Name="kerim reshid" 
age=23
age=age-4         # we will show 19 on the upt put 
# 2 str()
# age=23           
# age=str(age)      # we have changed the age from integer to string. 
# age=age-4         # so now in syntax it's correct but it's error in the out put bc we can't add str and int.

# 2 math (len and count)
  #  len(length) used to know the exact lenth of the text. even if there are white spaces it will count them.
print(len(Name))    #it will count spaaces also we will have to see 12 on the out put
print(len(age))     # it will return error bc one one the use of data type is differntiate function or oprater is allowe or not. Here is integer so using len for int is not allowed.

    # count

text="""
kerim is smart student.
every body in the  viallage knows kerim by his commitment.
Kerim is SWE student at haramaya university."""
print(text.count("kerim"))

































