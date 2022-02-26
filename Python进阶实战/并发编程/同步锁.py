import time,os
import threading
from threading import Thread,Lock,current_thread

n=100

def work(lock):
    global n
    lock.acquire()
    str=threading.current_thread().getName()
    print("%s is running"%str)

    temp=n
    time.sleep(0.1)
    n=temp-1
    lock.release()
def main():
    l = []
    lock=Lock()
    start_time=time.time()
    for i in range(100):
        p=Thread(target=work,args=(lock,))
        l.append(p)
        p.start()

    stop_time=time.time()
    print("主：%s %s"%(stop_time-start_time,n))

if __name__== "__main__":
    main()


