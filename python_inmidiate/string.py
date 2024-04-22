#string :ordered, immutable mean can't change the element already exist, text representation

my_list=[1,2,3,4]
my_list[2]=4
print(my_list)
'''
my_string="How are you going son of beach"
print(my_string.replace("son","father"))

**it's useful way to converse list and string and save time
my_list=my_string.split(" ")
print(my_list)
my_string=" ".join(my_list)
print(my_string)


example of the different reverse  use ''.join extrenmly good
from timeit import default_timer as timer
my_list=['*']*1000
my_string=''
start=timer()
for i in my_list:
    my_string+=i
stop=timer()
print(stop-start)

start=timer()
my_string=''.join(my_list)
stop=timer()
print(stop-start)
'''
'''
basic operation of string
my_string=my_string.strip() to remove wihte space
my_string.upper()
my_string.lower()
my_string.startswith('h')
my_string.endswith('d')
my_string.find('H')
my_string.count('o')
'''

'''
1 acces char and substring use index or slice ::
my_string="Hello World"
char=my_string[1]
substring=my_string[::2] :: is the slice
2 string concanate use +
greeting="Hello"
name="Bob"
sentence=greeting+" "+name

'''

'''
three represent of string 
1
my_string='I\'m  a programer' single quote could use \ to represent fomat
2
my_string="I'm a programer" double quote don't need \
3
my_string="""
Hello \ three quote is use in text. \ could cancel \n
world \
?
"""
'''
