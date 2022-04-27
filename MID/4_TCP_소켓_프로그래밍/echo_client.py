from socket import *

port = int(input("Port No: ")) # 포트 입력
address = ("localhost", port)
BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM) # 소켓 연결
s.connect() # 연결

while True:
    msg = input("Message to send: ") # 메시지 입력
    s.send(msg.encode()) # 데이터 전송
    data = s.recv(BUFSIZE) # 데이터 받기
    print(f"Received message: {data.decode()}")

s.close() # 소켓 끊기