# -*- coding: utf-8 -*-
"""
Created on Fri May 14 09:29:51 2021

@author: 15003
"""

'''import  time
def main():
    print("程序开始执行")
    name=input(">>>")
    print(name)
    time.sleep(1)
    print("程序结束运行")'''
import os
import multiprocessing
import time

def test1(a):
    print("test1 start:",a)
    print("test1的进程id:",os.getpid())
    print("test1的父进程id:",os.getppid())
    time.sleep(1)
    
def test2(a):
    print("test2 start:",a)
    print("test2的进程id:",os.getpid())
    print("test2的父进程id:",os.getppid())
    time.sleep(1)
    
def main():
    print("主进程的id是：",os.getpid())
    t1=multiprocessing.Process(target=test1,args=("x1",))
    t2=multiprocessing.Process(target=test2,args=("x2",))   #args里面最后要写，
    t1.start()
    t2.start()
    print("over")
    
if __name__ == '__main__':
    main()