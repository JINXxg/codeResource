#use variable name  just use the same reference
#shallow/deep copy use indenpendent copy 
#notice the file name can't same with the object name

import copy

class Animal:
    def __init__(self,name,size) :
        self.name=name
        self.size=size

class Zoo:
    def __init__(self,animal) :
        self.animal=animal

animal=Animal("bird",30)
zoo=Zoo(animal)
zoo_clon=copy.deepcopy(zoo)
zoo_clon.animal.name="pig"
print(zoo_clon.animal.name)
print(zoo.animal.name)
'''origin=[1,2,3,4]
#1.copy=copy.copy(origin)
#copy=origin.copy()
#copy=origin[:]

copy[2]=2
print(copy)

print(origin)
'''
'''shallow copy use the variable name
origin=[1,2,3,4,5]
copy=origin
copy[2]=2
print(copy)

print(origin)
'''