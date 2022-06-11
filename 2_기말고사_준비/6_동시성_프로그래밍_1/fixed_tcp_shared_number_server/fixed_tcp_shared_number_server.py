"""
    공유 자원을 사용하는 프로그램: 개선된 서버
"""
from socket import *
import threading

PORT = 2500
BUF_SIZE = 1024

shared_data = 0


def thread_handler(sock: socket) -> None:
    """ 스레드 핸들러 함수 """
    global shared_data

    lock.acquire()
    for _ in range(10_000_000):
        shared_data += 1
    lock.release()
    print(shared_data)
    sock.send(str(shared_data).encode())
    sock.close()


if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("", PORT))
    s.listen(5)
    lock = threading.Lock()

    while True:
        client, addr = s.accept()
        print("connected by", addr)
        th = threading.Thread(target=thread_handler, args=(client,))
        th.start()

    s.close()