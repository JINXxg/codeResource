#useage :@function's name 
#decorate is also a function with another function as arguments



''' the second use of decorator

import functools

#i know the decorator function math the argument is func's function as the aim function's decorator
def repeat(numtimes):
    def decoratoer_repeat(func):  
        @functools.wraps(func)
        def wrapper(*args,**kwaargs):
            for _ in range(numtimes):
                result=func(*args,**kwaargs)
            return result
        return wrapper
    return decoratoer_repeat#these return content is what?> all decorator must need wrapper to wrap func info



@repeat(numtimes=5)
def outname(name):
    print(f'hello{name}')

outname('bob')
'''

'''
#the modle to use decorator

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwaargs):
        #do something before
        result=func(*args,**kwaargs)
        #do something after
        return result
    return wrapper


@my_decorator
def add10(x):
    return x+10


print(add10(2))
'''