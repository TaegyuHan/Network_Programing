"""
    select() 함수

    여러 개의 소켓(또는 파일)에 대해 비동기 I/O를 지원하는 함수
"""

import socket, select

socks_list = []  # 소켓 리스트
BUF_SIZE = 1024
PORT = 2500


if __name__ == '__main__':
    server_sock = socket.socket()  # TCP 소켓
    server_sock.bind(("", PORT))
    server_sock.listen(5)

    socks_list.append(server_sock)  # 소켓 리스트에 서버 소켓을 추가
    print(f"{PORT} 에서 접속 대기중")

    while True:
        # 읽기 이벤트(연결요청 및 데이터 수신) 대기
        read_sock, write_sock, except_sock = select.select(socks_list, [], [])

        for s in read_sock:  # 수신(읽기 가능한) 소켓 리스트 검사

            if s == server_sock:  # 새로운 클리이언트의 연결 요청 이벤트 발생
                client_sock, addr = server_sock.accept()
                socks_list.append(client_sock)  # 연결된 클라이언트 소켓을 소켓 리스트에 추가
                print(f"Client ({addr}) connected")

            else:  # 기존 클라이언트의 데이터 수신 이벤트 발생
                data = s.recv(BUF_SIZE)
                if not data:
                    s.close()
                    socks_list.remove(s)  # 연결 종료된 클라이언트 소켓을 소켓 리스트에서 제거
                    continue

                print("Received:", data.decode())
                s.send(data)