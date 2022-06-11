"""
    멀티스레드 TCP 채팅 프로그램 만들기: 채팅 서버
"""

from socket import *
import threading

PORT = 3333
BUF_SIZE = 1024


def send_task(sock: socket) -> None:
    """ 보내느 함수 """

    while True:
        resp = input()
        print("->", resp)
        sock.send(resp.encode())


if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("", PORT))
    s.listen(1)
    conn, addr = s.accept()

    th = threading.Thread(target=send_task, args=(conn,))
    th.start()

    while True:
        data = conn.recv(BUF_SIZE)
        print("<-", data.decode())