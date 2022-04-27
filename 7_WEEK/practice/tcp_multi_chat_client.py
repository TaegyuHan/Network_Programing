from socket import *
import threading

PORT = 3333
BUFFSIZE = 1024

def handler(sock):
    while True:
        try:
            msg = sock.recv(BUFFSIZE)
            print(msg.decode())

        except ConnectionAbortedError:
            break

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("localhost", PORT))

my_id = input("ID를 입력하세요: ")
sock.send((f"[{my_id}]").encode())

th = threading.Thread(target=handler, args=(sock,))
th.start()

while True:
    input_data = input()
    msg = f"[{my_id}]" + input_data
    sock.send(msg.encode())

    if input_data == "quit":
        break

sock.close()