import threading
import time
from threading import Thread

def work():
    time.sleep(3)
    print(threading.current_thread().getName())

def main():
    '''t1=Thread(target=work)
    t1.start()
    print(threading.current_thread().getName())  #查看主进程
    print(threading.enumerate())    #查看有谁在运行
    print(threading.active_count())'''

    t1 = Thread(target=work)
    t1.start()
    print(t1.is_alive())
    t1.join()
    print(t1.is_alive())


if __name__=="__main__":
    main()