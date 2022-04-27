from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 9999)) # 자신의 서버 이름 ("ip", 포트번호)
s.listen(5) # backlog : 한번에 받을 소켓

while True:
    client, addr = s.accept() # 클라이언트 소켓과 연결
    print("connection from ", addr) # 주소 프린트
    client.send(time.ctime(time.time()).encode()) # 시간
    client.close() # 클라이언트 소켓 연결 끊기