import time
from multiprocessing import Process
import os
def foo():
    print("foo start")
    time.sleep(1)
    print("foo stop")
def bar():
    print("bar start")
    time.sleep(5)
    print("bar stop")
def main():
    print("main start")
    p1 = Process(target=foo)
    p2 = Process(target=bar)
    p1.daemon = True  #开启守护进程，父进程执行完后p1代码立刻停止运行
    p2.daemon = True
    p1.start()
    p2.start()
    time.sleep(1)
    print("main stop")
if __name__=="__main__":
    main()