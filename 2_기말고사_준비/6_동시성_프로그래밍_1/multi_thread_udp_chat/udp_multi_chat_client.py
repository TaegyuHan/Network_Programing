"""
    UDP를 이용한 단체 채팅 프로그램 만들기: 클라이언트

    채팅 클라이언트

    최초 실행 시, 'ID'를 입력받아 서버로 전송

    서브 스레드는 채팅 서버로부터 메시지를 수신하여 화면에 출력

    메인 스레드는 사용자의 입력을 받아 서버로 전송
"""
from socket import *
import threading

PORT = 2500
BUF_SIZE = 1024


def handler(sock: socket) -> None:
    """ 데이터 받는 함수 """
    while True:
        msg, addr = sock.recvfrom(BUF_SIZE)
        print(msg.decode())


if __name__ == '__main__':
    svr_addr = ("localhost", PORT)
    sock = socket(AF_INET, SOCK_DGRAM)

    my_id = input("ID를 입력하세요: ")
    sock.sendto(f"[{my_id}]".encode(), svr_addr)

    th = threading.Thread(target=handler, args=(sock,))
    th.daemon = True
    th.start()

    while True:
        data = input()
        msg = f"[{my_id}] " + data
        sock.sendto(msg.encode(), svr_addr)

        if data == "quit":
            break
