import multiprocessing
import os
import time
from  multiprocessing import Process
'''def f(a):
    print("hello",a)
    print("子进程")
def main():
    p_lst=[]
    for i in range(5):
        p=Process(target=f,args=("小明",))
        p.start()
        p_lst.append(p)
    print(p_lst)
    print("主进程")'''
def test1():
    print("test1 start")
    print(os.getpid())
    time.sleep(5)
    print("test1 stop")
def test2():
    print("test2 start")
    print(os.getpid())
    time.sleep(2)
    print("test2 stop")
def main():
    print("main start")
    print(os.getpid())
    t1 = Process(target=test1)
    t2 = Process(target=test2)
    t1.start()
    t2.start()
    #t1.join()
    t2.join()#阻塞进程推进，等到上面两个都完成以后再main stop
    print("main stop")


if __name__=="__main__":
    main()