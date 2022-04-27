from socket import *
import threading


PORT = 2500
BUFSIZE = 1024


def echo_task(sock):
    while True:
        data = sock.recv(BUFSIZE)
        if not data:
            break
        print("Received message:", data.decode())
        sock.send(data)

    sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("", PORT))
sock.listen(5)


while True:
    conn, (remote_host, remote_port) = sock.accept()
    print("connected by", remote_host. remote_port)
    th = threading.Thread(target=echo_task, args=(conn,))
    th.start()