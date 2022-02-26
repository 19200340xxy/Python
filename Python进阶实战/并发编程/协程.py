
'''def create_num(all_num):
    print("---1---")
    a,b=0,1
    current_num=0
    while current_num<all_num:
        print("----2-----")
        ret=yield b  #弹出a并暂停，等到重新send后继续执行
        print("----ret---",ret)
        print("---3---")
        a,b=b,a+b
        current_num+=1
        print("----4----")'''
import time
from greenlet import greenlet

def task_1():
    while True:
        print("--1--")
        time.sleep(1)
        yield
def task_2():
    while True:
        print("--2--")
        time.sleep(2)
        yield





def f1():
    res=1
    for i in range(1000):
        res+=1
        time.sleep(1)
        print(res)
        g2.switch()

def f2():
    res=1
    for i in range (2000):
        res+=2
        time.sleep(1)
        print(res)
        g1.switch()
g1=greenlet(f1)
g2=greenlet(f2)
def main():
    '''obj=create_num(10)
    ret=next(obj)
    print(ret)
    ret=obj.send("haha") #send会回到从头开始的下一次的yield
    print(ret)
    ret = obj.send("haha")
    print(ret)'''

    '''def eat(name):
        print("%s 吃了 1" % name)
        g2.switch('小明')
        print("%s 吃了 2" % name)
        g2.switch()

    def play(name):
        print("%s play 1" % name)
        g1.switch()
        print("%s play 2" % name)

    g1=greenlet(eat)
    g2=greenlet(play)

    g1.switch('小红')'''

    start_time=time.time()
    g2.switch()
    stop_time=time.time()
    print(stop_time-start_time)



if __name__ =='__main__':
    main()