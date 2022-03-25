import socket

BUFSIZE = 1024

# 클라이언트에서 TCP 소켓 생성과 연결 요청을 한번에 수행해주는 함수
# socket()과 connect()가 합쳐진것

s = socket.create_connection(("localhost", 2500))

while True:
    msg = input("Message to send: ")
    s.send(msg.encode())
    data = s.recv(BUFSIZE)

    if not data:
        break
    print(f"Received message: {data.decode()}")

s.close()