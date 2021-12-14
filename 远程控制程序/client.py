# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:11:28 2021

@author: Administrator
"""

import os
import socket

def main():
    s=socket.socket(socket.AF_INET,sock.SOCK_STREAM)
    host="192.168.70.1"
    port=12345
    s.connect((host,port))
    
    while True:
        data_recv=s.recv(1024)
        print(data_recv.decode("UTF-8"))
        msg=input("send msg:")
        s.send(msg.encode("utf-8"))
    s.close()
        
                
if __name__=="__main_":
    main()