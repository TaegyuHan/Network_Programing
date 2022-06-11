"""
    멀티스레드 에코 서버 (클래스)
"""

from socket import *
import threading

PORT = 2500
BUF_SIZE = 1024


class ServerThread(threading.Thread):
    """ 서버 소켓 클래스 """

    def __init__(self, sock: socket) -> None:
        """ 생성자 """
        threading.Thread.__init__(self)
        self._socket = sock

    def run(self):
        """ 에코 소켓 연동 후 대기 메소드 """
        while True:
            data = self._socket.recv(BUF_SIZE)
            if not data:
                break

            print("Received message:", data.decode())
            self._socket.send(data)
        self._socket.close()


if __name__ == '__main__':
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(("", PORT))
    sock.listen(5)

    while True:
        conn, (remote_host, remote_port) = sock.accept()
        print("connected by", remote_host, remote_port)
        th = ServerThread(conn)
        th.start()