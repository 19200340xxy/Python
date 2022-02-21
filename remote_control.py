import socket


def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host="10.3.12.101"
    port=12345
    s.connect((host,port))


    while True:
        data_recv=s.recv(1024)
        print(data_recv.decode("UTF-8"))
        msg=input("send msg：")
        s.send(msg.encode("UTF-8"))
    s.close()




if __name__=="__main__":
    main()