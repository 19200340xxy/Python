import gevent


def task(pid):
    print("task %s done"%pid)

def main():
    '''for i in range(10):
        task(i)'''
    g_l=[gevent.spawn(task,i) for i in range(10)]
    gevent.joinall(g_l)
    print("done")

if __name__=="__main__":
    main()