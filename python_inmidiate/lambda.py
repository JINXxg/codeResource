#lambda a anonymous function is defined: arguments : expression 
#map(func,value)
#filter(func,seq)

'''filter the element you need 
lis=[1,2,3,4,5,6]
c=filter(lambda x:x%2==0,lis)
print(list(c))

b=[x for x in lis if x%2==0]
print(b)
'''

''' same way to change the element in list 
lis=[1,2,3,4,5]
c=map(lambda x:x*2,lis)
print(list(c))
b=[x*2 for x in lis]
'''

'''lambda use in key to set the key value you need
point_2D=[(1,2),(2,-1),(15,-5),(10,-6)]

point_2D_sorted=sorted(point_2D,key=lambda x:x[1])
print(point_2D,"\n")
print(point_2D_sorted)
'''