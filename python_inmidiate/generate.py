#generate is a function to generate items
#advantage memory efficientive 
#like itself if you need then generate so it's memory saved


'''def fibnacci(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b

fib=fibnacci(30)
for i in fib:
    print(i)
'''

'''the data larger the advantage is more
import sys

def getsum(n):
    nums=[]
    num=0
    while(num<n):
        nums.append(num)
        num+=1
    return nums
def getsum_generator(n):
    num=0
    while(num<n):
        yield num
        num+=1

print(sys.getsizeof(getsum(10000)))
print(sys.getsizeof(getsum_generator(10000)))
'''


'''def countup(num):
    print("startinhg")
    while(num<0):
        yield num
        num+=1


cp=countup(-5)
print(next(cp))
print(next(cp))
print(next(cp))
print(next(cp))
print(next(cp))
print(next(cp))
'''
'''generate 

def my_generate():
    yield 1
    yield 2
    yield 3
1
g=my_generate()
print(sorted(g))


2 each time genrate only one item
value=next(g)
print(value)

    
3   
    for i in g:
        print(i)
'''