#Itertools(use in iteration):product, permutation, combinations(just like math ), accumulate , groupby



'''groupby key and use key=lambda or function set such x<3 or age or some get a dictionary obj the use for output it
from itertools import groupby
a=[1,2,3,4]
def bigger(x):
    return x<3
grop_obj=groupby(a,key=lambda x: x<3)
for key,value in grop_obj:
    print(key,list(value))
'''



'''product mean product the element type you need shuch as list tuple
from itertools import product random copair
a=[1,2]
b=[3]
pro=product(a,b)
print(list(pro))
'''
