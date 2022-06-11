"""
    멀티스레드 에코 서버

    특정 클라이언트로부터 메시지를 받고, 응답하는 부분을 별도 스레드로 구현

    메인 스레드는 클라이언트로부터 연결요청을 받은 후, 서브 스레드를
    생성하는 역할을 수행
        - 새로운 스레드를 생성한 후, 다음 연결요청을 기다림

    서브 스레드는 해당 클라이언트와 통신을 수행
"""

from socket import *
import threading

PORT = 2500
BUF_SIZE = 1024


def echo_task(sock: socket) -> None:
    """ 에코 소켓 연동 후 대기 함수 """
    while True:
        data = sock.recv(BUF_SIZE)

        if not data:  # 데이터 멈춤
            break
        print("Received message:", data.decode())
        socket.send(data)

    sock.close()


if __name__ == '__main__':
    sock = socket(AF_INET, SOCK_STREAM)  # 소켓 생성
    sock.bind(("", PORT))
    sock.listen(5)  # 소켓 통신 가능 수 제한

    while True:
        conn, (remote_host, remote_port) = sock.accept()  # 소켓 통신 대기
        print("connected by", remote_host, remote_port)
        th = threading.Thread(target=echo_task, args=(conn,))
        th.start()
