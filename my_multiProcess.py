from multiprocessing import Process,Lock, Value,Array
from multiprocessing import Queue
from multiprocessing import Pool  # it's auto control multiprocess use map ,then close then join apply(use for onlly one)

import time

#process pool just like the process controler
def cube(numbers):
    return numbers*numbers*numbers

'''
method for queue
def square(numbers,q):
    for i in numbers:
        q.put(i*i)

def make_double(numbers,q):
    for i in numbers:
   
         q.put(2*i)

'''

'''
method for Array
def add_100(numbers,lock):
    for i in range(100):
        time.sleep(0.1)#here is set the race condition
        for i in range(len(numbers)):
            with lock:#repalce lock.require() and lock.release()
                numbers[i]+=1    
'''
#seconde is use Queue to realize this
if __name__ == "__main__":
    numbers=range(11)
    pool=Pool()

    result=pool.map(cube,numbers)
    pool.close()
    pool.join()

    print(result)
    '''q=Queue()

    p1=Process(target=square,args=(numbers,q))
    p2=Process(target=make_double,args=(numbers,q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print("num:",q.get())
    
    
    
    
    
    
    '''
    
    
    '''
    data type Array   
    shared_memory = Array('d', [0,100,200])
    lock=Lock()
    start=time.time()
    print("beginging number is",shared_memory[:])

    p1 = Process(target=add_100, args=(shared_memory,lock))
    p2 = Process(target=add_100, args=(shared_memory,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end=time.time()#wdf time.time() function is mine?

    print("end value:", shared_memory[:])
    print("execute time",start-end)
    '''

