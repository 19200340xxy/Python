import os
import random
import time
from multiprocessing import  Process,Queue,JoinableQueue
def customer(q):
    while True:
        res=q.get()
        if res==None:
            break
        time.sleep(random.randint(1,3))
        print("%s 吃了 %s"%(os.getpid(),res))
        q.task_done()    #向q.join()发送信号数据已经被取走
def producer(name,q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res="%s 的 %s "%(name,i)
        q.put(res)
        print("%s 生产了 %s"%(os.getpid(),res))
    #q.put(None)  #发出结束信号
    q.join()  #生产完毕进行阻塞直到队列中全部内容进行完毕

def main():
    q = JoinableQueue()
    p1 = Process(target=producer, args=("包子", q,))
    p2 = Process(target=producer, args=("汉堡", q,))
    p3 = Process(target=producer, args=("炸鸡", q,))

    c1 = Process(target=customer, args=(q,))
    c2 = Process(target=customer, args=(q,))
    c1.daemon=True
    c2.daemon=True

    p_l=[p1,p2,p3,c1,c2]
    for i in p_l:
        i.start()
    p1.join()
    p2.join()
    p3.join()

    print("主进程开始")
