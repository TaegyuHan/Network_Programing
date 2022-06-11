"""
    selectors를 이용한 에코 서버

"""

import selectors
import socket

sel = selectors.DefaultSelector()  # 이벤트 처리기(셀럭터) 생성

PORT = 2500
BUF_SIZE = 1024

def accept(sock: socket, mask) -> None:
    """ 연결 처리 함수 """
    conn, addr = sock.accept()
    print("connected from", addr)
    sel.register(conn, selectors.EVENT_READ, read)  # 클라이언트 소켓을 이벤트 처리기에 등록


def read(conn: socket, mask) -> None:
    """ 수신한 데이터를 처리해주는 함수 """
    data = conn.recv(BUF_SIZE)
    if not data:
        sel.unregister(conn)
        conn.close()
        return
    print("received data:", data.decode())
    conn.send(data)


if __name__ == '__main__':

    sock = socket.socket()
    sock.bind(("", PORT))
    sock.listen(5)

    # 소버 소켓(신규 클라이언트 연결을 처리하는 소켓)을 이벤트 처리기에 등록
    sel.register(sock, selectors.EVENT_READ, accept)
    while True:
        events = sel.select()  # 등록된 객체에 대한 이벤트 감시 시작
        for key, mask in events:  # 발생한 이벤트를 모두 검사
            callback = key.data  # key.data: 이벤트 처리기에 등록함 callback 함수
            callback(key.fileobj, mask)  # callback 함수 호출