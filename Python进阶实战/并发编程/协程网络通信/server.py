from gevent import monkey;monkey.patch_all()
import gevent
from socket import *

def server(server_ip,port):
    s=socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind((server_ip,port))
    s.listen(5)
    while True:
        conn,addr=s.accept()
        gevent.spawn(talk,conn,addr)

def talk(conn,addr):
    try:
        while True:
            res=conn.recv(1024)
            print("client %s:%s  msg:%s "%(addr[0],addr[1],res.decode("utf-8")))
            conn.send(res.upper())
    except Exception as e:
        print(e)
    finally:
        conn.close()
def main():
    server('127.0.0.1',8088)

if __name__=="__main__":
    main()
