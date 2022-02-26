import os
import random
import time
from multiprocessing import  Process,Queue
def customer(q):
    while True:
        res=q.get()
        if res==None:
            break
        time.sleep(random.randint(1,3))
        print("%s 吃了 %s"%(os.getpid(),res))
def producer(name,q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res="%s 的 %s "%(name,i)
        q.put(res)
        print("%s 生产了 %s"%(os.getpid(),res))
    q.put(None)  #发出结束信号
def main():
    q=Queue()
    p1 = Process(target=producer, args=("包子",q,))
    p2 = Process(target=producer, args=("汉堡",q,))
    p3 = Process(target=producer, args=("炸鸡",q,))

    c1 = Process(target=customer, args=(q,))
    c2 = Process(target=customer, args=(q,))

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    q.put(None)
    q.put(None)
    q.put(None)
    c1.start()
    c2.start()
if __name__=="__main__":
    main()
