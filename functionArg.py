"""
-The difference between arguments and patameter
-Positional and keyword arguments
-Default arguments
-Variable-length arguments(*args and **kwargs)
-Container unpancking into function arguments
-Loca vs Global arguments
-Parameter passing (by value or by reference?)
"""

#emm in python if you pass the immutable value as parameter it's as reference value in c if you wanna chenge it you need use another variable
#pass the muttable value as reference addr as c
def muttable(a_list):
    a_list[0]=1000

my_list=[1,2,3,4]
muttable(my_list)
print(my_list)

def immutable(b):

    b=4

b=0
immutable(b)
print(b)


def global_variable():
    global number#if reference the out number you want to change it must add global
    x=number
    number=4
    print("this number is ",x)
 
number=0
global_variable()
print(number)
'''
def unpacking_arg(a,b,c):
    print(a,b,c)

my_list={'a':1,'c':2,'b':3}#the key must same as parameters
unpacking_arg(**my_list)# **use in dictionary 
    
def variable_length(b,a,*args,** kwargs):#this is mean's args(as tuple) can put any numbers of argumetns kwargs(must use keyword=valuse as arguments as it's dic)
    print(a,b)
    for arg in args:#after the *args must be kwargs
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

variable_length(1,2,3,4,5,6,7,eight=8,nine=9,tne=10)
def foo(a,b,c,d=5):#here is parameter:  d is default parameter if withot arguments it use default it and must be at the end
    print(a,b,c,d)

foo(c=1,b=2,a=3)#kerword arguments
foo(1,2,3,9)#positional arguments
'''