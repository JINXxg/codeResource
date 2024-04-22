#the ideal in python paramete(format is tuple ) equal c lock unlock
from threading import Thread,Lock,current_thread











'''instance of thread mutex

database_value=0

def increase(lock):
    global database_value
    lock.acquire()#lock acquire and release equal with lock:
    local_copy=database_value
    local_copy+=1
    time.sleep(0.1)
    database_value=local_copy
    lock.release()

if __name__=="__main__":
    print("start")
    lock=Lock()
    thread1=Thread(target=increase,args=(lock,))
    thread2=Thread(target=increase,args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(f"result ",database_value)

    print("end")
'''