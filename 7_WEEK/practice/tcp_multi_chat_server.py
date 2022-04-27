from socket import *
import threading
import time

PORT = 3333
BUFFSIZE = 1024
client_sockets = []

s = socket(AF_INET, SOCK_STREAM)
s.bind(("", PORT))
s.listen(1)

print("Server Started")

def server_thread(conn, addr):
    """ 서버 쓰레드 실행 동작 """

    while True:
        # 데이터 받기
        data = conn.recv(BUFFSIZE)

        # "quit" 종료
        if "quit" in data.decode():
            if conn in client_sockets:
                print(addr, "exited")
                client_sockets.remove(conn)
                break

        # 새로운 클라이언트이면 목록에 추가
        if conn not in client_sockets:
            print("new client", addr)
            client_sockets.append(conn)

        print(f"{time.asctime()}{str(addr)}:{data.decode()}")

        # 모든 클라이언트에게 전송
        for client in client_sockets:
            if client != conn:
                client.send(data)

    conn.close()

while True:
    conn, addr = s.accept()

    th = threading.Thread(target=server_thread,
                          args=(conn, addr))
    th.start()


s.close()