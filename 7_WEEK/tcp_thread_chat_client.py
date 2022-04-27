from socket import *
import threading

port = 3333
BUFFSIZE = 1024

def recv_task(sock):
    while True:
        data = sock.recv(BUFFSIZE)
        if data:
            break
        print("<-", data.decode())


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("localhost", port))

th = threading.Thread(target=recv_task, args=(sock,))
th.daemon = True # 메인쓰레드가 종료하면 종료
th.start()

while True:
    msg = input()
    print("->", msg)
    sock.send(msg.encode())