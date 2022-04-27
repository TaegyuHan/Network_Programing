from socket import *
import threading

port = 2500
BUFFSIZE = 1024

shared_data = 0

def thread_handler(sock):
    global shared_data
    lock.acquire()
    for _ in range(10000000):
        shared_data += 1
    lock.release()

    print(shared_data)
    sock.send(str(shared_data).encode())
    sock.close()

s = socket(AF_INET, SOCK_STREAM)
s.bind(("", port))
s.listen(5)

lock = threading.Lock()

while True:
    client, addr = s.accept()
    print("connected by", addr)
    th = threading.Thread(target=thread_handler, args=(client,))
    th.start()

s.close()