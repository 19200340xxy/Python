import sys,socket
from optparse import OptionParser
from threading import  Thread
def open(ip,port):
    s=socket.socket()
    try:
        s.connect((ip,port))
        return True
    except:
        return False
def scan(ip,port):
    if open(ip,port):
        print("%s host $s port open" %(ip,port))
    else:
        print("%s host $s port close" %(ip,port))

def main():
    usage="usage:xxx.py -i ip -p 端口"
    parse=OptionParser(usage=usage)
    parse.add_option("-i","--ip",type="string",dest="ipaddress",help="your target ip here")
    parse.add_option("-p", "--port", type="string", dest="port", help="your target port here")

    (option,args)=parse.parse_args()
    ip=option.ipaddress
    port=option.port

    defaultport=[135,139,445,1433,3306,3389,5944]
    if ',' in port:
        port=port.split(",")
        a=[]
        for x in port:
            a.append(int(x))
        defaultport=a
        #scan(ip,defaultport)
        for i in defaultport:
            i=int(i)
            s=Thread(target=scan,args=(ip,i))
            s.start()
    elif "-"in port:
        port=port.split("-")
        s=int(port[0])
        e=int(port[1])
        for i in range(s,e):
            s=Thread(target=scan,args=(ip,i))
            s.start()
    elif "all" in port:
        for i in range(65535):
            s = Thread(target=scan, args=(ip, i))
            s.start()
    elif "default" in port:
        for i in defaultport:
            i=int(i)
            s = Thread(target=scan, args=(ip, i))
            s.start()
    pass

if __name__=="__main__":
    main()


