#Exeception and Errors just like the exception in java:
'''try ecept block,and else finally also could define erro class by yourself
try:
    a=4+3
    b=4/0
except TypeError as e :
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("all will be fine ")
finally:
    print('you fucker!')
'''
''' two easy way to display exceptions
a=-2
if a<=0:
    raise Exception('variable should positive')


b =-1
assert(b>=0),'b should larger than zero'
'''