"""
    멀티스레드 TCP 채팅 프로그램 만들기: 채팅 클라이언트
"""

from socket import *
import threading

PORT = 3333
BUF_SIZE = 1024


def recv_task(sock: socket) -> None:
    """ 반환 함수 """

    while True:
        data = sock.recv(BUF_SIZE).decode()
        print("<-", data)

if __name__ == '__main__':
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(("localhost", PORT))

    th = threading.Thread(target=recv_task, args=(sock,))
    th.start()

    while True:
        msg = input()
        print("->", msg)
        sock.send(msg.encode())