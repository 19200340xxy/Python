import time
from multiprocessing import Process,Pool
def func(n):
    for i in range(10):
        print(n+1)
def main():
    start=time.time()
    pool=Pool(5)
    pool.map(func,range(100))
    t2=(time.time()-start)


