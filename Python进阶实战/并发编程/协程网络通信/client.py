from socket import *
def main():
    client=socket(AF_INET,SOCK_STREAM)
    client.connect(('127.0.0.1',8088))
    while True:
        msg=input(">>: ").strip()
        if not msg:
            continue
        client.send(msg.encode("utf-8"))
        msg=client.recv(1024)
        print(msg.decode("utf-8"))

if __name__=="__main__":
    main()
