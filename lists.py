"""
    infor you should know about list [],dulacates elements
    for i in lstt : in python if this variable is with sequnce could use for to 
    if elemnts's name in mylist:
    else:
    
"""
'''
list_org=["banana","apple","watermelon"]
if list_cpy=list_org mean's reference same location
list_cpy=list_org[:] equal list(list_org), list_org.copy() it real copy
list_cpy.append("cherry")
print(list_org)
print(list_cpy)
'''

''' mylist also can be use algorithm comput
mylist=[0]*5
print(mylist)
mylist2=[1,2,3,4]
new_list=mylist+mylist+mylist2*2
print(new_list)
'''
'''sort your list
    mylists.sort() sort() method without retrun 
    so
    print(mylists.sort()) is print None
    if wanna create a new list with sorce list sorted use 
    new_list=sorted(mylists)
'''
'''clear all elements
mylists.clear()
print(mylists)
'''
"""
    for x in mylists:
        print(x)
"""

'''check element's
if "your mother fucker" in mylists:
    print("yes")
else:
    print("no")
'''

'''append element ant print it's len
mylists.append("you mother fucker")
print(len(mylists))
print(mylists)
'''
'''pop element like data structure the elemets no longer contain
print(mylists.pop())
print(mylists)
'''
'''remove the specify data seem like in datastruct
mylists.remove("sb2")
print(mylists)
'''
