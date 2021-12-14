# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:34:01 2021

@author: 15003
"""
"""def main():
    usage="usage:xxx.py -f<filename> -i<ipaddress>"
    parser=OptionParser(usage=usage)   #添加USAGE方法
    parser.add_option("-f","--file",type="string",dest="filename",help="your filename name here")
    parser.add_option("-i","--ipaddress",type="string",dest="ipadd",help="your ipaddress name here")
    (options,args)=parser.parse_args()
    
    print(options.filename)
    print(options.ipadd) """
import socket
from optparse import OptionParser
def open(ip,port):
    s=socket.socket()
    try:
        s.connect((ip,port))
        return True
    except:
        print("连接失败")
        return False
    
def scan(ip,port):
    for x in port:
        if open(ip,x):
            print("%s host %s is open"%(ip,x))
        else:
            print("%s host %s is close"%(ip,x))
def rscan(ip,s,e):
    for x in range(s,e):
        if open(ip,x):
            print("%s host %s is open"%(ip,x))
        else:
            print("%s host %s is close"%(ip,x))
def main():
    usage="usage:xxx.py  -i ip地址 -p 端口"
    parser=OptionParser(usage=usage)   #添加USAGE方法
    parser.add_option("-i","--ip",type="string",dest="ipaddress",help="your target ip here")
    parser.add_option("-p","--port",type="string",dest="port",help="your target port here")
    (options,args)=parser.parse_args()
    
    ip=options.ipaddress
    port=options.port       
    
    defaultport=[80,135,139,445,3306,3389,8080]
    
    if "," in port:
        port=port.split(",")
        a=[]
        for x in port:
            a.append(int(x))
        Scan(ip,a)
    elif '-' in port:
        port=port.split("-")
        s=int(port[0])
        e=int(port[1])
        rscan(ip,s,e)
    elif 'all' in port:
        rscan(ip,1,65535)
    elif 'default 'in port:
        Scan(ip,defaultport)

if __name__ == '__main__':
    main()