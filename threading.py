#like create in c 1create process 2 start/execute process 3 join(mean's wait process end and lock main)
#from multiprocessing import Process

from threading import Thread
import os
import time 

def thread_fun():
    for i in range(100):
        i*i
        time.sleep(0.1)

threads=[]
num_thread=10

for i in range(num_thread):
    t=Thread(target=thread_fun)
    threads.append(t)

#starat 
for t in threads:
    t.start()

for t in threads:
    t.join()

print("end main")

''' It's can not execute and I dno't know why
from multiprocessing import Process, freeze_support#still wrong
import os
import time

def testmethod():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == '__main__':
    freeze_support()  # Required for Windows
    processes = []
    num_process = os.cpu_count()

    # create processes
    for i in range(num_process):
        p = Process(target=testmethod)
        processes.append(p)

    # start 
    for p in processes:
        p.start()

    # end
    for p in processes:
        p.join()

    print("end main")
'''